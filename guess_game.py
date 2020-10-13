import random
from random import randint

guess_range = randint(1,10)

if guess_range % 2 == 0:
        print(f" your number {guess_range} is divisible by 2 ")
        if guess_range == 6:
            print(" You have the lucky number 6 ")

else:
    print(f"This {guess_range} must be an Odd number")
