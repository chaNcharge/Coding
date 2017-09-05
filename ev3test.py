#!/usr/bin/env python3

import time, random
import ev3dev.ev3 as ev3

random.seed( time.time() )

def quote(topic):
	"""
	Recite a random Marvin the Paranoid Android quote on the specified topic.
	See https://en.wikipedia.org/wiki/Marvin_(character)
	"""

	marvin_quotes = {
			'initiating' : (
				"Life? Don't talk to me about life!",
				"Now I've got a headache.",
				"This will all end in tears.",
				),
			'depressed' : (
				"I think you ought to know I'm feeling very depressed.",
				"Incredible... it's even worse than I thought it would be.",
				"I'd make a suggestion, but you wouldn't listen.",
				),
			}

	ev3.Sound.speak(random.choice(marvin_quotes[topic])).wait()

quote()