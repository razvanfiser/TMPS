class Memento:
    def __init__(self, mileage, horsepower, device):
        self.mileage = mileage
        self.horsepower = horsepower
        self.device = device

    def get_states(self):
        return (self.mileage, self.horsepower, self.device)

    # self.mileage = mileage
    # self.horsepower = horsepower
    # self.device = external_device