""" """
from os import system
system("cls")


def zla_funkcja(n):
    try:
        return n / 0
    except ZeroDivisionError as e:
        raise ArithmeticError("Mam bład") from e


try:
    zla_funkcja(0)
except ArithmeticError as blad:
    print(blad)

print("KONIEC działania")
