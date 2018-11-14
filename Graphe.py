
from Largage import Largage
from Triangle import Triangle

class Graphe(object):

    def create(self, type_graphe):
        if type_graphe == 0:
            return Largage()
        elif type_graphe == 1:
            return Triangle()
        else:
            return -1



























