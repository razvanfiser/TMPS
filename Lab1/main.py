from CarShop import CarShop
from Car import Car
from Collectibles.CollectibleCar import CollectibleCar
from Collectibles.NonCollectibleCar import NonCollectibleCar
from UnitConversion.MilesPerHour import MilesPerHour
from UnitConversion.FootPerSecond import FootPerSecond
from UnitConversion.MetersPerSecond import MetersPerSecond
from CarTypeCache import CarTypeCache

if __name__ == '__main__':

    # STEP 1 - creation of a singleton class
    shop = CarShop()
    new_shop = CarShop()
    new_shop.address = "Dacia 22"  # changing the address of new_shop would change the address of shop too.
    print()

    # STEP 2 - creating an object following the builder pattern
    car = Car()
    # using the builder pattern to add data about a car object.
    car.set_name("Ford")
    car.set_color("Red")
    car.set_max_speed(120)
    car.set_address(shop)
    car.display()
    print()

    # STEP 3 - creating an object following the factory method
    # using the NonCollectibleCar class as an argument for initializing the function Car

    car = Car(NonCollectibleCar)
    # NonCollectibleCar is a class containing the value of the car (abstract factory pattern)

    car.set_name("Opel")
    car.set_color("Dark Blue")
    car.set_max_speed(110)
    car.set_address(shop)
    car.display()

    # printing the value
    car.show_value()
    print()

    # STEP 4 - Abstract Factory

    # function contains abstract factory classes  for unit conversion
    def Factory(unit="mph"):
        """Factory Method"""
        localizers = {
            "mps": MetersPerSecond,
            "fps": FootPerSecond,
            "mph": MilesPerHour,
        }

        return localizers[unit]()


    # converting max speed unit by using abstract factory method
    unit = Factory("mps")
    car.set_max_speed(unit.localize(car.max_speed))
    car.display()
    print()


    # step 5 - Prototype Pattern
    # adding a simple Opel car whose driver is Ion
    CarTypeCache.load()  #
    simple_car = CarTypeCache.get_car("2")
    simple_car.set_name(car.name)
    simple_car.set_driver("Ion")
    print(simple_car.get_type())
    print(simple_car.get_name())
    print(simple_car.get_driver())

    print()

    #  making a copy of the previous car. Same characteristics but a different driver
    another_car = simple_car.clone()
    another_car.set_driver("Ioana")
    print(another_car.get_type())
    print(another_car.get_name())
    print(another_car.get_driver())
