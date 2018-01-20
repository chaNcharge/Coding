import os

find = input("Find: ")

for fname in os.listdir("."):
    fname_noext, ext = os.path.splitext(fname)
    if fname.startswith(find):
        os.rename(fname, fname[len(find):])
    if fname_noext.endswith(find):
        os.rename(fname, (fname_noext[:len(find)] + ext))
