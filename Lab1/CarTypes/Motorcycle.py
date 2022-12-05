from CarType import CarType

# normal car class (prototype method)
class Motorcycle(CarType):
    def __init__(self):
        super().__init__()
        self.type = "Motorcycle"