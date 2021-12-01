#create a blueprint. Classes which inherit this blueprint must follow certain rules

from abc import ABC, abstractmethod

class BasePlane(ABC):
    @abstractmethod
    def fly(self): # this must be overridden by child classes
        pass

class AirBus(BasePlane):
    def fly(self):
        print("speed >= 200km/h")

#Works because overridden
a = AirBus()
a.fly()

# this won't work
class B2_Spirit(BasePlane):
    def yolo(self):
        print("This not gonna come out. Error")

