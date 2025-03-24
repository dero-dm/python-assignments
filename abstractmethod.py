from abc import ABC , abstractmethod
class vehicle(ABC):
    def start_engine(self):
        pass
class car(vehicle):
    def start_engine(self):
        return "car has started!"
my_vehicle = vehicle()
#print(my_vehicle.start_engine())  
my_car = car()
print(my_car.start_engine())
