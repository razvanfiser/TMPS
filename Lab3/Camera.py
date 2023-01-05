import zope.interface
from ExternalDevice import ExternalDevice


@zope.interface.implementer(ExternalDevice)
class Camera:
    def __init__(self, is_functional):
        self.is_func = is_functional

    def is_functional(self):
        return self.is_func

    def make_sound(self):
        print("You are on camera officer!")
