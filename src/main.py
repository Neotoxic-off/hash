#!/usr/bin/python3

from parser import load_file
import sortlib
import sys

if (len(sys.argv) != 2):
    quit()
data = load_file(sys.argv[1])
ratio = sortlib.ratio_one(data["libraries"])
libraries = sortlib.ratioArraySort(ratio, data["libraries"])
libraries = sortlib.duplicateArraySort(libraries)

def display_output(libraries):
    print(len(libraries))
    for library in libraries:
        booksList = sorted(library["books"], reverse=True)
        print(f"{library['id']} {len(library['books'])}")
        print(" ".join(map(lambda book: str(book), booksList)))

#print(len(data["libraries"]))
#print(len(libraries))
display_output(libraries)