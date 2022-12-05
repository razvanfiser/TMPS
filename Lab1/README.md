# Creational design patterns

Creational design patterns are concerned with the way of creating 
objects. These design patterns are used when a decision must be made 
at the time of instantiation of a class (i.e. creating an object of 
a class). In this project were implemented the following design patterns:
- Singleton pattern
- Builder pattern
- Factory method
- Abstract factory method
- Prototype pattern

## The Singleton Pattern
Singleton is a creational design pattern that lets you ensure that 
a class has only one instance, while providing a global access 
point to this instance.
<br>
The class CarShop follows this principle. In main.py 2 objects of type
CarShop were created, but updating the address of one of them would 
cause a change in the other object too.

## The Builder pattern
Builder pattern aims to “Separate the construction of a complex 
object from its representation so that the same construction 
process can create different representations.”
The class Car follows this pattern and for creating an object of type
car, it is needed to add all the details such as name,color, max_speed
step by step.

## The Factory method
Factory Method is a creational design pattern used to create concrete 
implementations of a common interface.
In this project this design pattern allows us to convert max_speed to
different units. The logic behind conversion can be found inside the 
classes contained in the folder UnitConversion.
The default unit is mph (miles per hour).

## The Abstract factory method
Abstract Factory is a creational design pattern that lets you produce 
families of related objects without specifying their concrete classes.
The 2 families present in this code are Collectible and Non-Collectible
cars. The cars are divided into classes using the Car() class, but it
receives a class parameter at initialization which contains the 
the information whether the car is collectible or not.

## The Prototype pattern
Prototype is a creational design pattern that lets you copy existing 
objects without making your code dependent on their classes.
In this project the classes respecting The Prototype pattern are: 
CarType, CarTypeCache, Motorcycle, NormalCar and Race. The developer
can choose a type of car by specifying the ip. It also allows copying 
objects. In the example from main.py, at step 5, tou can see that a car
whose owner is Ion was created then we copied the same car by using the 
clone() function to which the first created object had access, and then 
changes only the driver name in a usual manner.