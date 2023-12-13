import os
os.system("cls")


def pokaz_arumenty(*args) -> None:
    """
    PEP257
    Funkcja wypisuje otrzymany argumenty na ekranie

    Args:
    Returns:
        NONE
    """
    print(type(args))
    print(f"Przekazano {len(args)} argumentów")
    for war in args:
        print(war, end=",")


def zwroc_wartosc(war1: int) -> int:
    """
    W Pythonie można użyć adnotacji (ang. annotations)
    do wskazania oczekiwanego typu ale nie wpływa wykonywanie kodu
    Adnotacje są zatem informacjami dla programisty, a nie wymogiem
    """
    print(type(war1))
    if isinstance(war1, int):
        return war1
    else:
        return "TEST"


def modyfikuj_liste(lista):
    print(id(lista))
    lista[-1] = 999


def obsluguj_argumenty(*args, **kwargs):
    # print(a, b)
    print("Argumenty pozycyjne:", args)
    print("Argumenty nazwane:", kwargs)


def main() -> None:

    #    print(zwroc_wartosc(4.4))
    lst1 = [1, 2, 3, 4, 5]

    pokaz_arumenty("ala", 1, 2.7, lst1)
    print("\n\n")
    obsluguj_argumenty(1, 2, 3, imie="Jan", nazwisko="Kowalski")

    print(lst1)
    print(id(lst1))
    modyfikuj_liste(lst1)
    print(lst1)

    a = 10
    pokaz_arumenty(a)

    pokaz_arumenty(lst1)
    print()

    pokaz_arumenty(*lst1)
    print()


if __name__ == "__main__":
    print(__name__)
    main()
