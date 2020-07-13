#def greet_user():
#    print('HI There!')
#    print('Welcome aboard')


#print("Start")
#greet_user()
#print('Finish')


#######Parameter in function
def greet_user(name, lastname):
    print(f'HI {name} {lastname}')
    print('Welcome aboard')


print("Start")
greet_user("John", "smith") ##argument with multiple values
print('Finish')


##############using Keyword argument position of the parameter doesnot matter
######helps in easy reading when using numerical value
###always use positional argument before keyword argument
greet_user(lastname="John",name="smith")


########Return value to a function
def square(number):
    return number * number


print(square(3))
####By default function in python retursn None
