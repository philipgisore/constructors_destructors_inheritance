#polymorphism means that different objects can respond to the same method or function call in different ways
#implementing Polymorphism and Method overiding
class Animal:
    def make_sound(self):
        print("Generic animal sound")
        
class Dog(Animal):
    def make_sound(self):
        print("Woof!")
        
animals = [Dog(), Animal()]
for animal in animals:
    animal.make_sound()
    
#polymorphism with duck typing
class Duck:
    def sound(self):
        return "Quack"
        
class Dog:
    def sound(self):
        return "Woof"
    
class Cat:
    def sound(self):
        return "Meows"
    
#Function that uses duck typing
def animal_sound(animal):
    print(animal.sound())
   
#Different objects passed to the same function 
duck = Duck()
dog = Dog()
cat = Cat()

animal_sound(duck)
animal_sound(dog)
animal_sound(cat)

