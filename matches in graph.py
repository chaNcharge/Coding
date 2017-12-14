#!/usr/bin/env python3
# Requires matches.py to work

from matplotlib import pyplot as plt
from matches import get_time, run

get_time()
counts = [run(10000) for _ in range(1000)]
plt.hist(counts, bins=20)
plt.show()
