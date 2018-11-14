import sys
import math

from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *

from Point import Point
from Graphe import Graphe

class Example(QWidget):

    def __init__(self):
        super().__init__()
        self.labelPositionCurseur = QLabel()  # le label dans lequel on affiche le texte
        self.pos = None  # position du curseur (contient un champ x et un champ y)
        self.isNewGraph = False  # sert à determiner si on commence un nouveau graphe ou non
        self.listeGraphe = []
        self.grapheCourrant = None
        self.graphe = Graphe()
        self.type_graphe = 0

        self.largageButton          = QPushButton('Largage', self)
        self.lineTriangleButton     = QPushButton('LineTriangle', self)

        self.initUI()

    def initUI(self):
        grid = QGridLayout()  # notre espace de jeu
        grid.addWidget(self.labelPositionCurseur, 0, 0, Qt.AlignTop)
        self.setMouseTracking(True)
        self.setLayout(grid)
        self.setGeometry(200, 100, 1000, 600)  # taille par défautt de la fenetre
        self.setWindowTitle('Santoline')

        grid.addWidget(self.largageButton, 0, 1, Qt.AlignBottom)
        grid.addWidget(self.lineTriangleButton, 0, 4, Qt.AlignBottom)

        self.largageButton.clicked[bool].connect(self.set_type_largage)
        self.lineTriangleButton.clicked[bool].connect(self.set_type_line_triangle)

        self.show()

    # fonction qui réagit à l'évènement : la souris bouge
    def mouseMoveEvent(self, e):
        self.pos = e.pos()
        if self.isNewGraph:
            self.labelPositionCurseur.setText("x: " + str(e.x()) + " y: " + str(e.y()))
            self.grapheCourrant.point_curseur = Point(e.x(), e.y())
            self.update()

    # fonction qui réagit à l'évènement : appuis sur n'importe quel bouton de la souris
    def mousePressEvent(self, event: QMouseEvent) -> None:
        if event.button() == Qt.LeftButton:
            if not self.isNewGraph:
                self.isNewGraph = True
                self.grapheCourrant = self.graphe.create(self.type_graphe)
                self.listeGraphe.append(self.grapheCourrant)

            self.grapheCourrant.point_curseur = Point(event.x(), event.y())
            self.labelPositionCurseur.setText("click")
            b = Point(event.x(), event.y())
            self.grapheCourrant.pointList.append(b)
            
        elif event.button() == Qt.RightButton:
            self.isNewGraph = False
            self.labelPositionCurseur.setText("fini")


    def paintEvent(self, event):
        q = QPainter(self)
        for g in self.listeGraphe:
            g.draw(q)

    def set_type_largage(self, x):
        self.type_graphe = 0
        self.isNewGraph = False

    def set_type_line_triangle(self, x):
        self.type_graphe = 1
        self.isNewGraph = False

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())

