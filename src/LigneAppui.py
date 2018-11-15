from PyQt5.QtCore import *
from PyQt5.QtGui import *
from src import Graphe


class LigneAppui(Graphe.Graphe):

    def __init__(self):
        super().__init__()

    def draw(self, q):
        p = QPen(Qt.red)

        p.setWidth(5)

        q.setPen(p)

        pixmap = QPixmap("t.png")

        tr = QTransform()

        for j in range(1, len(self.pointList)):
            alpha = 30
            p1 = self.pointList[j-1]
            p2 = self.pointList[j]

            q.drawLine(p1.x, p1.y, p2.x, p2.y)

            tr.rotate(alpha)

            largeur = p2.x - p1.x

            # HAUTEUR du segment dessiné
            hauteur = p2.y - p1.y

            # calcul de la longueur du segment en cours
            longueur = p2.distance(p1)

            nb_graphe_rond = int(longueur // 25)

            pixmap = pixmap.transformed(tr, Qt.SmoothTransformation)

            for s in range(0, nb_graphe_rond):
                # distance en abscisse entre le symbole dessiné et le point listeLargages[i-1]
                dx = s * (largeur / nb_graphe_rond)

                # distance en ordonnée entre le symbole dessiné et le point listeLargages[i-1]
                dy = s * (hauteur / nb_graphe_rond)

                point = QPoint(p1.x + dx, p1.y + dy)

                q.drawPixmap(point, pixmap)
