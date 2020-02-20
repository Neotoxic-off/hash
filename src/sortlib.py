#!/usr/bin/python3

def ratio(libraries):
    ratioArray = list()
    for library in libraries:
        ratioArray.append(library["signup_days"] * (library["book_count"] / library["books_per_day"]))
    return ratioArray

def ratioArraySort(ratioArray, libraries):
    newratioArray = sorted(libraries, key=lambda library: ratioArray[library["id"]])
    return (newratioArray)