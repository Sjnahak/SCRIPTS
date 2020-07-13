course = 'Python for Beginners'

##calculate length of string
print(len(course))

print (course.upper()) ##here upper is method of string object called as course

print (course.lower())

##find index of an alphabet find and replace are case sensitive
print(course.find('y'))

####Replace function
print(course.replace('Beginners','Absolute Beginners'))

###to Search some character in string we use "in" operator
###output will be boolean value

print('Python' in course)
