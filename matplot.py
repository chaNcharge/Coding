import matplotlib.pyplot as plt
from numpy.random import randn

a = randn(10000)
plt.hist(a)
plt.show()

def mean(b, c, d):
    return (b + c + d) / 3