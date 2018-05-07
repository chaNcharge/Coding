from scipy.stats import chisquare

o = []
e = []
ratio = []
recommendedexpected = []

while True:
    tocalc = input("Enter one observed number. Enter a blank to finish. ")
    if tocalc == "":
        break
    else:
        o.append(float(tocalc))

while True:
    toratio = input("Enter hypothesis ratio, one number at a time. Enter a blank to finish. ")
    if toratio == "":
        break
    else:
        ratio.append(int(toratio))

ratiototal = sum(ratio)
observedtotal = sum(o)
for n in ratio:
    torecommendedexpected = observedtotal / ratiototal * n
    recommendedexpected.append(round(torecommendedexpected, 2))
print("Recommended expected numbers: ", recommendedexpected)

while True:
    toexp = input("Enter one expected number. Enter a blank to finish. ")
    if toexp == "":
        break
    else:
        e.append(float(toexp))

print(chisquare(o, f_exp=e))
