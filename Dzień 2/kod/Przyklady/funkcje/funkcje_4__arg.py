"""
Funkcje - tablica argumentów
"""
from os import system
system('cls')


def pokaz_arumenty(*args):
    print(type(args))
    print(f"Przekazano {len(args)} argumentów")
    for war in args:
        print(war, end=",")
    # koniec funkcji


pass
pokaz_arumenty("ala", 1, 2.7, "ma", 88, 2.5)
print()
lst1 = [1, 2, 3]
pokaz_arumenty(*lst1)
