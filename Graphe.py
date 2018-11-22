import math


class Graphe(object):
    def __init__(self):
        self.pointList = []
        self.point_curseur = None

    @staticmethod
    def angle_ligne_rad(p1, p2):
        """
        retourne l'angle que forme le segment[p1 p2] par rapport à l'horizontale en radian
        :param p1: premier point
        :param p2: deuxieme poit
        :return: l'angle que forme le segment[p1 p2] par rapport à l'horizontale en radian
        """
        teta = 0
        if p1.x == p2.x:  # si la ligne est verticale
            if p1.y <= p2.y:
                teta = math.pi / 2
            else:
                teta = -math.pi / 2
        elif p1.x > p2.x:  # si on est sur la partie droite du cercle trigonométrique
            teta = math.atan((-p2.y + p1.y) / (
                        p2.x - p1.x))  # on remarquera ici l'inversion de p2.y et p1.y due au systeme de coordonées inversé en y
        else:  # si on est sur la partie gauche du cercle trigonométrique
            teta = math.atan(
                (-p2.y + p1.y) / (p2.x - p1.x)) + math.pi  # on ajoute pi par rapport au calcul précédent
        return teta
