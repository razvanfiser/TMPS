from ExternalDevice import ExternalDevice
import zope.interface

@zope.interface.implementer(ExternalDevice)
class GPS:
    def __init__(self, is_functional):
        self.is_func = is_functional

    def is_functional(self):
        return self.is_func

    def make_sound(self):
        print("Bleep bloop!")
