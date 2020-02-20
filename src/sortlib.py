#!/usr/bin/python3

def ratio_one(libraries):
    ratioArray = list()
    for library in libraries:
        ratioArray.append((sum(library["books"]) * library["signup_days"]) / (library["book_count"] * library["books_per_day"]))
    return ratioArray

def ratio_two(libraries):
    ratioArray = list()
    for library in libraries:
        ratioArray.append((library["signup_days"] * (library["book_count"]) * library["books_per_day"]))
    return ratioArray   

def ratioArraySort(ratioArray, libraries):
    newratioArray = sorted(libraries, key=lambda library: ratioArray[library["id"]])
    return newratioArray

def librariesScore(libraries, booksScore, deadline):
    total = 0
    total_days = 0
    for library in libraries:
        if total_days + library["signup_days"] <= deadline:
            total_days += library["signup_days"]
            total += sum([booksScore[book] for book in library["books"]])
        else:
            break
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
