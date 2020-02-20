#!/usr/bin/python3

def ratio(libraries):
    ratioArray = list()
    for library in libraries:
        ratioArray.append(sum(library["books"]) / (library["book_count"] * library["books_per_day"]))
    return ratioArray

def ratioArraySort(ratioArray, libraries):
    newratioArray = sorted(libraries, key=lambda library: ratioArray[library["id"]])
    return newratioArray

def librariesScore(libraries, booksScore):
    total = 0
    for library in libraries:
        total += sum([booksScore[book] for book in library["books"]])
    return total

def duplicateArraySort(libraries):
    signedUpBooks = list()
    newArray = list()
    for library in libraries:
        booksList = list()
        for book in library["books"]:
            if not book in signedUpBooks:
                booksList.append(book)
        library["books"] = booksList
        if len(booksList):
            newArray.append(library)
    return newArray
