""" Funkcja anonimowa lambda f  sorted"""
from os import system
system("cls")

lista_krotek = [(1, 6), (3, 11), (15, 1), (4, 2)]


def sortuj(war):
    return war[1]
# Użyj funkcji lambda do sortowania listy
# według drugiego elementu każdej krotki


lista_wynik = sorted(lista_krotek, key=sortuj, reverse=True)
print(lista_wynik)


lista_wynik = sorted(lista_krotek, key=lambda element: element[1], reverse=True)
print(lista_wynik)

lista_wynik = sorted(lista_krotek, key=lambda element: element[0] + element[1])
print(lista_wynik)

lista_wynik = sorted(lista_krotek, key=lambda element: element[0] * element[1])
print(lista_wynik)
