"""
Przykładowe rozwiązanie zadania 5.1
"""
from os import system


def modyfikuj_liste(lista_testowa, indeks, wartosc):
    try:
        lista_testowa[indeks] = wartosc
        return None
    except IndexError:
        return "Niepoprawny indeks."

# ZAD 1 a


def podziel(a, b):
    try:
        return a / b
    except (ZeroDivisionError, TypeError):
        return "Niepoprawne argumenty."


# ZAD 1 b


def pobierz_element(lista, indeks):
    try:
        return lista[indeks]
    except IndexError:
        return "Niepoprawny indeks."


def main():
    system("cls")
    lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    wynik = modyfikuj_liste(lista, 20, 99)
    print(wynik)


main()
