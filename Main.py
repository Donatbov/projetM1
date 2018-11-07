import sys
import math
# sys.path.append("/Users/leizhang/Desktop/projet801/Point.py")
# from Point import Point
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *


class Point(object):
    def __init__(self,xParam = 0.0,yParam = 0.0):
        self.x = xParam
        self.y = yParam

    def distance (self,pt):
        xDiff = self.x - pt.x
        yDiff = self.y - pt.y
        return math.sqrt(xDiff ** 2 + yDiff ** 2)


class Example(QWidget):

    def __init__(self):
        super().__init__()

        self.listeGraphe = [ [[]], [[]], [[]], [[]], [[]] ]
        self.isNewGraph = False  # sert à determiner si on commence un nouveau graphe ou non

        x = 0
        y = 0
       
        self.text = "x: {0},  y: {1}".format(x, y)  # le texte qui va aller dans le label
        self.labelPositionCurseur = QLabel(self.text, self)    # le label dans lequel on affiche le texte
        self.pos = None     # position du curseur (contient un champ x et un champ y)
        self.typeGraphe = 0

        self.choice = QComboBox()
        self.choice.addItems(["n", "v", "b", "r"])
        self.largageButton = QPushButton('Largage', self)
        self.lineWithFlashButton = QPushButton('LineWithFlash', self)
        self.lineButton = QPushButton('Line', self)
        self.lineTriangleButton = QPushButton('LineTriangle', self)
        self.curseurButton = QPushButton('curseur', self)

        
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Santoline')
        self.setGeometry(200, 100, 1000, 600)   # taille par défautt de la fenetre
        grid = QGridLayout()    # notre espace de jeu
        self.setLayout(grid)

        grid.addWidget(self.labelPositionCurseur, 0, 0, Qt.AlignTop)
        grid.addWidget(self.choice, 0, 0, Qt.AlignBottom)
        grid.addWidget(self.largageButton, 0, 1, Qt.AlignBottom)
        grid.addWidget(self.lineWithFlashButton, 0, 2, Qt.AlignBottom)
        grid.addWidget(self.lineButton, 0, 3, Qt.AlignBottom)
        grid.addWidget(self.lineTriangleButton, 0, 4, Qt.AlignBottom)
        grid.addWidget(self.curseurButton, 0, 5, Qt.AlignBottom)

        self.largageButton.clicked[bool].connect(self.set_type_largage)
        self.lineWithFlashButton.clicked[bool].connect(self.set_type_cercle)
        self.lineButton.clicked[bool].connect(self.set_type_line)
        self.lineTriangleButton.clicked[bool].connect(self.set_type_line_triangle)
        self.curseurButton.clicked[bool].connect(self.set_type_null)

        self.setMouseTracking(True)
        self.show()


    def createHorizontalLayout(self):
        self.horizontalGroupBox = QGroupBox("What is your favorite color?")

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
        if event.button() == Qt.LeftButton and self.typeGraphe != -1:
            if not self.isNewGraph:
                self.listeGraphe[self.typeGraphe].append([])

            self.isNewGraph = True
            text = "click"
            self.labelPositionCurseur.setText(text)
            b = Point(event.x(),event.y())
            self.listeGraphe[self.typeGraphe][len(self.listeGraphe[self.typeGraphe]) - 1].append(b)

        elif event.button() == Qt.RightButton:
            self.isNewGraph = False
            text = "fini"
            self.labelPositionCurseur.setText(text)
            self.update()  # sert a invoquer paintEvent pour effacer le segment en cours


    def angle_ligne_rad(self, p1, p2):
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


    # fonction qui réagit à l'évènement : raffraichisssement de la fenetre
    def paintEvent(self, event):
        for s in range(len(self.listeGraphe)):
            for i in range(0, len(self.listeGraphe[s])):
                for j in range(1, len(self.listeGraphe[s][i])):
                    self.trace_segment( self.listeGraphe[s][i][j - 1], self.listeGraphe[s][i][j], s)

        # le graphe courant
        s  = self.typeGraphe     # pour simplifier la vie
        lg = self.listeGraphe[s] # liste de graphe de meme type
        ls = lg[len(lg) - 1]     # le derinier graphe de ce type de graphe
        for i in range(1, len(ls)):
            self.trace_segment( ls[i-1], ls[i], s)

        # Si on a au moins un point dans notre listeLargages de points alors on trace un segment entre le dernier
        # point placé et le curseur pour prévisualiser le tracé
        if self.isNewGraph:
            p = ls[len(ls) - 1] # le dernier point du dernier graphe de ce type de graphe
            ptmp = Point(self.pos.x(),self.pos.y()) # le curseur
            self.trace_segment(p, ptmp, s)

    
    def trace_segment(self, p1, p2, type):
        q = QPainter(self)
        largeur = p2.x  - p1.x
        hauteur = p2.y - p1.y
        longueur = p2.distance(p1)

        if type == 0:
            nb_graphe_rond = int(longueur // 8)
            for s in range(0, nb_graphe_rond):
                dx = s * (largeur / nb_graphe_rond)
                dy = s * (hauteur / nb_graphe_rond)
                q.drawEllipse(p1.x + dx - 5, p1.y + dy - 5, 10, 10)

        elif type == 1:
            q.drawLine(p1.x, p1.y, p2.x, p2.y)
            if hauteur == 0:
                sita = 0
            else:
                sita = math.atan(largeur/hauteur)
            sita = abs(sita)
            nb_graphe_rond = int(longueur // 20)
            for s in range(0, nb_graphe_rond):
                dx = s * (largeur / nb_graphe_rond)
                dy = s * (hauteur / nb_graphe_rond)
                x1 = p1.x + dx
                y1 = p1.y + dy
                if largeur > 0 and hauteur < 0:
                    q.drawLine(x1, y1, x1 + 20 * math.cos(sita), y1 + 20 * math.sin(sita))
                elif largeur <= 0 and hauteur < 0:
                    q.drawLine(x1, y1, x1 + 20 * math.cos(sita), y1 - 20 * math.sin(sita))
                elif largeur < 0 and hauteur > 0:
                    q.drawLine(x1, y1, x1 - 20 * math.cos(sita), y1 - 20 * math.sin(sita))
                elif largeur >= 0 and hauteur > 0:
                    q.drawLine(x1, y1, x1 - 20 * math.cos(sita), y1 + 20 * math.sin(sita))

        elif type == 2:
            q.drawLine(p1.x, p1.y, p2.x, p2.y)

        elif type == 3:
            nb_pixmap = int(longueur // 25)
            p = QPen(Qt.red)    # On cree un objet painter
            p.setWidth(5)
            q.setPen(p)
            q.drawLine(p1.x, p1.y, p2.x, p2.y)
            # on determine l'angle de notre ligne par rapport à l'horizontale
            alpha = self.angle_ligne_rad(p1, p2)  # retourne l'angle de notre ligne en radian
            pixmap = QPixmap("t.png")
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


    


    def set_type_largage(self, x):
        self.typeGraphe = 0
        self.isNewGraph = False
        print("tpye graphe = " + str(self.typeGraphe))

    def set_type_cercle(self, x):
        self.typeGraphe = 1
        self.isNewGraph = False
        print("tpye graphe = " + str(self.typeGraphe))

    def set_type_line(self, x):
        self.typeGraphe = 2
        self.isNewGraph = False
        print("tpye graphe = " + str(self.typeGraphe))
    
    def set_type_line_triangle(self, x):
        self.typeGraphe = 3
        self.isNewGraph = False
        print("tpye graphe = " + str(self.typeGraphe))
    
    def set_type_null(self, x):
        self.typeGraphe = -1
        self.isNewGraph = False
        print("tpye graphe = " + str(self.typeGraphe))

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())

