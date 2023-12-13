"""
Funkcje - podstawy, parametry i wartosci domyslne

"""
import os
os.system("cls")


def funkcja_testowa(a, b=20, c=30):
    print(f"a={a}\tb={b}\tc={c}")


def funkcja_testowa_int(a, b=20, c=30):
    if not isinstance(a, int):
        print("złe a")
        return False

    print(isinstance(b, int))
    print(isinstance(c, int))
    print(f"a={a}\tb={b}\tc={c}")
    return True


funkcja_testowa('a', 2, 3)
funkcja_testowa(1)
funkcja_testowa(c=1, a=2, b=6)


funkcja_testowa_int("1", 3, 3.99)
