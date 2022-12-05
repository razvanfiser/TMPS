from Car import Car

class CarriageAdapter(Car):
    def __init__(self, carriage):
        self.carriage = carriage

    def get_horsepower(self):
        return 15 * self.carriage.n_horses

    def est_max_velocity(self):
        return 20 * pow(15 * self.carriage.n_horses, 1/3)
