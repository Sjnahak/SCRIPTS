####Jus like append,remove etc in list we can make class
#Class start with a camel case
#self is instance of class
#Methods are functions inside a class
#Class variable or class attribute can be accessed as classname.attribute (Circle.pi)
#def __int__ (constructor of the class)
#attributes can be accessed as self.attribute

class Point:
    def move(self):
        print("move")
        
    def draw(self):
        print("draw")

##create object
point1 = Point()
point1.draw()


#####pass attribute to a class
point1.x = 10
point1.y = 20
print(point1.x)


