
"""
Przykładowe rozwiązanie zadania 5.6
"""
from os import system


def czysc_slowo_cale(slowo):
    nowe_slowo = ""
    for litera in slowo.lower():
        if litera.isalpha():
            nowe_slowo += litera
    return nowe_slowo

# czysci tylko z lewej lub prawej nie usuwa w środku


def czysc_slowo(slowo):
    # Usuwamy spacje na początku i na końcu słowa
    slowo = slowo.strip()

    # Usuwamy znaki nie będące literami na początku słowa
    while len(slowo) > 0 and not slowo[0].isalpha():
        slowo = slowo[1:]

    # Usuwamy znaki nie będące literami na końcu słowa
    while len(slowo) > 0 and not slowo[-1].isalpha():
        slowo = slowo[:-1]

    # Zamieniamy słowo na małe litery
    slowo = slowo.lower()

    return slowo


system("cls")
print(czysc_slowo("66okno"))
print(czysc_slowo("Okno5%"))
print(czysc_slowo("$$Ok#no5%"))
print(czysc_slowo_cale("$$Ok#no5%"))
