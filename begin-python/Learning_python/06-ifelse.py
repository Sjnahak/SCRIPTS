is_hot = False  ###change this value to see different output in if
is_cold = False
if is_hot:
    print("It's a hot day")
    print("Drink plenty of water")
elif is_cold:
    print("It's a cold day")
    print("Wear warm clothes")
else:
    print("It's a lovely day")
print("Enjoy your day")


########################################
price_house=1000000
good_credit = True
if good_credit:
    down_payment = 0.1 * price_house
else:
    down_payment = 0.2 * price_house
print(f'Downpayment : ${down_payment}')
    
    
********** Optimized if else **********

Pythonscript.py

#############Python if other way ####################ß
name = input("What is your first name? ")

# 1) Call `print` with a different string using a single conditional expression
print(
        "Your name is as long or longer than the average first name in the United States"
) if len(name) >= 6 else print(
        "Your name is shorter than the average first name in the United States"
)

# 2) Set `message` using a single conditional expression
message = ( 
        "The first letter in your name is among the five most common"
        if name[0].lower() in ["a", "j", "m", "e", "l"]
        else "The first letter of your name is not among the five most common"
)

print(message)

# 3) Change the string passed to the `print` function using a conditional expression
for letter in name:
    if letter.lower() in ["a", "e", "i", "o", "u"]:
        print(f"{letter} is a vowel")
    else:
        print(f"{letter} is a consonant")

for letter in name:
    print(
        f"{letter} {'is a vowel' if letter.lower() in ['a', 'e', 'i', 'o', 'u'] else 'is a consonant'}"
    )
