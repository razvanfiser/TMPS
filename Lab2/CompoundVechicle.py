import zope.interface
from Vechicle import Vechicle

@zope.interface.implementer(Vechicle)
class CompoundVechicle:
    def __init__(self):
        self.vechicle_list = []

    def add(self, vechicle):
        self.vechicle_list.append(vechicle)

    def remove(self, index):
        self.vechicle_list.pop(index)

    def estimate_price(self):
        return sum([v.estimate_price() for v in self.vechicle_list])
