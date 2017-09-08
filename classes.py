#!/usr/bin/python

class Pet(object):
    is_alive = True

    def __init__(self, name, age, asleep):
        self.name = name
        self.age = age
        self.asleep = asleep

    def description(self):
        print self.name, self.age


cat = Pet("Cole", 4, False)
cat2 = Pet("Marmalade", 2, True)
dog = Pet("Yoda", 5, False)
bird = Pet("Ari", 1, False)

print cat.name, cat.age, cat.asleep
print cat2.name, cat2.age, cat2.asleep, cat2.is_alive
print dog.name, dog.asleep
print bird.name, bird.age
dog.description()
print 4 << 3
