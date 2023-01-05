#Behavioral Design Patterns
&ensp; &ensp; In software engineering, behavioral design patterns have the purpose of identifying common communication patterns between different software entities. By doing so, these patterns increase flexibility in carrying out this communication.

&ensp; &ensp; Some examples from this category of design patterns are :

   * Chain of Responsibility
   * Command
   * Interpreter
   * Iterator
   * Mediator
   * Observer
   * Strategy
   * Memento
   
## Memento Pattern
Memento is a behavioral design pattern that lets you save and restore the previous state of an object without 
revealing the details of its implementation. Memento pattern uses three actor classes. Memento contains state of an object to be restored. Originator creates and stores states in Memento objects and Caretaker object is responsible to restore object state from Memento.
We have created classes `Memento`, `Car` (which will act as
the Originator class) and `CareTaker`.
```py
class Memento:
    def __init__(self, mileage, horsepower, device):
        self.mileage = mileage
        self.horsepower = horsepower
        self.device = device

    def get_states(self):
        return (self.mileage, self.horsepower, self.device)
```
`Memento` implements the `get_states` function which will be used to update the
states of the `Car` Originator class.
```py
class CareTaker:
    def __init__(self):
        self.memento_list = []
        self.index = 0
    def add(self, state):
        self.memento_list.append(copy.copy(state))

    def undo(self):
        self.index -= 1
        if (self.index < - len(self.memento_list)):
            print("Cannot undo anymore!")
            self.index += 1
            return self.memento_list[self.index]
        return self.memento_list[self.index]
```
The `Car` (Originator) class only interacts with the `Memento` class and 
we use the `CareTaker` class to store a list of `Memento` with different states
so we can acces them and therefore restore the Originator's states to some previous
values. Below is the implementation in the `main` class:
```py
test_car = Car(gps, 1000, 140)
care_taker = CareTaker()
care_taker.add(test_car.save_states_to_memento())

test_car.drive(100) #drive for 100 miles
care_taker.add(test_car.save_states_to_memento())


test_car.drive(110) #drive for 110 miles
care_taker.add(test_car.save_states_to_memento())

test_car.drive(1488) #drive for 1488 miles
care_taker.add(test_car.save_states_to_memento())

for i in range(6):
    test_car.get_states_from_memento(care_taker.undo())
    print("Undo no. " + str(i + 1) + ":" + str(test_car.mileage))
```

As you can see in `main` we only instantiate the `Car` and `Caretaker` class.
We use the latter to implement an "undo" functionality to get back to a previous
state of a car.