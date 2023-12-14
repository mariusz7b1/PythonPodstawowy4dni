"""
Przykładowe rozwiązanie zadania 5.2 i 5.3
"""
import itertools
from os import system
system("cls")


def check_palimdrom_v1(tekst):
    """Sprawdza czy podany tekst to palimdrom 'recznie odwracajac tekst"""
    tekst = (tekst.lower()).replace(" ", "")
    # tekst = tekst.lower()
    # tekst = tekst.replace(" ", "")

    t2 = ""
    for i in range(len(tekst), 0, -1):
        t2 += tekst[i - 1]
    return tekst == t2


def check_palimdrom_v2(tekst):
    """Sprawdza czy podany tekst to palimdrom wycinki z krokiem -1"""
    # wyciananie spacji i zamienianie na małe litery
    tekst = (tekst.lower()).replace(" ", "")
    # tekst [::-1] daje w odwrotnej  kolejności
    return tekst == tekst[::-1]


def check_palimdrom_v3(tekst):
    """Sprawdza czy podany tekst to palimdrom zamiast replace split i join"""
    # wyciananie spacji ale inaczej
    tekst = ("".join(tekst.split())).lower()

    # tekst [::1] daje w odwrotnej  kolejności
    return tekst == tekst[::-1]


def check_anagran_v1(t1, t2):
    """Sprawdza czy podane tekst to anagramy"""
    lst1 = list(t1.replace(" ", "").lower())
    lst2 = list(t2.replace(" ", "").lower())
    lst1.sort()
    lst2.sort()
    return lst1 == lst2


def check_anagran_v2(t1, t2):
    """Sprawdza czy podane tekst to anagramy"""
    wynik = sorted(list(t1.replace(" ", "").lower())) == sorted(
        list(t2.replace(" ", "").lower()))
    return wynik
    # return True if sorted(list(t1.replace(" ", "").lower())) == \
    #    sorted(list(t2.replace(" ", "").lower())) else False


def main():
    """Glowna funkcja"""
    lst_text = ["Akta generała ma mała renegatka",
                " Kobyła ma mały bok", "Malajalam", "13431", "mariusz"]
    for t1 in lst_text:
        print(f"Czy: {check_palimdrom_v1(t1):33} jest palimdormem ? :{1}")

    lst_text = ["optyczny", "poczytny", "chityna",
                "hiacynt", "alergia", "galeria"]
    kombinacje = list(itertools.combinations(lst_text, 2))
    for kombinacja in kombinacje:
        print(f"Czy {kombinacja} jest anagramem ? ", end="")
        print(check_anagran_v2(kombinacja[0], kombinacja[1]))


main()
