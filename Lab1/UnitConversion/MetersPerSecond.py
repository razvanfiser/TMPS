# factory method for conversion to mps
class MetersPerSecond:
    def __init__(self):
        pass
    
    def localize(self, value):
        return value / 2.237
