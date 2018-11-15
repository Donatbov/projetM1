from Point import Point
from PyQt5.QtCore import * #Qt
from PyQt5.QtGui import * #QMouseEvent, QPainter
class AttaquePF(object):
    def __init__(self):
        self.pointList = []
        self.point_curseur = None

    def say_hello(self):
        print("hello, this is triangle",end = "\n")

    def draw(self, q):
        pen = QPen(Qt.black)
        q.setPen(pen)
        icon = QPixmap("./res/perce.png")
        if(len(self.pointList)>=1):
            p1 = QPoint(self.pointList[0].x- icon.width() / 2, self.pointList[0].y - icon.height() / 2)
            q.drawPixmap(p1, icon)
        for i in range(0, len(self.pointList) - 1):
            p1 = QPoint(self.pointList[i+1].x- icon.width() / 2, self.pointList[i+1].y - icon.height() / 2)
            q.drawPixmap(p1, icon)

        point = QPoint(self.point_curseur.x - icon.width() / 2, self.point_curseur.y - icon.height() / 2)
        q.drawPixmap(point, icon)