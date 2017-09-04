"""
Create a kickstarter with code!
Coded by chaNcharge
Only works on Python 3 and above!
Change all input commands to raw_input to work with older Python versions
"""

import time
import sys

def delay_print(s):
    for c in s:
        sys.stdout.write( '%s' % c )
        sys.stdout.flush()
        time.sleep(0.05)

delay_print("Hello! I'm here to judge your kickstarter idea!\n")

it_is = input("So, it is...")
that = input("That...")
but_it = input("But it...")
answer = input("So it's %s that %s but it %s? (answer with yes or no) " % (it_is, that, but_it))

if answer == "yes":
    if it_is == "a meme" and that == "memes" and but_it == "memes":
        time.sleep(1)
        delay_print ("MEMES?! ")
        time.sleep(1)
        delay_print("Best idea ever!!! Go ahead and sell it, it'll make millions!\n")
    elif it_is == "travis" or it_is == "a travis":
        time.sleep(1)
        delay_print("You weeaboo.\n")
        time.sleep(1)
        delay_print("riggity.\n")
    elif it_is == "a pun" or it_is == "a bad pun" or it_is == "a joke" or it_is == "a bad joke":
        time.sleep(1)
        delay_print("HAHAHAHA YES DO IT!\n")
    elif it_is == "shelby" or it_is == "a sheb" or it_is == "a shebby" or it_is == "shebby":
        time.sleep(1)
        delay_print("The girl with many names, interesting choice")
    elif that == "is depressed" or but_it == "is depressed":
        time.sleep(1)
        delay_print("Is it Marvin?\n")
        time.sleep(1)
        delay_print("I think you ought to know I'm feeling very depressed...\n")
    else:
        delay_print("It sucks, good luck selling that, because you're going to need it.\n")
elif answer == "no":
    delay_print ("Then why did you even bother running me? Go do something better with your life.\n")
else:
    delay_print ("You're supposed to say 'yes' or 'no', you illiterate scumbag.\n")
