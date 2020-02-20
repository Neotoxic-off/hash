#!/usr/bin/python3

def ratio_one(libraries):
    ratioArray = list()
    for library in libraries:
        ratioArray.append((sum(library["books"]) * library["signup_days"]) / (library["book_count"] * library["books_per_day"]))
    return ratioArray

def ratio_two(libraries):
    ratioArray = list()
    for library in libraries:
<<<<<<< HEAD
        ratioArray.append((library["signup_days"] * library["book_count"] * library["books_per_day"]))
    return ratioArray   
=======
        ratioArray.append((library["signup_days"] * (library["book_count"]) * library["books_per_day"]))
    return ratioArray
>>>>>>> c5a84250fc75f892466d1c5e8ea197fbef3544f1

def ratio_three(libraries):
    ratioArray = list()
    for library in libraries:
        ratioArray.append(library["signup_days"] / (library["book_count"] * library["books_per_day"]))
    return ratioArray

def ratio_doubleone(libraries):
    ratioArray = list()
    for i in range(len(libraries)):
        library = libraries[i]
        ratioArray.append(sum(library["books"]) * i / library["books_per_day"])
    return ratioArray

def ratioArraySort(ratioArray, libraries):
    newratioArray = sorted(libraries, key=lambda library: ratioArray[library["id"]])
    return newratioArray

def librariesScore(libraries, booksScore, deadline):
    total = 0
    total_days = 0
    for library in libraries:
        if total_days + library["signup_days"] <= deadline:
            books_len = len(library["books"])
            book_days = 0
            total_days += library["signup_days"]
            for i in range(0, books_len, library["books_per_day"]):
                for j in range (i, i + library["books_per_day"]):
                    if j < books_len:
                        total += booksScore[library["books"][j]]
                book_days += 1
                if total_days + book_days > deadline:
                    return total
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
