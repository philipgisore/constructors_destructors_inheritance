class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        print(f"{self.name} has been created, age {self.age}.")

    def __del__(self):
        print(f"{self.name} has been deleted. Goodbye!")

        
p1 = Person("Alice", 25)
p2 = Person("Bob", 30)

#Deleting one manually
