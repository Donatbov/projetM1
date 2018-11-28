from Graphe import Graphe
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from Point import Point


class AttaqueJ(Graphe):

    def draw(self, q,zoom):
        #Accumulateur servant à repartir les symboles sur de très courts segments
        cumule=0
        for i in range(0, len(self.pointList) - 1):
            p1 = self.pointList[i]
            p2 = self.pointList[i + 1]
            plop1 = Point(p1.x / zoom, p1.y / zoom)
            plop2 = Point(p2.x / zoom, p2.y / zoom)
            p1 = plop1
            p2 = plop2

            largeur = p2.x - p1.x
            hauteur = p2.y - p1.y
            longueur = p2.distance(p1)

            nb_pixmap = int(longueur // (40 / zoom))
            p = QPen(Qt.black)  # On cree un objet painter
            # On dessine la ligne
            p.setWidth(int(2/ zoom))
            q.setPen(p)
            q.drawLine(p1.x, p1.y, p2.x, p2.y)
            # on determine l'angle de notre ligne par rapport à l'horizontale
            alpha = self.angle_ligne_rad(p1, p2)  # retourne l'angle de notre ligne en radian
            pixmap = QPixmap("./res/fleche.png")
            tr = QTransform()
            tr.rotateRadians(-alpha+0.7)  # rotate tourne le png dans le sens non trigo autour du pixel (0,0)
            tr.translate(pixmap.width() / 2, pixmap.height() / 2)  # not working

            # on l'applique à notre pixmap

            pixmap = pixmap.transformed(tr, Qt.SmoothTransformation)
            pixmap = pixmap.scaledToHeight(int(pixmap.height() / zoom), Qt.SmoothTransformation)

            # sert à ne pas dessiner de symboles si le segment est trop petit
            if nb_pixmap == 0:
                cumule += longueur
            else:
                cumule = 0
            if cumule // (40 / zoom) > 0:
                point = QPoint(p1.x - pixmap.width() / 2, p1.y - pixmap.height() / 2)
                q.drawPixmap(point, pixmap)
                cumule = 0

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

        # trace le segment entre le curseur et le dernier point du graphe
        dernierPoint = Point(self.pointList[len(self.pointList) - 1].x, self.pointList[len(self.pointList) - 1].y)
        largeur = self.point_curseur.x - dernierPoint.x
        hauteur = self.point_curseur.y - dernierPoint.y
        longueur = self.point_curseur.distance(dernierPoint)
        nb_pixmap = int(longueur // 40)
        p = QPen(Qt.black)  # On cree un objet painter
        p.setWidth(2)
        q.setPen(p)
        q.drawLine(dernierPoint.x, dernierPoint.y, self.point_curseur.x, self.point_curseur.y)
        # on determine l'angle de notre ligne par rapport à l'horizontale
        alpha = self.angle_ligne_rad(dernierPoint, self.point_curseur)  # retourne l'angle de notre ligne en radian
        pixmap = QPixmap("./res/fleche.png")
        tr = QTransform()
        tr.rotateRadians(-alpha+0.7)  # rotate tourne le png dans le sens non trigo autour du pixel (0,0)
        tr.translate(pixmap.width() / 2, pixmap.height() / 2)  # not working
        # on l'applique à notre pixmap
        pixmap = pixmap.transformed(tr,Qt.SmoothTransformation)

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
        # on l'applique à notre pixmap
        q.drawPixmap(point, pixmap)

