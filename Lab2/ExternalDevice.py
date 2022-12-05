import zope.interface

class ExternalDevice(zope.interface.Interface):
    def __init__(self, x):
        pass
    def is_functional(self):
        pass
    def make_sound(self):
        pass