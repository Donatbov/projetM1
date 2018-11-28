import sys

from PyQt5 import QtSvg

from Point import Point
from CreationGraphe import CreationGraphe
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
        self.graphe = CreationGraphe()
        self.type_graphe = 0
        self.zoomLevel = 1
        self.choixLargage = QComboBox()
        self.choixLargage.addItem(QIcon("res/hretardant.png"), "")
        self.choixLargage.addItem(QIcon("res/heau.png"), "")
        self.choixLargage.addItem(QIcon("res/cretardant.png"), "")
        self.choixLargage.addItem(QIcon("res/ceau.png"), "")
        self.choixLargage.setToolTip("Choix de largage")

        self.attaqueButton = QPushButton('', self)
        self.envisageButton = QPushButton('', self)
        self.appuiButton = QPushButton('', self)
        self.attaqueJEButton = QPushButton('', self)
        self.attaqueJButton = QPushButton('', self)
        self.attaquePFEButton = QPushButton('', self)
        self.attaquePFButton = QPushButton('', self)
        self.PEPSButton = QPushButton('', self)
        self.PPSButton = QPushButton('', self)

        self.zoomLevel = 1

        self.initUI()

    def initUI(self):
        grid = QGridLayout()  # notre espace de jeu
        grid.addWidget(self.labelPositionCurseur, 0, 0, Qt.AlignTop)
        self.setMouseTracking(True)
        self.setLayout(grid)
        self.setGeometry(200, 100, 1000, 600)  # taille par défautt de la fenetre
        self.setWindowTitle('Santoline')

        self.attaqueButton.setToolTip("attaque")
        self.attaqueButton.setStyleSheet("QPushButton{border-image: url(res/attaqueS.png)}"
                                         "QPushButton:pressed{border-image: url(res/VentPenteLogo.png)}")

        self.envisageButton.setToolTip("envisageButton")
        self.envisageButton.setStyleSheet("QPushButton{border-image: url(res/ligneappuiE.png)}"
                                         "QPushButton:pressed{border-image: url(res/VentPenteLogo.png)}")

        self.appuiButton.setToolTip("Ligne d'appui")
        self.appuiButton.setStyleSheet("QPushButton{border-image: url(res/ligneappui.png)}"
                                         # "QPushButton:hover{border-image: url(attaque.png)}"
                                         "QPushButton:pressed{border-image: url(res/VentPenteLogo.png)}")

        self.attaqueJEButton.setToolTip("attaqueJEButton")
        self.attaqueJEButton.setStyleSheet("QPushButton{border-image: url(res/Jalonnement.png)}"
                                         # "QPushButton:hover{border-image: url(attaque.png)}"
                                         "QPushButton:pressed{border-image: url(res/VentPenteLogo.png)}")

        self.attaqueJButton.setToolTip("attaqueJButton")
        self.attaqueJButton.setStyleSheet("QPushButton{border-image: url(res/Jalonnement.png)}"
                                         # "QPushButton:hover{border-image: url(attaque.png)}"
                                         "QPushButton:pressed{border-image: url(res/VentPenteLogo.png)}")

        self.attaquePFEButton.setToolTip("attaquePFEButton")
        self.attaquePFEButton.setStyleSheet("QPushButton{border-image: url(res/PerceE.png)}"
                                         # "QPushButton:hover{border-image: url(attaque.png)}"
                                         "QPushButton:pressed{border-image: url(res/VentPenteLogo.png)}")

        self.attaquePFButton.setToolTip("attaquePFButton")
        self.attaquePFButton.setStyleSheet("QPushButton{border-image: url(res/Perce.png)}"
                                         # "QPushButton:hover{border-image: url(attaque.png)}"
                                         "QPushButton:pressed{border-image: url(res/VentPenteLogo.png)}")

        self.PEPSButton.setToolTip("PEPSButton")
        self.PEPSButton.setStyleSheet("QPushButton{border-image: url(res/sensible.png)}"
                                         # "QPushButton:hover{border-image: url(attaque.png)}"
                                         "QPushButton:pressed{border-image: url(res/VentPenteLogo.png)}")

        self.PPSButton.setToolTip("PPSButton")
        self.PPSButton.setStyleSheet("QPushButton{border-image: url(res/sensibleE.png)}"
                                         # "QPushButton:hover{border-image: url(attaque.png)}"
                                         "QPushButton:pressed{border-image: url(res/VentPenteLogo.png)}")

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
            self.labelPositionCurseur.setText("x: " + str(e.x()) + " y: " + str(e.y())+" zoom: "+str(self.zoomLevel))
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
            g.draw(q,self.zoomLevel)

    def wheelEvent(self, event):

        self.zoomLevel -= event.angleDelta().y()/1200
        self.update()




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

