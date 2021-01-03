"""
                By GTDT
              11/19/2020

    51  Challange: Random Number Generator

              7 points

Make a basic program that generate a number between 1-10 and the input should say 'enter a number'
when you enter the number the bot should also select a random number between 1-10 if your number
luckily is the same as the program, the program answers You won! i select <number> and you selected
<number> if your number doesen't matches the program. It should answer with well looks like you lost try again
"""

import random

R = random.randint(1, 10)

EnterN = int(input("Enter a number: "))

if EnterN == R:
    print("You won!")
else:
    print("Well looks like you lost try again")

print(f"The number was {R}")

