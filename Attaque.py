import math

from Point import Point
from PyQt5.QtCore import * #Qt
from PyQt5.QtGui import * #QMouseEvent, QPainter


class Attaque(object):
    def __init__(self):
        self.pointList = []
        self.point_curseur = None

    def say_hello(self):
        print("hello, this is triangle",end = "\n")

    def draw(self, q):
        pen = QPen(Qt.black)
        pen.setWidth(3)
        q.setPen(pen)
        icon = QPixmap("./res/tete.png")
        for i in range(0, len(self.pointList) - 1):
            p1 = self.pointList[i]
            p2 = self.pointList[i + 1]
            q.drawLine(p1.x, p1.y, p2.x, p2.y)
        dernierPoint = Point(self.pointList[len(self.pointList) - 1].x, self.pointList[len(self.pointList) - 1].y)
        alpha = self.angle_ligne_rad(dernierPoint, self.point_curseur)
        p = QPoint(self.point_curseur.x - icon.width() / 2, self.point_curseur.y - icon.height() / 2)
        q.drawLine(self.pointList[len(self.pointList) - 1].x, self.pointList[len(self.pointList) - 1].y, self.point_curseur.x, self.point_curseur.y)

        tr = QTransform()
        tr.rotateRadians(-alpha)  # rotate tourne le png dans le sens non trigo autour du pixel (0,0)
        # on l'applique à notre pixmap
        icon = icon.transformed(tr)
        q.drawPixmap(p, icon)


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