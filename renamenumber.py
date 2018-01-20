import os

choice = input("Remove the start or end of file? Input 'start' or 'end': ")
characters = int(input("Characters to remove: "))
files = os.listdir(".")
files.remove("renamenumber.py")

for fname in files:
    fname_noext, ext = os.path.splitext(fname)
    if choice == "start":
        os.rename(fname, fname[characters:])
    if choice == "end":
        os.rename(fname, (fname_noext[:-characters] + ext))
