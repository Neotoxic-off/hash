def load_file(filepath: str):
    try:
        with open(filepath, 'r') as h:
            lines = h.readlines()

    except Exception as e:
        print(f"Could not open {filepath}: {e}")
        return None

    data = {
        "book_count": 0, # B
        "library_count": 0, # L
        "days": 0, # D
        "book_scores": {},
        "libraries": []
    }

    g_values = lines[0].split()
    data["book_count"] = int(g_values[0])
    data["library_count"] = int(g_values[1])
    data["days"] = int(g_values[2])

    scores = lines[1].split()
    for i in range(0, len(scores)):
        data["book_scores"][i] = int(scores[i])

    library_nb = 0
    for i in range(2, data["library_count"] * 2 + 1, 2):
        library_values = lines[i].split()
        library = {
            "id": library_nb,
            "book_count": int(library_values[0]),
            "signup_days": int(library_values[1]),
            "books_per_day": int(library_values[2]),
            "books": [],
        }

        books = lines[i + 1].split()
        for book in books:
            library["books"].append(int(book))

        data["libraries"].append(library)

        library_nb += 1

    return data
