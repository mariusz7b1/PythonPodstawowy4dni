"""
Funkcje - podstawy, parametry i wartosci domyslne

"""
import os
os.system("cls")


def funkcja_testowa(a, b=20, c=30):
    print(f"a={a}\tb={b}\tc={c}")


funkcja_testowa(1, 2, 3)
funkcja_testowa(1)
funkcja_testowa(c=1, a=2, b=6)
