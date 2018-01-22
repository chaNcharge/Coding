import os

search = input("Search for: ")
replace = input("Replace with: ")
path = os.path.dirname(os.path.realpath(__file__))
path.remove("renamereplace.py")

for f in os.listdir(path):
    os.rename(os.path.join(path, f), 
              os.path.join(path, f.replace(search, replace)))
