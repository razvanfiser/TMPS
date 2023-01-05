from Car import Car

class ElectricCar(Car):
    def __init__(self, external_device, mileage, horsepower, battery_capacity):
        super().__init__(external_device, mileage, horsepower)
        self.battery_capacity = battery_capacity

    def how_much_battery_left(self, time):
        return self.battery_capacity - self.horsepower * 0.3 * time - int(self.device.is_functional()) * 0.1 * time

