"""
Przykładowa relizacja:
Zadanie 3  z Laboratorium 03a
"""
from os import system
system('cls')

# wczytywanie danych
lst = []
n = int(input("Podaj liczbę naturalną ? "))
for i in range(n):
    liczba = int(input(f"Podaj[{i}] ? "))
    lst.append(liczba)

wartosc_maksymalna = max(lst)
wartosc_minnimalna = min(lst)
print(lst)
print(f"Wartosc maksymalna to {wartosc_maksymalna}")
print(f"Wartosc minimalna to {wartosc_minnimalna}")
