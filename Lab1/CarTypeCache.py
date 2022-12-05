from CarTypes.NormalCar import NormalCar
from CarTypes.Race import Race
from CarTypes.Motorcycle import Motorcycle


# implements prototype method
# function load to find the type of a car by id
class CarTypeCache:
    # cache to store useful information
    cache = {}

    @staticmethod
    def get_car(sid):
        car = CarTypeCache.cache.get(sid, None)
        return car.clone()

    @staticmethod
    def load():
        race_car = Race()
        race_car.set_id("1")
        CarTypeCache.cache[race_car.get_id()] = race_car

        normal_car = NormalCar()
        normal_car.set_id("2")
        CarTypeCache.cache[normal_car.get_id()] = normal_car

        motorcycle = Motorcycle()
        motorcycle.set_id("3")
        CarTypeCache.cache[motorcycle.get_id()] = motorcycle