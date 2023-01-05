import copy

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