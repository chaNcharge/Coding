from math import sqrt

q2 = float(raw_input("Enter recessive genotype frequency: "))
q = sqrt(q2)
p = 1 - q
p2 = p**2
pq2 = 2 * p * q

print "p =", p
print "q =", q
print "p^2 =", p2
print "q^2 =", q2
print "2pq =", pq2
