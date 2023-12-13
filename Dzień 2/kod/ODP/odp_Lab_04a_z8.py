def read_int(prompt, minimum, maksimum):
    while True:
        wartosc = input(prompt)
        if not wartosc.isdigit():
            print("podaj liczbę !!!! złożoną z cyfr ")
        else:
            wartosc = int(wartosc)
            if wartosc < minimum or wartosc > maksimum:
                print(
                    f"zły zakres !!! Podaj liczbę od {minimum} do {maksimum}")
            else:
                break
    return wartosc


def zadanie_4a(n):
    linia = ""
    for y in range(0, n):
        for x in range(0, n):
            linia += "*"
        print(linia)
        linia = ""
    print("\n\n")


def zadanie_4b(n):
    linia = ""
    for y in range(0, n):
        for x in range(0, n):
            if y == 0 or y == n - 1:
                linia += "*"
            else:
                if x == 0 or x == n - 1:
                    linia += "*"
                else:
                    linia += " "
        print(linia)
        linia = ""
    print("\n\n")


def zadanie_4c(n):
    linia = ""
    for y in range(0, n):
        for x in range(0, n):
            if y == 0 or y == n - 1:
                linia += "*"
            else:
                if x == 0 or x == n - 1 or x == y:
                    linia += "*"
                else:
                    linia += " "
        print(linia)
        linia = ""
    print("\n\n")


def zadanie_4d(n):
    linia = ""
    for y in range(0, n):
        for x in range(0, n):
            if y == 0 or y == n - 1:
                linia += "*"
            else:
                if x == 0 or x == n - 1 or x == y or x == n - 1 - y:
                    linia += "*"
                else:
                    linia += " "
        print(linia)
        linia = ""
    print("\n\n")


def zadanie_4e(n):
    linia = ""
    for y in range(0, n):
        for x in range(0, n):
            if y % 2 == 0:
                linia += "*" if x % 2 == 0 else " "
            elif y % 2 != 0:
                linia += "*" if x % 2 != 0 else " "
        print(linia)
        linia = ""
    print("\n\n")


def main():
    while True:
        print("powiedz mi co chcesz zrobić :) ? ")
        print("1 -  pełny kwadrat")
        print("2 -  kwadrat")
        print("3 -  kwadrat z przekatną")
        print("4 -  kwadrat z z dwoma przekatnymi")
        print("5 -  szachownica")
        print("9 - zakonczenie programu")
        wybor = read_int("Jaki jest twój wybor ? ", 1, 9)
        if wybor == 9:
            break

        wielkosc = read_int("Podaj wielkosc kwadratu ? ", 4, 25)
        if wybor == 1:
            zadanie_4a(wielkosc)
        if wybor == 2:
            zadanie_4a(wielkosc)
        if wybor == 3:
            zadanie_4c(wielkosc)
        if wybor == 4:
            zadanie_4d(wielkosc)
        if wybor == 5:
            zadanie_4e(wielkosc)

    tekst = "Dziękuje bardzo za współprace"
    print("*" * (len(tekst) + 2))
    print(f"*{tekst}*")
    print("*" * (len(tekst) + 2))


if __name__ == "__main__":
    main()
