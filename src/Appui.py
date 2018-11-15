import math
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from src.Point import Point


class Appui(object):
    def __init__(self):
        self.pointList = []
        self.point_curseur = None

    def draw(self, q):
        for i in range(0, len(self.pointList) - 1):
            p1 = self.pointList[i]
            p2 = self.pointList[i + 1]
            largeur = p2.x - p1.x
            hauteur = p2.y - p1.y
            longueur = p2.distance(p1)
            nb_pixmap = int(longueur // 25)
            p = QPen(Qt.red)  # On cree un objet painter
            p.setWidth(5)
            q.setPen(p)
            q.drawLine(p1.x, p1.y, p2.x, p2.y)
            # on determine l'angle de notre ligne par rapport à l'horizontale
            alpha = self.angle_ligne_rad(p1, p2)  # retourne l'angle de notre ligne en radian
            pixmap = QPixmap("./res/t.png")
            tr = QTransform()
            tr.rotateRadians(-alpha)  # rotate tourne le png dans le sens non trigo autour du pixel (0,0)
            tr.translate(pixmap.width() / 2, pixmap.height() / 2)  # not working

            # on l'applique à notre pixmap
            pixmap = pixmap.transformed(tr)

            # Dans cette boucle nous dessinons nbPixmap symboles le long du segment
            for s in range(0, nb_pixmap):
                # distance en abscisse entre le symbole dessiné et le point listeLargages[i-1]
                dx = s * (largeur / nb_pixmap)

                # distance en ordonnée entre le symbole dessiné et le point listeLargages[i-1]
                dy = s * (hauteur / nb_pixmap)

                # on dessine un symbole aux coordonnées x = x de listeLargages[i] + dx
                #                                       y = y de listeLargages[i] + dy
                point = QPoint(p1.x + dx - pixmap.width() / 2, p1.y + dy - pixmap.height() / 2)
                q.drawPixmap(point, pixmap)
            # on dessine le dernier pixmap
            point = QPoint(p2.x - pixmap.width() / 2, p2.y - pixmap.height() / 2)

            q.drawPixmap(point, pixmap)

        # trace le segment entre le curseur et le dernier point du graphe
        dernierPoint = Point(self.pointList[len(self.pointList) - 1].x, self.pointList[len(self.pointList) - 1].y)
        largeur = self.point_curseur.x - dernierPoint.x
        hauteur = self.point_curseur.y - dernierPoint.y
        longueur = self.point_curseur.distance(dernierPoint)
        nb_pixmap = int(longueur // 25)
        p = QPen(Qt.red)  # On cree un objet painter
        p.setWidth(5)
        q.setPen(p)
        q.drawLine(dernierPoint.x, dernierPoint.y, self.point_curseur.x, self.point_curseur.y)
        # on determine l'angle de notre ligne par rapport à l'horizontale
        alpha = self.angle_ligne_rad(dernierPoint, self.point_curseur)  # retourne l'angle de notre ligne en radian
        pixmap = QPixmap("./res/t.png")
        tr = QTransform()
        tr.rotateRadians(-alpha)  # rotate tourne le png dans le sens non trigo autour du pixel (0,0)
        tr.translate(pixmap.width() / 2, pixmap.height() / 2)  # not working

        # on l'applique à notre pixmap
        pixmap = pixmap.transformed(tr)

        # Dans cette boucle nous dessinons nbPixmap symboles le long du segment
        for s in range(0, nb_pixmap):
            # distance en abscisse entre le symbole dessiné et le point listeLargages[i-1]
            dx = s * (largeur / nb_pixmap)

            # distance en ordonnée entre le symbole dessiné et le point listeLargages[i-1]
            dy = s * (hauteur / nb_pixmap)

            # on dessine un symbole aux coordonnées x = x de listeLargages[i] + dx
            #                                       y = y de listeLargages[i] + dy
            point = QPoint(dernierPoint.x + dx - pixmap.width() / 2, dernierPoint.y + dy - pixmap.height() / 2)
            q.drawPixmap(point, pixmap)
        # on dessine le dernier pixmap
        point = QPoint(self.point_curseur.x - pixmap.width() / 2, self.point_curseur.y - pixmap.height() / 2)

        q.drawPixmap(point, pixmap)

    @staticmethod
    def angle_ligne_rad(p1, p2):
        '''
        retourne l'angle que forme le segment[p1 p2] par rapport à l'horizontale en radian
        :param p1: premier point
        :param p2: deuxieme poit
        :return: l'angle que forme le segment[p1 p2] par rapport à l'horizontale en radian
        '''
        teta = 0
        if p1.x == p2.x:  # si la ligne est verticale
            if p1.y <= p2.y:
                teta = math.pi / 2
            else:
                teta = -math.pi / 2
        elif p1.x > p2.x:  # si on est sur la partie droite du cercle trigonométrique
            teta = math.atan((-p2.y + p1.y) / (
                        p2.x - p1.x))  # on remarquera ici l'inversion de p2.y et p1.y due au systeme de coordonées inversé en y
        else:  # si on est sur la partie gauche du cercle trigonométrique
            teta = math.atan(
                (-p2.y + p1.y) / (p2.x - p1.x)) + math.pi  # on ajoute pi par rapport au calcul précédent
        return teta
