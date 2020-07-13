#### to handle error try and except block
##In except paas the type of error you want to handle
try:
    age = int(input('Age: '))
    print(age)
except ZeroDivisionError:
    print('Age Cannot divide with zero')
except ValueError:
    print('Invalid value')

    
