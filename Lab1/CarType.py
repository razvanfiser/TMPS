import copy
from abc import ABCMeta


# prototype method. Contains a function named "clone" which makes an exact copy of the object, and functions set_id
# and get_id allowing the existence of different car types.
class CarType(metaclass=ABCMeta):
    def __init__(self):
        self.id = None
        self.type = None
        self.name = None
        self.driver = None

    def set_name(self, name):
        self.name = name

    def get_name(self):
        return self.name

    def set_driver(self, driver):
        self.driver = driver

    def get_driver(self):
        return self.driver

    def get_type(self):
        return self.type

    def get_id(self):
        return self.id

    def set_id(self, sid):
        self.id = sid

    def clone(self):
        return copy.copy(self)
    