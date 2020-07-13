#for item in 'Python':
#    print(item)

#for i in ['Python','suraj','Github']:
#    print(i)

#for j in range(1,10):
#    print(j)
##############  Calculate the sum of all items##############
#total = 0
#for price in [20,50,80]:
#    total = total + price
#print(f'Total: {total}')
    

#################Nested loops###################
### print (x,y cordinate)

#for xaxis in range(4):
#   for yaxis in range(3):
#        print(f'({xaxis}), ({yaxis})')

############################print pattern F based on a list of numbers
#numbers = [5, 2, 5, 2, 2]
numbers = [1, 1, 1, 1, 3]
for num in numbers:
    print ('x' * num)

###Using nested loop
for x_count in numbers:
    output = ''
    for count in range(x_count):
        output += '*'
    print(output)

####modify number to print L
        
