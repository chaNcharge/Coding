#!/usr/bin/env python3
''' 
This program runs forever until a match is found,
then prints the results into the console, showing
how many times it loops and what the match is.
'''
import random as r
from datetime import datetime
import calendar

def get_time():
    ''' Prints a timestamp '''
    d = datetime.utcnow()
    unixtime = calendar.timegm(d.utctimetuple())
    unixtimee = datetime.fromtimestamp(unixtime)
    print(unixtimee)

def run(maxnum):
    ''' Loops until a match is found, until a match are found '''
    counter = 0
    while True:
        var1 = r.randint(0,maxnum)
        var2 = r.randint(0,maxnum)

        counter += 1

        if var1 == var2:
            print("Match is: {}".format(var1))
            print("Iterations: {} times.".format(counter))
            get_time() 
            return counter

if __name__ == "__main__":
    get_time()
    run(10000000)
