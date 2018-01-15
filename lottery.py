#!/usr/bin/env python3
''' 
A lottery that chooses 5 random numbers from 0 - 9.
5 numbers are user inputs.
If they all match, the user wins.
'''

from random import sample

lotterynumbers = sample(range(10), 5)

my_numbers = []
numsinlist = 0

# Checks if there are less than 5 numbers in the list. Does not add duplicates.
while numsinlist < 5:
    numinput = int(input("Enter 1 number 0 - 9, then press return: "))
    if numinput in my_numbers:
        print("That number is already in the ticket.")
    else:
        my_numbers.append(numinput)
        numsinlist += 1

print("Lottery numbers are " + str(lotterynumbers))
print("Your numbers are " + str(my_numbers))
if set(my_numbers) == set(lotterynumbers):
    print("You win!")
else:
    print("You lose!")
