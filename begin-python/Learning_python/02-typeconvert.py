#calculate age based on birth year
birth_year = input('Enter your Birth Year: ')
#####we cannot subtract a number from string hence convert birth year to number using int
print (type(birth_year))##### to get the type of variable use "type" function
age = 2020 - int(birth_year)
print (type(age))
print(age)


##Ask a user their weigh in pounds convert it into kilograms and print on terminal

weight = input('Enter your weight in pounds: ')

weight_kg = int(weight) * 0.45
print(weight_kg)
