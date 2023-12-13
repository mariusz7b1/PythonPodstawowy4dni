"""
Funkcje - podstawy, parametry i wartosci domyslne

"""
import os
os.system("cls")


def funkcja_testowa(a, b=20, c=30):
    print(f"a={a}\tb={b}\tc={c}")


def funkcja_testowa_int(a, b=20, c=30):
    assert isinstance(a, int)
    assert isinstance(b, int)
    assert isinstance(c, int)
    print(f"Suma wynosi {a+b+c}")


# funkcja_testowa(1, 2, 3)
# funkcja_testowa(1)
# funkcja_testowa(c=1, a=2, b=6)


funkcja_testowa_int("1", 3, 3.99)
