####constructor are used at the time of creating an object
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        
    def move(self):
        print("move")


    def draw(self):
        print("draw")

##create object
## self is reference to  current point object in memory
point1 = Point(10, 20)########

print(point1.x)
##you can update the value of x
point1.x = 11
print(point1.x)


################################################
class Person:
    def __init__(self, name):
        slef.name = name

    def talk(self):
        #print("talk")
        print(f"Hi am {self.name}")
john = Person("john smith")
print(john.name)
john.talk()

