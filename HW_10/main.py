# Polymorphism
class Car:
    def __init__(self, wheels, mode):
        self.wheels = wheels
        self.mode = mode

    def get_count_of_wheels(self):
        print(f'Car has {self.wheels} wheels')

    def get_mode_of_transport(self):
        print(f'Car mode {self.mode}')

class Bus:
    def __init__(self, wheels, mode):
        self.wheels = wheels
        self.mode = mode

    def get_count_of_wheels(self):
        print(f'Bus has {self.wheels} wheels')

    def get_mode_of_transport(self):
        print(f'Bus mode {self.mode}')

bus = Bus(8, 'Public usage')
car = Car(4, 'Private usage')
list = [car, bus]
for i in list:
    i.get_count_of_wheels()
    i.get_mode_of_transport()

print('*'*40)

class Vehicle:
    def __init__(self, color, wheels):
        self.color = color
        self.wheels = wheels

    def get_desc(self):
        print(f'This vehicle has {self.color} color')

    def get_wheels(self):
        print(f'This vehicle has {self.wheels} wheels')

class Car(Vehicle):
    def __init__(self, color, wheels, kind):
        Vehicle.__init__(self, color, wheels)
        self.kind = kind

    def get_desc(self):
        print(f'This is a {self.color} {self.kind} car')

    def get_wheels(self):
        print(f'This car has {self.wheels} wheels')

class Bus(Vehicle):
    def __init__(self, color, wheels, mode):
        Vehicle.__init__(self, color, wheels)
        self.mode = mode

    def get_desc(self):
        print(f'This {self.color} bus is for {self.mode}')

    def get_wheels(self):
        print(f'This bus has {self.wheels} wheels')

vehicle = Vehicle('red', 2)
car = Car('red', 4, 'sport')
bus = Bus('red', 8, 'public usage')

vehicle.get_desc()
vehicle.get_wheels()
car.get_desc()
car.get_wheels()
bus.get_desc()
bus.get_wheels()

print('*'*40)

# Encapsulation
class Person:
    def __init__(self, a, b):
        self._a = a
        self.__b = b

person = Person(1, 2)
print(person._a)
print(person.__b)

