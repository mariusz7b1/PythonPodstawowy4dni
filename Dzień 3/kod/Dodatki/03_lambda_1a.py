""" Funkcja anonimowa lambda oraz  ,metoda sort"""
from os import system
system("cls")

lista_krotek = [(1, 6), (3, 11), (15, 1), (4, 2)]


def sortuj(war):
    return war[1]
# Użyj funkcji lambda do sortowania listy
# według drugiego elementu każdej krotki


lista_krotek.sort(key=sortuj, reverse=True)
print(lista_krotek)

lista_krotek.sort(key=lambda element: element[1], reverse=True)
print(lista_krotek)


lista_krotek.sort(key=lambda element: element[0] + element[1])
print(lista_krotek)


lista_krotek.sort(key=lambda element: element[0] * element[1])
print(lista_krotek)

# inny przykład
lista_slow = "ala ma kota i kot jest najwspanialszy z kotow jakie ona zna".split()
print(lista_slow)
lista_slow.sort(key=len, reverse=True)
print(lista_slow)
