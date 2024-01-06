Custom Constructors, Class Methods, and Decorators:

Documentation for This Video
Classes (https://docs.python.org/3/tutorial/classes.html#classes)
Class Methods (https://docs.python.org/3/library/functions.html#classmethod)


Custom Class Constructors

Unlike other languages like Java, Python doesn't provide a way for us to create multiple constructor methods. Instead, we get a single constructor method that we can customize, the __init__ method. We've already customized this for our Vehicle class. This method has a default implementation that takes no arguments, so by defining this in our class, we've created a custom constructor.


Using @classmethod to Create Convenience Constructor Methods

Although creating multiple different constructors isn't a feature of Python, it doesn't mean we can't do something similar. If we want another way to construct a Vehicle object with some preset values, we can create convenience methods using what is known as a class method. A class method is a function attached to the class itself, not an instance of the class, and it has access to any class-level attributes. To create a class method, we need to use what is known as a decorator. Decorators are functions or classes that we use to add additional functionality to a function by prefixing the decorator's name with an at-sign (@) and putting it on the line above our function or method definition. This sounds confusing, but remember back to our look at higher-order functions. A decorator takes a function and returns another modified function in its place. For the purposes of the PCAP, we only need to know how to use one specific decorator so that we can add class methods to our classes: the @classmethod decorator. Let's add a method to our Vehicle class that will allow us to create a bicycle (which has two wheels, and no engine).

~/python_objects/vehicle.py


class Vehicle:
    """
    Vehicle models a vehicle w/ tires and an engine
    """
    default_tire = 'tire'

    def __init__(self, engine, tires):
        self.engine = engine
        self.tires = tires

    @classmethod
    def bicycle(cls, tires=None):
        if not tires:
            tires = [cls.default_tire, cls.default_tire]
        return cls(None, tires)

    def description(self):
        print(f"A vehicle with an {self.engine} engine, and {self.tires} tires")


Notice we added a class-level variable called default_tire. This variable is set on the class itself and will also be available to instances of the class. By decorating the bicycle as a @classmethod, we're able to call Vehicle.bicycle(), and the class itself will be passed in as the implicit cls argument (this name is a convention, not a required name). Because the class itself (Vehicle) is passed into the method as the cls variable, that means when we call cls(), it is equivalent to doing Vehicle() and will invoke the __init__ method. It's beneficial to use the cls variable instead of the class name, because if we ever change the name of the class, then we won't need to modify this function. If no argument is passed in for the tires parameter, then we'll create a default list containing the value of the default_tire class attribute two times. Let's load this file into the REPL and see if it works:


$ python3.7 -i vehicle.py
>>> bike = Vehicle.bicycle()
>>> bike
<__main__.Vehicle object at 0x7f947c0f7750>
>>> bike.description()
A vehicle with an None engine, and ['tire', 'tire'] tires
>>> bike.engine
>>> bike.tires
['tire', 'tire']


As we start modeling more and more concepts, there will be more situations where we'll want to use class methods to perform actions that require information available to only the class and doesn't require any instance information.
