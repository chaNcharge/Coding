def is_happy(n):
	local_list = []
	while True:
		str_number = str(n)
		r = 0
		for i in str_number:
			r += (int(i) * int(i))
		if r == 1:
			return True
		elif r in local_list:
			return False
		local_list.append(r)
		n = r

def is_prime(x):
	if x < 2:
		return False
	else:
		for n in range(2, x):
			if x % n == 0:
			   return False
		return True

# my list
happy_list = [n for n in range(1, 501) if is_happy(n) == True]
happy_primes = [n for n in range(1, 501) if is_happy(n) == True and is_prime(n) == True]

print "Happy Numbers:", happy_list
print
print "Happy Primes:", happy_primes
print "Sequence:", filter(lambda x: x >= 313 and x <= 400, happy_primes)