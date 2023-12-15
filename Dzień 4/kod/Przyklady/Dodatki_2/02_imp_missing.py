class MyDict(dict):
    def __missing__(self, key):
        return f"Klucz {key} nie istnieje w słowniku."


# Tworzenie instancji klasy CustomDict
dct1 = MyDict({"a": 1, "b": 2, "c": 3})

# Uzyskiwanie wartości dla istniejących kluczy
print(dct1["a"])  # Wypisze: 1
print(dct1["b"])  # Wypisze: 2

# Uzyskiwanie wartości dla nieistniejących kluczy
print(dct1["d"])  # Wypisze: Klucz d nie istnieje w słowniku.
