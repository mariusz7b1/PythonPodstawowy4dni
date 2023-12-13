
# Zadanie 1
def suma_trzech_liczb(a, b, c):
    return a + b + c

# Zadanie 2


def czy_parzysta(n):
    return n % 2 == 0

# Zadanie 3


def podziel_wyraz(wyraz, liczba):
    wynik = []  # pusta lista na przechowanie wyników
    i = 0  # zmienna pomocnicza do iteracji przez wyraz

    while i < len(wyraz):
        fragment = wyraz[i:i + liczba]  # wyciągamy fragment wyrazu
        wynik.append(fragment)  # dodajemy fragment do listy wyników
        i += liczba  # przesuwamy zmienną i o liczbę znaków w fragmencie

    return wynik  # zwracamy listę wyników


print(podziel_wyraz("tojestcalkiemdlugieslowo", 3))
