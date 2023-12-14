"""Przykładowe rozwiazania 8a"""
# 2


def pobierz_wartosc(slownik, klucz):
    return slownik.get(klucz, "Klucz nie istnieje")

# 3


def polacz_slowniki(slownik1, slownik2):
    slownik1.update(slownik2)
    return slownik1

# 4


def lista_kluczy(slownik):
    return list(slownik.keys())

# 5


def lista_wartosci(slownik):
    return list(slownik.values())


def main():
    dni_tygodnia1 = {
        "poniedziałek": 1,
        "wtorek": 2,
        "środa": 3,
    }

    dni_tygodnia2 = {
        "czwartek": 4,
        "piątek": 5,
        "sobota": 6,
        "niedziela": 7
    }
    print(pobierz_wartosc(dni_tygodnia1, "wtorek"))
    print(pobierz_wartosc(dni_tygodnia1, "czwartek"))
    dni_tygodnia = polacz_slowniki(dni_tygodnia1, dni_tygodnia2)
    print(lista_kluczy(dni_tygodnia))
    print(lista_wartosci(dni_tygodnia))


if __name__ == '__main__':
    main()
