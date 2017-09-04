#!/usr/bin/python

shopping_list = ["banana", "orange", "meme", "meme", "pear", "meme", "apple"]

stock = {
	"banana": 6,
	"apple": 0,
	"orange": 32,
	"pear": 15,
	"meme": 21
}
	
prices = {
	"banana": 4.99,
	"apple": 2.99,
	"orange": 1.49,
	"pear": 3.99,
	"meme": 5.99
}

def compute_bill(food):
	total = 0
	for i in food:
		if stock[i] > 0:
			total += prices[i]
			stock[i] -= 1
	return total
	
bill = compute_bill(shopping_list)

print bill