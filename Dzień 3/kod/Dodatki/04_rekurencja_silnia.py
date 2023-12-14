""" Rekurencja - przykład"""
from os import system
system("cls")


def silnia(liczba):
    if liczba == 0 or liczba == 1:
        return 1
    else:
        return liczba * silnia(liczba - 1)


wartosc = int(input("Podaj liczbę ? "))
wynik = silnia(wartosc)
print(f"Silnia dla liczby {wartosc} wynosi {wynik}")
