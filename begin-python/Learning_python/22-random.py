###python3 module index
import random

for i in range(3):
    print(random.random())
    print(random.randint(0,3))

members = ['Mosh', 'Marry', 'Bob', 'Test']
leader = random.choice(members)
print(leader)

class Dice:
    def roll(self):
        first = random.randint(1,6)
        second = random.randint(1,6)
        return first, second

dice = Dice()
print(dice.roll())
