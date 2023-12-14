"""Przykładowe rozwiazania 8b"""

# 01


def policz_znaki(tekst):
    slownik = {}
    for znak in tekst:
        if znak in slownik:
            slownik[znak] += 1
        else:
            slownik[znak] = 1
    return slownik


# 02
def porownaj_slowniki(slownik1, slownik2):
    return slownik1 == slownik2


# 03
def zamien_klucze_z_wartosciami(slownik):
    return {v: k for k, v in slownik.items()}

# 04


def sortuj_po_wartosciach(slownik):
    return {k: v for k, v in sorted(slownik.items(), key=lambda item: item[1])}

# 05


def usun_po_wartosci(slownik, wartosc):
    return {k: v for k, v in slownik.items() if v != wartosc}


def main():
    dni_tygodnia = {
        "A": 4,
        "B": 6,
        "C": 8,
        "D": 7
    }
    print(policz_znaki("Ala ma kota ale kota ni elubi ali i nic z tym nie zrobimy"))
    wynik = sortuj_po_wartosciach(dni_tygodnia)
    print(wynik)

    wynik = usun_po_wartosci(dni_tygodnia, 6)
    print(wynik)


if __name__ == '__main__':
    main()
