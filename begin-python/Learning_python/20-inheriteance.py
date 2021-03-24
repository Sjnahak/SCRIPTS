class Mammal:
    def walk(self):
        print("walk")

###Inheriting mammal class
class Dog(Mammal):
    def bark(self):
        print("Bark")

class Cat(Mammal):
    pass

dog1 = Dog()
dog1.walk()
dog1.bark()
