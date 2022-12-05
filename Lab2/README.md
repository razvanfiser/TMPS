# Structural design patterns

Structural design patterns explain how to assemble objects and classes into larger structures, while keeping these
structures flexible and efficient. They can be listed as follows:
- Adapter pattern
- Bridge pattern
- Composite pattern
- Decorator pattern
- Facade pattern
- Flyweight pattern
- Proxy pattern

## Adapter pattern
We addapt the carriage class to act as a car by implementing the CarriageAdapter class, 
which has an attribute of type Carriage and implements the missing functions
from the Carriage class. In this way, we avoid the inconvenience of making
Car a parent class of Carriage, which is a falsehood, since a carriage cannot
be a car. 

## Bridge pattern
 We want to create both regular and electric cars, which are equipped with either a gps or a camera.
This would normally cause us to create the following subclasses: GPSCar, CameraCar, GPSElectricCar, CameraElectricCar. 
 This is hard to keep track of. We can save lots of lines of code by creating an ExternalDevice interface, since
a GPS and Camera could implement the same functions. Then we pass a device as an argument into the Car constructor.
Then both Car and ElectricCar (which is a child of class Car) can have access to the functions inside the device.

## Composite pattern
We may want to goup certain vechicles together, since they may be stored in different storage units. We might also
 want to apply functions to the whole unit, for example we want to aggregate the estimated price for each vechicle into
the price for the whole unit. For this we want to create a Vechicle interface and make the Car, Carriage and
CompoundVechicle class implement it. Each instance of CompoundVechicle has a list of objects that implement Vechicle,
even other CompoundVechicle objects. In this way we can recursevly call the .estimate_price() function of each object
and calculate the total sum, although the client doesn't see the difference on their side, because the client sees
the same common interface for all classes.
