"""Przykłady słowniki"""
from os import system
system("cls")

dct1 = {'k1': 1, 'k2': 2}
dct2 = dct1
print(f"czy dct1 i dct2 to ten sam słownik  {dct1 is dct2}")

dct1['k3'] = 3
print(dct2)

dct2 = dct1.copy()
print(f"czy dct1 i dct2 to ten sam słownik  {dct1 is dct2}")
dct2['k4'] = 40
print(dct1)
print(dct2)

dct3 = dct1.items()
print(f"czy dct1 i dct3 to ten sam słownik  {dct1 is dct3}")


for klucz, wartosc in dct1.items():
    print(f"{klucz}->{wartosc}")
