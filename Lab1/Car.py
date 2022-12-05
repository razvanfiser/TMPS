# resprects builder pattern and abstract factory method
class Car:
    def __init__(self, collectible_factory=None):
        self.name = None
        self.color = None
        self.max_speed = None
        self.address = None

        # abstract factory. age_factcory is a class received as a parameter which contains the value of a car (collectible or not)
        self.collectible_factory = collectible_factory

    def show_value(self):
        # creates and shows the value of a car using the abstract factory
        value = self.collectible_factory()
        print(f'The car is {value}')

    # builder pattern
    # there are specific functions created for adding new components to our object (name, color, max speed, address)
    def set_name(self, name):
        self.name = name

    def set_color(self, color):
        self.color = color

    def set_max_speed(self, max_speed):
        self.max_speed = max_speed

    def set_address(self, car_shop):
        self.address = car_shop.address

    def display(self):
        print('Found at: ', self.address)
        print('Name: ', self.name)
        print("Color:", self.color)
        print("Max speed:", self.max_speed)
