import zope.interface
from Vechicle import Vechicle

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


