print(10 / 3)####gives floating number
print(10 // 3)#####gives integer
print(10 % 3) ###gives us the remainder
print(10**3) ###expontetial


##########
x = 10
#x = x + 3
###a different way by augumented and enhanced operator
x += 3
print(x)
x -= 3
print(x)

##############operator precedence
y = 10 + 3 * 10 / 5
print(y)

z = (10 + 3) * 2 ** 2
#####order is
##if we add parenthesis always takes the priority
#exponentiation 2 **3
#multiplication or division
#addtion or subtraction
#if same kind of opertor precedence is present go right to left

#############Math Function####################
x = 2.9
print(round(x)) ###round of value
print(abs(-2.9))  ##Always gives positive value

#####to use math function python 3 math module to learn all other function
import math 
print(math.ceil(2.9)) ###gives 3
print(math.ceil(2.9)) ### gives 2
