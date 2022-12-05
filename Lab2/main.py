from Car import Car
from Carriage import Carriage
from CarriageAdapter import CarriageAdapter
from ExternalDevice import *
from GPS import *
from Camera import Camera
from ElectricCar import ElectricCar
from CompoundVechicle import CompoundVechicle

camera = Camera(True)
gps = GPS(False)

slow_car = Car(Camera(True), 1000, 180)
fast_car = Car(GPS(True), 10, 400)

small_carriage = Carriage(2)
big_carriage = Carriage(4)




# Adapter pattern
# We addapt the carriage class to act as a car by implementing the CarriageAdapter class,
# which has an attribute of type Carriage and implements the missing

try:
    print((small_carriage.est_max_velocity(), big_carriage.est_max_velocity()))
except AttributeError as err:
    print(f"Attribute Error: {err}")

adapt_small_carriage = CarriageAdapter(small_carriage)
adapt_big_carriage = CarriageAdapter(big_carriage)

print((adapt_small_carriage.est_max_velocity(), adapt_big_carriage.est_max_velocity()))

# Bridge pattern
# We want to create both regular and electric cars, which are equipped with either a gps or a camera.
# This would normally cause us to create the following subclasses: GPSCar, CameraCar, GPSElectricCar, CameraElectricCar.
# This is hard to keep track of. We can save lots of lines of code by creating an ExternalDevice interface, since
# a GPS and Camera could implement the same functions. Then we pass a device as an argument into the Car constructor.
# Then both Car and ElectricCar (which is a child of class Car) can have access to the functions inside the device.

gps_car = Car(gps, 100, 300)
print(gps_car.estimate_price())
gps_electric_car = ElectricCar(gps, 100, 300, 5000)
print(gps_electric_car.how_much_battery_left(10))

# Composite pattern
# We may want to goup certain vechicles together, since they may be stored in different storage units. We might also
# want to apply functions to the whole unit, for example we want to aggregate the estimated price for each vechicle into
# the price for the whole unit. For this we want to create a Vechicle interface and make the Car, Carriage and
# CompoundVechicle class implement it. Each instance of CompoundVechicle has a list of objects that implement Vechicle,
# even other CompoundVechicle objects. In this way we can recursevly call the .estimate_price() function of each object
# and calculate the total sum, although the client doesn't see the difference on their side, because the client sees
# the same common interface for all classes.

group1 = CompoundVechicle()
group2 = CompoundVechicle()
v_list1 = [Car(gps, 100, 300), ElectricCar(camera, 10000, 280, 8000), Carriage(5)]
v_list2 = [Carriage(2), Car(gps, 4000, 300)]

for item in v_list1:
    group1.add(item)

for item in v_list2:
    group2.add(item)

group2.add(group1)

print("Group 2 price:")
print(group2.estimate_price())