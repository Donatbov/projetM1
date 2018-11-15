from Point import Point
from PyQt5.QtCore import * #Qt
from PyQt5.QtGui import * #QMouseEvent, QPainter
class AttaqueJ(object):
    def __init__(self):
        self.pointList = []
        self.point_curseur = None

    def say_hello(self):
        print("hello, this is triangle",end = "\n")

    def draw(self, q):
        pen = QPen(Qt.black)
        q.setPen(pen)
        for i in range(0, len(self.pointList) - 1):
            p1 = self.pointList[i]
            p2 = self.pointList[i + 1]
            q.drawLine(p1.x, p1.y, p2.x, p2.y)

        p = Point(self.pointList[len(self.pointList) - 1].x, self.pointList[len(self.pointList) - 1].y)
        q.drawLine(p.x, p.y, self.point_curseur.x, self.point_curseur.y)
