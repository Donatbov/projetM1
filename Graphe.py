
from Largage import Largage
from Triangle import Triangle

class Graphe(object):

    def create(self, type_graphe):
        if type_graphe == 0:
            return LargageHR()
        elif type_graphe == 1:
            return LargageHE()
        elif type_graphe == 2:
            return LargageAR()
        elif type_graphe == 3:
            return LargageAE()
        elif type_graphe == 4:
            return Attaque()
        elif type_graphe == 5:
            return Envisage()
        elif type_graphe == 6:
            return Appui()
        elif type_graphe == 7:
            return AttaqueJE()
        elif type_graphe == 8:
            return AttaqueJ()
        elif type_graphe == 9:
            return AttaquePFE()
        elif type_graphe == 10:
            return AttaquePF()
        elif type_graphe == 11:
            return PEPS()
        elif type_graphe == 12:
            return PPS()
        else:
            return -1



























