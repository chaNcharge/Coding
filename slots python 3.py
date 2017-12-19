#!/usr/bin/env python3

# Python Slots developed by chaNcharge

from random import randint
from time import sleep


def autospin():
    times_spun = 0
    try:
        spins = int(input("How many times would you like to spin? "))
    except:
        raise ValueError("Invalid number entered, please rerun.")
    for _ in range(spins):
        times_spun += 1
        slot1 = randint(1, 13)
        slot2 = randint(1, 13)
        slot3 = randint(1, 13)
        print(slot1, slot2, slot3)
        if slot1 == slot2 == slot3:
            print("You win!!!", "Spins until win: %s" % times_spun)
            if slot1 and slot2 and slot3 == 13:
                print("Wait! That's all 13's! You lose anyway! :(")
            elif slot1 and slot2 and slot3 == 7:
                print("You got the jackpot!!! :D")
            break
    else:
        print("No luck this time :(")


def manualspin():
    print("Press enter to spin...")
    times_spun = 0
    while True:
        spin = input()
        times_spun += 1
        slot1 = randint(1, 13)
        slot2 = randint(1, 13)
        slot3 = randint(1, 13)
        print(slot1, slot2, slot3, end="\r")
        if slot1 == slot2 == slot3:
            print("You win!!!", "Spins until win: %s" % times_spun)
            if slot1 and slot2 and slot3 == 13:
                print("Wait! That's all 13's! You lose anyway! :(")
            elif slot1 and slot2 and slot3 == 7:
                print("You got the jackpot!!! :D")
            break


def coinslot():
    coins = 30
    print("Press enter to spin...")
    while coins > 0:
        spin = input("\nCoins left: %s" % coins)
        coins -= 1
        for _ in range(30):
            sleep(0.05)
            slot1 = randint(1, 7)
            slot2 = randint(1, 7)
            slot3 = randint(1, 7)
            print(slot1, slot2, slot3, end = "\r")
        if slot1 == slot2 == slot3:
            print("\nYou win!!!")
            if slot1 and slot2 and slot3 == 1:
                coins += 10
            elif slot1 and slot2 and slot3 == 2:
                coins += 20
            elif slot1 and slot2 and slot3 == 3:
                coins += 30
            elif slot1 and slot2 and slot3 == 4:
                coins += 40
            elif slot1 and slot2 and slot3 == 5:
                coins += 50
            elif slot1 and slot2 and slot3 == 6:
                coins += 60
            elif slot1 and slot2 and slot3 == 7:
                coins += 100
                print("Jackpot!!!")
    else:
        print("\nOut of coins :(")


# Init

print("Slot options: 'auto' 'manual' 'coin'")
choice = input("Type: ")
if choice == "auto":
    autospin()
elif choice == "manual":
    manualspin()
elif choice == "coin":
    coinslot()
else:
    print("Invalid option: please run again and answer using 'auto', 'manual', or 'coin'")
