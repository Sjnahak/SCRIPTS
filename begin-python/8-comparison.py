temperature = 35

#### < > <= >= == (not equal!=)
if temperature > 30:
    print("It's a hot day")
else:
    print("It's not hot day")


name = input("Enter your name: ")

if len(name) < 3:
    print ("Name must be atlease 3 character long")
elif len(name) > 50:
    print("Name can be maximum of 50 character long")
else:
    print("Name looks Good")
