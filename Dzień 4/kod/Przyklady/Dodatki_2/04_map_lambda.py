from os import system
system("cls")

lista1 = [1, 2, 3, 4]
lista2 = [5, 6, 7, 8]

wynik_map = map(lambda x, y: x * y, lista1, lista2)
print(wynik_map)

wynik_map2 = list(wynik_map)
print(wynik_map2)

suma_iloczynow = sum(map(lambda x, y: x * y, lista1, lista2))
print(suma_iloczynow)  # Wynik: 70
