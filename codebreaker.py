from random import randint

code = int(input("Enter 6 digit code to be cracked: "))
crackedcode = 0

while code != crackedcode:
    crackedcode = randint(1, 999999)
    print(crackedcode, end='\r')

print("The code is " + str(crackedcode))
