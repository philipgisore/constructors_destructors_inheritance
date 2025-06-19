# Base class
class Animal:
    def eat(self):
        print("The animal is eating.")
        
    def sleep(self):
        print("The animal is sleeping.")
        
#subclass
class Dog(Animal):
    def bark(self):
        print("The dog is barking.")
        
#creating instances
a = Animal()
a.eat()
a.sleep()

d = Dog()
d.eat()
d.sleep()
d.bark()
  
#Multiple inheritance, a child class inherits from multiple parent classes
class Flyer:
    def fly(self):
        print("Flying...")
        
class Swimmer:
    def swim(self):
        print("Swimming...")
        
class Duck(Flyer, Swimmer):
    pass

duck = Duck()
duck.fly()
duck.swim()

#Multilevel inheritance, a child class inherits from a parent class which inherits from another parent class
class Vehicle:
    def move(self):
        print("Moving...")
        
class Car(Vehicle):
    pass

class ElectricCar(Car):
    def charge(self):
        print("Charging...")
        
tesla = ElectricCar()
tesla.move()
tesla.charge()
  