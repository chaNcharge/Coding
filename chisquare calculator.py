from scipy.stats import chisquare

o = []

while True:
    tocalc = input("Enter a number. Enter a blank to finish. ")
    if tocalc == "":
        break
    else:
        o.append(int(tocalc))

print(chisquare(o))
