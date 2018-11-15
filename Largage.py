from PyQt5.QtCore import * #Qt
from PyQt5.QtGui import * #QMouseEvent, QPainter
from Point import Point
class LargageHR(object):
    def __init__(self):
        self.pointList = []
        self.point_curseur = None

    def say_hello(self):
        print("hello, this is largage ",end = "\n")

    def draw(self, q):
        pen = QPen(Qt.red)
        q.setPen(pen)
        for i in range(0, len(self.pointList) - 1):
            p1 = self.pointList[i]
            p2 = self.pointList[i + 1]
            largeur = p2.x - p1.x
            hauteur = p2.y - p1.y
            longueur = p2.distance(p1)
            nb_graphe_rond = int(longueur // 8)
            for s in range(0, nb_graphe_rond):
                dx = s * (largeur / nb_graphe_rond)
                dy = s * (hauteur / nb_graphe_rond)
                q.drawEllipse(p1.x + dx - 5, p1.y + dy - 5, 10, 10)

        p = Point(self.pointList[len(self.pointList) - 1].x, self.pointList[len(self.pointList) - 1].y)
        largeur = self.point_curseur.x - p.x
        hauteur = self.point_curseur.y - p.y
        longueur = self.point_curseur.distance(p)
        nb_graphe_rond = int(longueur // 8)
        for s in range(0, nb_graphe_rond):
            dx = s * (largeur / nb_graphe_rond)
            dy = s * (hauteur / nb_graphe_rond)
            q.drawEllipse(p.x + dx - 5, p.y + dy - 5, 10, 10)



class LargageHE(object):
    def __init__(self):
        self.pointList = []
        self.point_curseur = None

    def draw(self, q):
        pen = QPen(Qt.blue)
        q.setPen(pen)
        for i in range(0, len(self.pointList) - 1):
            p1 = self.pointList[i]
            p2 = self.pointList[i + 1]
            largeur = p2.x - p1.x
            hauteur = p2.y - p1.y
            longueur = p2.distance(p1)
            nb_graphe_rond = int(longueur // 8)
            for s in range(0, nb_graphe_rond):
                dx = s * (largeur / nb_graphe_rond)
                dy = s * (hauteur / nb_graphe_rond)
                q.drawEllipse(p1.x + dx - 5, p1.y + dy - 5, 10, 10)

        p = self.pointList[len(self.pointList) - 1]
        largeur = self.point_curseur.x - p.x
        hauteur = self.point_curseur.y - p.y
        longueur = self.point_curseur.distance(p)
        nb_graphe_rond = int(longueur // 8)
        for s in range(0, nb_graphe_rond):
            dx = s * (largeur / nb_graphe_rond)
            dy = s * (hauteur / nb_graphe_rond)
            q.drawEllipse(p.x + dx - 5, p.y + dy - 5, 10, 10)



class LargageAR(object):
    def __init__(self):
        self.pointList = []
        self.point_curseur = None

    def draw(self, q):
        pen = QPen(Qt.red)
        q.setPen(pen)
        for i in range(0, len(self.pointList) - 1):
            p1 = self.pointList[i]
            p2 = self.pointList[i + 1]
            largeur = p2.x - p1.x
            hauteur = p2.y - p1.y
            longueur = p2.distance(p1)
            nb_graphe_rond = int(longueur // 8)
            for s in range(0, nb_graphe_rond):
                dx = s * (largeur / nb_graphe_rond)
                dy = s * (hauteur / nb_graphe_rond)
                q.drawEllipse(p1.x + dx - 5, p1.y + dy - 5, 15, 10)

        p = self.pointList[len(self.pointList) - 1]
        largeur = self.point_curseur.x - p.x
        hauteur = self.point_curseur.y - p.y
        longueur = self.point_curseur.distance(p)
        nb_graphe_rond = int(longueur // 8)
        for s in range(0, nb_graphe_rond):
            dx = s * (largeur / nb_graphe_rond)
            dy = s * (hauteur / nb_graphe_rond)
            q.drawEllipse(p.x + dx - 5, p.y + dy - 5, 15, 8)



class LargageAE(object):
    def __init__(self):
        self.pointList = []
        self.point_curseur = None

    def draw(self, q):
        pen = QPen(Qt.blue)
        q.setPen(pen)
        for i in range(0, len(self.pointList) - 1):
            p1 = self.pointList[i]
            p2 = self.pointList[i + 1]
            largeur = p2.x - p1.x
            hauteur = p2.y - p1.y
            longueur = p2.distance(p1)
            nb_graphe_rond = int(longueur // 8)
            for s in range(0, nb_graphe_rond):
                dx = s * (largeur / nb_graphe_rond)
                dy = s * (hauteur / nb_graphe_rond)
                q.drawEllipse(p1.x + dx - 5, p1.y + dy - 5, 10, 10)

        p = self.pointList[len(self.pointList) - 1]
        largeur = self.point_curseur.x - p.x
        hauteur = self.point_curseur.y - p.y
        longueur = self.point_curseur.distance(p)
        nb_graphe_rond = int(longueur // 8)
        for s in range(0, nb_graphe_rond):
            dx = s * (largeur / nb_graphe_rond)
            dy = s * (hauteur / nb_graphe_rond)
            q.drawEllipse(p.x + dx - 5, p.y + dy - 5, 10, 10)