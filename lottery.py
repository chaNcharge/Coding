from random import sample

lotterynumbers = sample(range(10), 5)

my_numbers = []

for _ in range(5):
    my_numbers.append(int(input("Enter 1 number, then press return: ")))
print("Lottery numbers are " + str(lotterynumbers))
print("Your numbers are " + str(my_numbers))
if set(my_numbers) == set(lotterynumbers):
    print("You win!")
else:
    print("You lose!")
