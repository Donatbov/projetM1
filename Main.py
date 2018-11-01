import sys
import math
from Point import Point
from PyQt5.QtWidgets import QWidget, QApplication, QGridLayout, QLabel, QPushButton
from PyQt5.QtCore import Qt, QPoint
from PyQt5.QtGui import QMouseEvent, QPainter, QPixmap, QTransform, QPen


class Example(QWidget):

    def __init__(self):
        super().__init__()

        x = 0
        y = 0
        self.nbGraphe = 0  # c'est le nombre de graphes
        self.isNewGraph = False  # sert à determiner si on commence un nouveau graphe ou non
        self.listeLargages = [[]]  # liste contenant les graphes des largages
        self.text = "x: {0},  y: {1}".format(x, y)  # le texte qui va aller dans le label
        self.labelPositionCurseur = QLabel(self.text, self)  # le label dans lequel on affiche le texte
        self.pos = None  # position du curseur (contient un champ x et un champ y)
        self.clearButton = QPushButton('Clear', self)

        self.initUI()

    def initUI(self):
        grid = QGridLayout()  # notre espace de jeu
        grid.addWidget(self.labelPositionCurseur, 0, 0, Qt.AlignTop)

        grid.addWidget(self.clearButton)
        self.setMouseTracking(True)
        self.setLayout(grid)
        self.setGeometry(200, 100, 1000, 600)  # taille par défaut de la fenetre
        self.setWindowTitle('Interface')
        self.show()

    # fonction qui réagit à l'évènement : la souris bouge
    def mouseMoveEvent(self, e):
        self.pos = e.pos()
        if self.isNewGraph:
            x = e.x()
            y = e.y()
            text = "x: {0},  y: {1}".format(e.x(), e.y())
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
            b = Point(event.x(), event.y())
            self.listeLargages[self.nbGraphe - 1].append(b)
        elif event.button() == Qt.RightButton:
            self.isNewGraph = False
            text = "fini"
            self.labelPositionCurseur.setText(text)
            self.update()  # sert a invoquer paintEvent pour effacer le segment en cours
    '''
    def keyPressEvent(self, QKeyEvent):
        if QKeyEvent == clearButton:
            self.listeLargages = [[]]
            self.nbGraphe = 0'''

    # fonction qui réagit à l'évènement : raffraichisssement de la fenetre
    def paintEvent(self, event):
        # pour dessiner tous les graphes precedents
        if self.nbGraphe >= 2:
            for i in range(0, self.nbGraphe - 1):
                for j in range(1, len(self.listeLargages[i])):
                    self.trace_segment_typo_triangle(self.listeLargages[i][j - 1],
                                                     self.listeLargages[i][j])

        # le graphe courant
        if len(self.listeLargages[self.nbGraphe - 1]) >= 0:
            for i in range(1, len(self.listeLargages[self.nbGraphe - 1])):
                self.trace_segment_typo_triangle(self.listeLargages[self.nbGraphe - 1][i - 1],
                                                 self.listeLargages[self.nbGraphe - 1][i])

        # Si on a au moins un point dans notre listeLargages de points alors on trace un segment entre le dernier
        # point placé et le curseur pour prévisualiser le tracé
        if self.isNewGraph:
            if len(self.listeLargages[self.nbGraphe - 1]) >= 1:
                ptmp = Point(self.pos.x(), self.pos.y())
                self.trace_segment_typo_triangle(self.listeLargages[self.nbGraphe - 1][len(self.listeLargages[self.nbGraphe]) - 1],
                                                 ptmp)

    def trace_segment_typo_circle(self, p1, p2):
        '''
        prend en parametre deux points et le contexte et trace une ligne entre les deux
        avec la typo: cercle
        :param self: self
        :param p1: coordonées du premier point
        :param p2: coordonées du deuxieme point
        :return: nothing
        '''
        q = QPainter(self)

        # LARGEUR du segmet dessiné
        largeur = p2.x - p1.x

        # HAUTEUR du segment dessiné
        hauteur = p2.y - p1.y

        # calcul de la longueur du segment en cours
        longueur = p2.distance(p1)

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
            q.drawEllipse(p1.x + dx - 5, p1.y + dy - 5, 10, 10)

    def trace_segment_typo_triangle(self, p1, p2):
        '''
        prend en parametre deux points et le contexte et trace une ligne entre les deux
        avec la typo: triangle (avec l'image t.png)
        :param self: self
        :param p1: coordonées du premier point
        :param p2: coordonées du deuxieme point
        :return: nothing
        '''
        q = QPainter(self)

        # LARGEUR du segmet dessiné
        largeur = p2.x - p1.x

        # HAUTEUR du segment dessiné
        hauteur = p2.y - p1.y

        # calcul de la longueur du segment en cours
        longueur = p2.distance(p1)

        # Nombre de symboles dessinés sur le segment en cours
        nb_pixmap = int(longueur // 25)

        p = QPen(Qt.red)    # On cree un objet painter
        p.setWidth(5)

        q.setPen(p)

        q.drawLine(p1.x, p1.y, p2.x, p2.y)

        # on determine l'angle de notre ligne par rapport à l'horizontale
        alpha = angle_ligne_rad(p1, p2)  # retourne l'angle de notre ligne en radian

        pixmap = QPixmap("t.png")

        # on déclare une transformation
        tr = QTransform()
        tr.rotateRadians(-alpha)    # rotate tourne le png dans le sens non trigo autour du pixel (0,0)
        # tr.translate(pixmap.width()/2, pixmap.height()/2) # not working

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
            point = QPoint(p1.x + dx - pixmap.width()/2, p1.y + dy - pixmap.height()/2)
            q.drawPixmap(point, pixmap)
        # on dessine le dernier pixmap
        point = QPoint(p2.x - pixmap.width() / 2, p2.y - pixmap.height() / 2)
        q.drawPixmap(point, pixmap)

def angle_ligne_rad(p1, p2):
    '''
    retourne l'angle que forme le segment[p1 p2] par rapport à l'horizontale en radian
    :param p1: premier point
    :param p2: deuxieme poit
    :return:
    '''
    teta = 0
    if p1.x == p2.x:    # si la ligne est verticale
        if p1.y <= p2.y:
            teta = math.pi/2
        else:
            teta = -math.pi/2
    elif p1.x > p2.x:   # si on est sur la partie droite du cercle trigonométrique
        teta = math.atan((-p2.y+p1.y)/(p2.x-p1.x))  # on remarquera ici l'inversion de p2.y et p1.y due au systeme de coordonées inversé en y
    else:   # si on est sur la partie gauche du cercle trigonométrique
        teta = math.atan((-p2.y + p1.y) / (p2.x - p1.x)) + math.pi  # on ajoute pi par rapport au calcul précédent
    return teta


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
