from time import time, sleep
from sys import version

start = time()
print(version)
end = time()
elapsed = end - start
print("Time:", elapsed)
sleep(2)

start = time()
timelist = []

for i in range(1000001):
	timelist.append(i)

end = time()
elapsed = end - start

print('Time:', elapsed)