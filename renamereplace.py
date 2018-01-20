import os

search = input("Search for: ")
replace = input("Replace with: ")
path = "."

for f in os.listdir(path):
    os.rename(os.path.join(path, f), 
              os.path.join(path, f.replace(search, replace)))
