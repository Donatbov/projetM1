import sys
import math
from PyQt5.QtCore import Qt, QPoint
from PyQt5.QtWidgets import QWidget, QApplication, QGridLayout, QLabel
from PyQt5.QtGui import QMouseEvent, QPainter


class Example(QWidget):

    def __init__(self):
        super().__init__()

        QPoint
        x = 0
        y = 0
        self.nbGraphe = 0  # c'est le nombre de graphes
        self.isNewGraph = False  # sert à determiner si on commence un nouveau graphe ou non
        self.listeLargages = [[]]  # liste contenant les graphes des largages
        self.text = "x: {0},  y: {1}".format(x, y)  # le texte qui va aller dans le label
        self.labelPositionCurseur = QLabel(self.text, self)    # le label dans lequel on affiche le texte
        self.pos = None     # position du curseur (contient un champ x et un champ y)

        self.initUI()

    def initUI(self):
        grid = QGridLayout()    # notre espace de jeu
        grid.addWidget(self.labelPositionCurseur, 0, 0, Qt.AlignTop)
        self.setMouseTracking(True)
        self.setLayout(grid)
        self.setGeometry(200, 100, 1000, 600)   # taille par défautt de la fenetre
        self.setWindowTitle('Zhang Lei')
        self.show()

    # fonction qui réagit à l'évènement : la souris bouge
    def mouseMoveEvent(self, e):
        self.pos = e.pos()
        if self.isNewGraph:
            x = e.x()
            y = e.y()
            text = "x: {0},  y: {1}".format(x, y)
            self.labelPositionCurseur.setText(text)
            self.update()

    # fonction qui réagit à l'évènement : appuis sur n'importe quel bouton de la souris
    def mousePressEvent(self, event: QMouseEvent) -> None:
        if event.button() == Qt.LeftButton:
            if not self.isNewGraph:
                self.listeLargages.append([])
                self.nbGraphe += 1

            self.isNewGraph = True
            text = "click"
            self.labelPositionCurseur.setText(text)
            a = [event.x(), event.y()]
            self.listeLargages[self.nbGraphe - 1].append(a)
        elif event.button() == Qt.RightButton:
            self.isNewGraph = False
            text = "fini"
            self.labelPositionCurseur.setText(text)
            self.update()   # sert a invoquer paintEvent pour effacer le segment en cours

    # fonction qui réagit à l'évènement : raffraichisssement de la fenetre
    def paintEvent(self, event):
        # pour dessiner tous les graphes precedents
        if self.nbGraphe >= 2:
            for i in range(0, self.nbGraphe - 1):
                for j in range(1, len(self.listeLargages[i])):
                    self.trace_segment_typo_circle(self.listeLargages[i][j - 1][0],
                                                   self.listeLargages[i][j - 1][1],
                                                   self.listeLargages[i][j][0],
                                                   self.listeLargages[i][j][1])

        # le graphe courant           
        if len(self.listeLargages[self.nbGraphe - 1]) >= 0:
            for i in range(1, len(self.listeLargages[self.nbGraphe - 1])):
                self.trace_segment_typo_circle(self.listeLargages[self.nbGraphe - 1][i - 1][0],
                                               self.listeLargages[self.nbGraphe - 1][i - 1][1],
                                               self.listeLargages[self.nbGraphe - 1][i][0],
                                               self.listeLargages[self.nbGraphe - 1][i][1])

        # Si on a au moins un point dans notre listeLargages de points alors on trace un segment entre le dernier
        # point placé et le curseur pour prévisualiser le tracé
        if self.isNewGraph:
            if len(self.listeLargages[self.nbGraphe - 1]) >= 1:
                self.trace_segment_typo_circle(self.pos.x(),
                                               self.pos.y(),
                                               self.listeLargages[self.nbGraphe - 1][len(self.listeLargages[self.nbGraphe]) - 1][0],
                                               self.listeLargages[self.nbGraphe - 1][len(self.listeLargages[self.nbGraphe]) - 1][1])

    def trace_segment_typo_circle(self, x1, y1, x2, y2):
        '''
        prend en parametre deux points et le contexte et trace une ligne entre les deux
        avec la typo: cercle
        :param self: self
        :param x1: abscisse du premier point
        :param y1: ordonnée du premier point
        :param x2: abscisse du deuxieme point
        :param y2: ordonnée du deuxieme point
        :return: nothing
        '''
        q = QPainter(self)

        # LARGEUR du segmet dessiné
        largeur = x2 - x1

        # HAUTEUR du segment dessiné
        hauteur = y2 - y1

        # calcul de la longueur du segment en cours
        longueur = math.sqrt(largeur ** 2 + hauteur ** 2)

        # Nombre de symboles dessinés sur le segment en cours
        nb_graphe_rond = int(longueur // 8)

        # Dans cette boucle nous dessinons nbGraphe symboles le long du segment
        for s in range(0, nb_graphe_rond):
            # distance en abscisse entre le symbole dessiné et le point listeLargages[i-1]
            dx = s * (largeur / nb_graphe_rond)

            # distance en ordonnée entre le symbole dessiné et le point listeLargages[i-1]
            dy = s * (hauteur / nb_graphe_rond)

            # on dessine un symbole aux coordonnées x= x de listeLargages[i] + dx -5
            #                                       y= y de listeLargages[i] + dy -5
            # on retire 5 à chaque coordonnées pour centrer le cercle qui
            # est inclu dans un carré de 10 de coté
            q.drawEllipse(x1 + dx - 5, y1 + dy - 5, 10, 10)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
