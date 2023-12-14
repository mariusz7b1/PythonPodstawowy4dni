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


def liczby_losowe(n, od=1, do=10):

    lst = [randint(od, do) for i in range(n)]
    wynik = [(lst.count(i)) for i in range(od, do + 1)]

    # print(len(lst))
    # print(wynik)
    # print(sum(wynik))

    print(f"Przetestowano {n} liczb z zakresu {od} {do}")
    print("wyniki zamieszczono w poniższej tabeli")
    wynik_proc = [((wynik[i] / n * 100)) for i in range(do)]

    for i in range(od, do + 1):
        print(f"{i:4} wystapiło {wynik_proc[i - 1]:>6.2f} % ")


def main() -> None:
    system("cls")
    liczby_losowe(read_int("Podaj liczbę z zakresu 1 - 10000", 1, 10000))


if __name__ == "__main__":
    main()
