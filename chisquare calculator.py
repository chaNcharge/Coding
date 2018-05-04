from scipy.stats import chisquare

o = []
e = []

while True:
    tocalc = input("Enter one observed number. Enter a blank to finish. ")
    if tocalc == "":
        break
    else:
        o.append(float(tocalc))

while True:
    toexp = input("Enter one expected number. Enter a blank to finish. ")
    if toexp == "":
        break
    else:
        e.append(float(toexp))

print(chisquare(o, f_exp=e))
