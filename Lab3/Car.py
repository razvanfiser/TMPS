import zope.interface
from Vechicle import Vechicle
from Memento import Memento
from copy import copy

@zope.interface.implementer(Vechicle)
class Car:
    def __init__(self, external_device, mileage, horsepower):
        self.mileage = mileage
        self.horsepower = horsepower
        self.device = external_device

    def estimate_price(self):
        return (-0.001*self.mileage + 100*self.horsepower) + int(self.device.is_functional()) * 100
    def get_mileage(self):
        return self.mileage

    def get_horsepower(self):
        return self.horsepower

    def est_max_velocity(self):
        return 20 * pow(self.horsepower, 1/3)

    def drive(self, for_x_miles):
        self.mileage += for_x_miles

    def save_states_to_memento(self):
        # we pass a copy of each field to the Memento object because of the way memory allocation works in python
        # if we hadnt passed a copy, any changes to the fields would carry out through to the Memento object
        return Memento(copy(self.mileage), copy(self.horsepower), copy(self.device))

    def get_states_from_memento(self, memento):
        self.mileage, self.horsepower, self.device = memento.get_states()


