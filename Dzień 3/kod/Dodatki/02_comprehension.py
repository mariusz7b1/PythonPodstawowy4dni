""""   Comprehension  """
from os import system
system("cls")
# List
# tworzenie listy kwadratów liczb parzystych
kwadraty_parzyste = [x**2 for x in range(1, 11) if x % 2 == 0]

# litery z tekstu
litery_w_tekscie = [znak for znak in 'Hello, World!' if znak.isalpha()]

# Słowniki
#  - tworzenie słownika z liczbami i ich kwadratami
kwadraty_slownik = {x: x**2 for x in range(1, 6)}

# zamiana kluczy i wartości w słowniku
odwrocony_slownik = {wartosc: klucz for klucz, wartosc in {'a': 1, 'b': 2}.items()}

# Zbiory
# tworzenie zbioru kwadratów liczb
kwadraty_zbior = {x**2 for x in [1, 2, 3, 4, 5]}

# Set Comprehension - tworzenie zbioru z unikalnymi elementami z listy
unikalne_elementy = {element for element in [1, 2, 2, 3, 3, 3, 4]}


# Wyświetlanie wyników
print("Kwadraty parzyste:", kwadraty_parzyste)
print("Litery w tekście:", litery_w_tekscie)

print("Słownik kwadratów:", kwadraty_slownik)
print("Odwrocony słownik:", odwrocony_slownik)

print("Zbiór kwadratów:", kwadraty_zbior)
print("Unikalne elementy:", unikalne_elementy)
