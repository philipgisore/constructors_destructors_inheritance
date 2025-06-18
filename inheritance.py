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
    