from os import system
from random import randint
system("cls")

# deklaracja słownika i listy
lista_nazwisk = []

# wczytywanie danych
zm_robocza = 1
while zm_robocza < 10:
    # odczytaj z pliku kolejną linie
    dct = {}
    dct["imie"] = "Jan_" + str(zm_robocza)          # najcześciej dane z pliku
    dct["nazwisko"] = "Nowak_" + str(zm_robocza)
    dct["wiek"] = randint(20, 90)
    lista_nazwisk.append(dct)
    zm_robocza += 1

record = (lista_nazwisk[-2])["nazwisko"]

print(record)
