####Jus like append,remove etc in list we can make class
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


