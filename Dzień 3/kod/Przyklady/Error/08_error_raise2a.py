""" """
from os import system
system("cls")


def zla_funkcja(n):
    try:
        return n / 0
    except Exception as e:
        raise


try:
    zla_funkcja(0)
except ArithmeticError:
    print("Bład Arytmetyczny!")

print("KONIEC działania")
