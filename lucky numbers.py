#!/usr/bin/python

from random import randint

luckynum = randint(1, 20)
guesses = 5

while guesses > 0:
	luckyguess = int(raw_input("What is your lucky number? Guesses left: %s: " % (guesses)))
	if luckyguess == luckynum:
		print "That is your lucky number!"
		break
	else:
		guesses -= 1
else:
	print "You lose :("