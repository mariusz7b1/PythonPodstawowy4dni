# Zbior w Pythonie to nieuporzadkowany zestaw unikalnych elementow.

# Tworzenie zbioru
zbiór = set()
print(f"Początkowy zbiór: {zbiór}")

# Dodawanie elementów do zbioru
zbiór.add("pomarańcza")
zbiór.add("jabłko")
zbiór.add("banan")
print(f"Zbiór po dodaniu owoców: {zbiór}")

# Usuwanie elementów ze zbioru
zbiór.remove("pomarańcza")
print(f"Zbiór po usunięciu pomarańczy: {zbiór}")

# Sprawdzanie, czy element jest w zbiorze
czy_jabłko_w_zbiorze = "jabłko" in zbiór
print(f"Czy jabłko jest w zbiorze? {czy_jabłko_w_zbiorze}")

# Operacje na zbiorach, takie jak unia, przecięcie i różnica.
zbiór_1 = set(["jabłko", "banan", "gruszka"])
zbiór_2 = set(["banan", "kiwi", "mango"])

unia = zbiór_1.union(zbiór_2)
przecięcie = zbiór_1.intersection(zbiór_2)
różnica = zbiór_1.difference(zbiór_2)

print(f"Unia zbiorów: {unia}")
print(f"Przecięcie zbiorów: {przecięcie}")
print(f"Różnica zbiorów: {różnica}")
