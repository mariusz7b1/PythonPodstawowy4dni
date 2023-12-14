"""Demonstracja __doc__"""
from os import system
system("cls")
SAMOGLOSKI = tuple("aeiouyAEIOUY")


def przywiatnie_pythona(napis="Cześć nazywam się Python :) ") -> None:
    """
    PEP257
    Funkcja pyta o imie, sprawdza czy imie jest dluższe od 2 znaków
            i czy sklada się z samych liter.

    Args:
        napis (str): opcjonalny, treść powitania
    Returns:
        str: podane imię
    """

    print(napis)
    imie = ""
    mnoznik = 1
    while not imie.isalpha() or len(imie) <= 2:
        znak = '?' * mnoznik
        imie = input(f"A jak ty masz na imię {znak} ")
        mnoznik += 2
        if mnoznik > 8:
            print("ROZUMIESZ O CO  CIE PYTAM !!!! ")
    return imie


def kobieta_czy_mezczyzna(imie):
    """
    Funkcja sprawdza pleć na podstawie imienia
    jako argument przyjmuje imie, Sprawdza czy ostatnia litera to 'a' lub 'A'

    Args:
            imie (str): imię

    Returns:
            str: zwraca K lub M
    """
    if imie[-1] == 'a' or imie[-1] == 'A':
        return 'K'
    else:
        return 'M'


def odmiana_zenskiego_imienia(imie):
    """
    Funkcja jako argument przyjmuje imie żeńskie.
    dokonuje odmiany na bazie kryterium przedostatniej litery
    zamienia pierwsza litere na wielką
        Args:
                imie (str): imię żeńskie

        Returns:
                str: zwraca odmienione imię
        """

    przed_ostatnia = imie[-2]
    if przed_ostatnia in SAMOGLOSKI:
        imie = imie[0:-1] + 'u'
    else:
        imie = imie[0:-1] + 'o'
    imie = imie[0].upper() + (imie[1:]).lower()
    return imie


def main() -> None:
    imie_kursanta = przywiatnie_pythona()
    if kobieta_czy_mezczyzna(imie_kursanta) == 'K':
        print(
            f"Miło cię powitać {odmiana_zenskiego_imienia(imie_kursanta)} :)")
    else:
        print(f"Cześć {imie_kursanta.upper()} !!!")

    input("Naciśnij Enter aby kontynuować")


if __name__ == "__main__":
    # main()
    print(odmiana_zenskiego_imienia.__doc__)
    print(kobieta_czy_mezczyzna.__doc__)
    print(przywiatnie_pythona.__doc__)


# np:
# python -m pydoc math
