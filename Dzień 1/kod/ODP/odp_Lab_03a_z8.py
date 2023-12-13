"""
Przykładowa relizacja:
Zadanie 8  z Laboratorium 03a
"""

lista = [['a', 'b', 'c'], ['d', 'e', 'f'], ['g', 'h', 'i']]
i = int(input("Podaj indeks i: "))
j = int(input("Podaj indeks j: "))

if 0 <= i < len(lista) and 0 <= j < len(lista[i]):
    print(lista[i][j])
else:
    print("Podane indeksy są poza zakresem.")
