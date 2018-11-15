import sys
import math
from Point import Point
from Graphe import Graphe
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *


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

        
        self.initUI()

    def initUI(self):
        grid = QGridLayout()  # notre espace de jeu
        grid.addWidget(self.labelPositionCurseur, 0, 0, Qt.AlignTop)
        self.setMouseTracking(True)
        self.setLayout(grid)
        self.setGeometry(200, 100, 1000, 600)  # taille par défautt de la fenetre
        self.setWindowTitle('Santoline')

        self.choixLargage = QComboBox()
        self.choixLargage.addItems(["Largage HBE au retardant","Largage HBE en eau", "Largage ABE au retardant", "Largage HBE en eau"])
        self.attaqueButton = QPushButton('Attaque', self)
        self.envisageButton = QPushButton('appui envisagee', self)
        self.appuiButton = QPushButton('appui', self)
        self.attaqueJEButton = QPushButton('attaqueJE', self)
        self.attaqueJButton = QPushButton('attaqueJ', self)
        self.attaquePFEButton = QPushButton('attaquePFE', self)
        self.attaquePFButton = QPushButton('attaquePF', self)
        self.PEPSButton = QPushButton('PEPS', self)
        self.PPSButton = QPushButton('PPS', self)


        grid.addWidget(self.choixLargage, 0, 0, Qt.AlignBottom)
        grid.addWidget(self.attaqueButton, 0, 1, Qt.AlignBottom)
        grid.addWidget(self.envisageButton, 0, 2, Qt.AlignBottom)
        grid.addWidget(self.appuiButton, 0, 3, Qt.AlignBottom)
        grid.addWidget(self.attaqueJEButton, 0, 4, Qt.AlignBottom)
        grid.addWidget(self.attaqueJButton, 0, 5, Qt.AlignBottom)
        grid.addWidget(self.attaquePFEButton, 0, 6, Qt.AlignBottom)
        grid.addWidget(self.attaquePFButton, 0, 7, Qt.AlignBottom)
        grid.addWidget(self.PEPSButton, 0, 8, Qt.AlignBottom)
        grid.addWidget(self.PPSButton, 0, 9, Qt.AlignBottom)

        self.choixLargage.currentIndexChanged.connect(self.selectionchangeLargage)
        self.attaqueButton.clicked[bool].connect(self.set_type_attaque)
        self.envisageButton.clicked[bool].connect(self.set_type_envisage)
        self.appuiButton.clicked[bool].connect(self.set_type_appui)
        self.attaqueJEButton.clicked[bool].connect(self.set_type_attaqueJE)
        self.attaqueJButton.clicked[bool].connect(self.set_type_attaqueJ)
        self.attaquePFEButton.clicked[bool].connect(self.set_type_attaquePFE)
        self.attaquePFButton.clicked[bool].connect(self.set_type_attaquePF)
        self.PEPSButton.clicked[bool].connect(self.set_type_PEPS)
        self.PPSButton.clicked[bool].connect(self.set_type_PPS)

        self.show()

    def selectionchangeLargage(self, i):
        if i == 0:
            self.type_graphe = 0
        elif i == 1:
            self.type_graphe = 1
        elif i == 2:
            self.type_graphe = 2
        else:
            self.type_graphe = 3
        self.update()

    def set_type_attaque(self, x):
        self.type_graphe = 4
        self.isNewGraph = False

    def set_type_envisage(self, x):
        self.type_graphe = 5
        self.isNewGraph = False

    def set_type_appui(self, x):
        self.type_graphe = 6
        self.isNewGraph = False

    def set_type_attaqueJE(self, x):
        self.type_graphe = 7
        self.isNewGraph = False
    
    def set_type_attaqueJ(self, x):
        self.type_graphe = 8
        self.isNewGraph = False

    def set_type_attaquePFE(self, x):
        self.type_graphe = 9
        self.isNewGraph = False

    def set_type_attaquePF(self, x):
        self.type_graphe = 10
        self.isNewGraph = False

    def set_type_PEPS(self, x):
        self.type_graphe = 11
        self.isNewGraph = False
    
    def set_type_PPS(self, x):
        self.type_graphe = 12
        self.isNewGraph = False
        
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
            text = "fini"
            self.labelPositionCurseur.setText(text)
            self.update()  # sert a invoquer paintEvent pour effacer le segment en cours

    # fonction qui réagit à l'évènement : raffraichisssement de la fenetre
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

