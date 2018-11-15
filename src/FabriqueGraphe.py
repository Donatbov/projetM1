
from src.Largage import Largage
from src.LigneAppui import LigneAppui


class FabriqueGraphe(object):

    @staticmethod
    def create(type_graphe):
        if type_graphe == 0:
            return Largage()
        if type_graphe == 1:
            return LigneAppui()
