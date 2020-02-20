#!/usr/bin/python3

from parser import load_file
import sortlib
import sys

if (len(sys.argv) != 2):
    quit()
data = load_file(sys.argv[1])

libs = []

ratio = sortlib.ratio_one(data["libraries"])
libraries = sortlib.ratioArraySort(ratio, data["libraries"])
libs.append(sortlib.duplicateArraySort(libraries))
ddouble = sortlib.ratio_doubleone(libraries)
libs.append(sortlib.duplicateArraySort(ddouble))

ratio = sortlib.ratio_two(data["libraries"])
libraries = sortlib.ratioArraySort(ratio, data["libraries"])
libs.append(sortlib.duplicateArraySort(libraries))
ddouble = sortlib.ratio_doubleone(libraries)
libs.append(sortlib.duplicateArraySort(ddouble))

ratio = sortlib.ratio_three(data["libraries"])
libraries = sortlib.ratioArraySort(ratio, data["libraries"])
libs.append(sortlib.duplicateArraySort(libraries))
ddouble = sortlib.ratio_doubleone(libraries)
libs.append(sortlib.duplicateArraySort(ddouble))

best_score = -1
best_library = None
for lib in libs:
    score = sortlib.librariesScore(lib, data["book_scores"], data["days"])
    if score > best_score:
        best_library = lib
        best_score = score

def display_output(libraries):
    print(len(libraries))
    for library in libraries:
        booksList = sorted(library["books"], reverse=True)
        print(f"{library['id']} {len(library['books'])}")
        print(" ".join(map(lambda book: str(book), booksList)))

#print(len(data["libraries"]))
#print(len(libraries))
display_output(best_library)
