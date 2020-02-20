#!/usr/bin/python3

from parser import load_file
import sortlib
import sys

if (len(sys.argv) != 2):
    quit()
data = load_file(sys.argv[1])
ratioArray = sortlib.ratio(data["libraries"])
print(ratioArray)
ratioArray = sortlib.ratioArraySort(ratioArray, data["libraries"])
print(ratioArray)

def display_output(libraries):
    print(len(libraries))
    for library in libraries:
        print(f"{library['id']} {len(library['books'])}")
        print(" ".join(map(lambda book: str(book), library["books"])))

display_output(ratioArray);