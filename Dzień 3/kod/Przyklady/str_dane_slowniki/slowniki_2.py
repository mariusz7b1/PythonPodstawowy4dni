"""Przykłady słowniki"""
from os import system
system("cls")

dct1 = {'k1': 1, 'k2': 2}

dct1['k3'] = 3
print(dct1)

dct1['k1'] = 10
print(dct1)

dct2 = {'k1': 100, 'k3': 30, 'k4': 40}

dct1.update(dct2)
print(dct1)

# startujemu od nowa
dct1 = {'k1': 1, 'k2': 2}
dct1.update(k1=10, k3=3, k4=4)
print(dct1)
