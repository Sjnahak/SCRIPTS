##Using double quotes and single quotes
#we are using apostophe in line 1 hence use double quote otherwise you will error
course = "Welcome to Python's Course for Beginners"
course2 = 'Welcome to Python Course for "Beginners"'
print (course)
print (course2)

## to get elements in variable use index
print (course[0])

#get multiple elements
print (course[0:3])
### Get Negative index
print (course[-1])

######## below will print the value "ura"
## Starting from 1 to last excluding the last value
name = 'suraj'
print(name[1:-1])

print (name[-1:1])####null value
#For Multiline string use ''' '''(triple quote)
#mail = '''
#Hi ,
#What is the first program you wrote in python
#thanks,
#____
#'''
#print(mail)

###########################formatted String############
first = 'John'
last = 'Smith'
message = first + ' [' + last + ']' + 'is a coder' ##this approach is difficult
print (message)

##f string or formatted way
msg = f'{first} [{last}] is a coder'
print (msg)
