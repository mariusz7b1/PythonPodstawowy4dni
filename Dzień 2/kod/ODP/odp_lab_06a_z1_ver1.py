"""
Przykładowe rozwiązanie zadania 6.1 ver1
"""
from random import randint
from os import system


def read_int(prompt, minimum, maximum):
    prompt = f"{prompt} z zakresu od {minimum}  do {maximum} "
    while True:
        try:
            wartosc = int(input(prompt))
        except ValueError:
            print("podaj liczbę !!!! złożoną z cyfr ")
        except KeyboardInterrupt:
            print(" Nic z tego  :)")
        else:
            if wartosc < minimum or wartosc > maximum:
                print(f"zły zakres !!! Podaj liczbę od {minimum} do {maximum}")
            else:
                break
    return wartosc


def liczby_losowe(n, od=1, do=10) -> None:
    liczby = [0] * 11
    for i in range(n):
        liczba = randint(od, do)
        liczby[liczba] += 1
    for i in range(1, 11):
        print("Liczba", i, "wystąpiła: ",
              round(liczby[i] / n * 100, 2), "%")


def main() -> None:
    system("cls")
    liczby_losowe(read_int("Podaj liczbę z zakresu 1 - 10000", 1, 10000))


if __name__ == "__main__":
    main()
