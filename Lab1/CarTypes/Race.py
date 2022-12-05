from CarType import CarType


# normal car class (prototype method)
class Race(CarType):
    def __init__(self):
        super().__init__()
        self.type = "Race"
