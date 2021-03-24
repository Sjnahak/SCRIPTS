i = 1
while i <=3:
    print (i)
    i = i + 1
print("done")

i = 1
while i <=3:
    print ('*' * i)
    i = i + 1
print("done")


##########Guessing game###########################
secret_number = 9
guess_count = 0
guess_limit = 3

while guess_count < guess_limit:
    guess_number = int(input('guess number: '))
    guess_count += 1
    if guess_number == secret_number:
        print ("you win")
        break ###break the loop when success
else:
    print ("You failed")

    
    
