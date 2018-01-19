#!/usr/bin/env python3
''' 
A lottery that chooses 5 random numbers from 1 - 9.
5 numbers are user inputs.
If they all match, the user wins.
'''

from random import sample

lotterynumbers = sample(range(1, 10), 5)

my_numbers = []
numsinlist = 0

# Checks if there are less than 5 numbers in the list. Does not add duplicates.
while numsinlist < 5:
    numinput = int(input("Enter 1 number 1 - 9, then press return: "))
    if numinput in my_numbers:
        print("That number is already in the ticket.")
    elif numinput < 1 or numinput > 9:
        print("That number is out of range of the lottery numbers.")
    else:
        my_numbers.append(numinput)
        numsinlist += 1

print("Lottery numbers are " + str(lotterynumbers))
print("Your numbers are " + str(my_numbers))
if set(my_numbers) == set(lotterynumbers):
    print("You win!")
else:
    print("You lose!")
