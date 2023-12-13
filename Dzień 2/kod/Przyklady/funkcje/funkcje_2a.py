"""
Funkcje - podstawy, parametry pozycyjne i nazwane
"""
import os
os.system("cls")


def funkcja_testowa(a, b, c):
    print(f"a={a}\tb={b}\tc={c}")


funkcja_testowa(1, 2, 3)

funkcja_testowa(c=1, a=2, b=6)

funkcja_testowa(11, 12, c=90)

funkcja_testowa(11, c=12, b=90)

funkcja_testowa (11, c=12, 90)
# tak być nie możę - argument pozycyjny nie może nastepować po nazwanym
