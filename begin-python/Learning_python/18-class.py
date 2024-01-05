####Jus like append,remove etc in list we can make class 
#https://docs.python.org/3/tutorial/classes.html#classes
#Class start with a camel case
#self is instance of class
#Methods are functions inside a class
#Class variable or class attribute can be accessed as classname.attribute (Circle.pi)
#def __int__ (constructor of the class)
#attributes can be accessed as self.attribute

class Vehicle:
    """
    Vehicle models a vehicle w/ tires and an engine
    """

    def __init__(self, engine, tires):
        self.engine = engine
        self.tires = tires

    #Custom Method
    def description(self):
        print(f"A vehicle with an {self.engine} engine, and {self.tires} tires")

##create object
>>> civic = Vehicle('4-cylinder', ['front-driver', 'front-passenger', 'rear-driver', 'rear-passenger'])
>>> civic.engine
'4-cylinder'

>>> civic.tires
['front-driver', 'front-passenger', 'rear-driver', 'rear-passenger']

>>> civic.description
<bound method Vehicle.description of <__main__.Vehicle object at 0x7fb5f3fbbda0>>

>>> civic.description()
A vehicle with a 4-cylinder engine, and ['front-driver', 'front-passenger', 'rear-driver', 'rear-passenger'] tires


