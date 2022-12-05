import zope.interface
from Vechicle import Vechicle

@zope.interface.implementer(Vechicle)
class Carriage():
    def __init__(self, n_horses):
        self.n_horses = n_horses

    def estimate_price(self):
        return 1000 * self.n_horses

    def get_n_horses(self):
        return self.n_horses
