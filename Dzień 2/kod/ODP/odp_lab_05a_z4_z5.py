"""
Przykładowe rozwiązanie zadania 5.4 i 5.5
"""
from os import system
system('cls')


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


def read_float(prompt, minimum, maximumu):
    prompt = f"{prompt} z zakresu od {minimum}  do {maximumu} "
    while True:
        try:
            wartosc = float(input(prompt))
        except ValueError:
            print("podaj liczbę !!!! złożoną z cyfr i maksymalknie jednej . ")
        except KeyboardInterrupt:
            print(" Nic z tego  :)")
        else:
            if wartosc < minimum or wartosc > maximumu:
                print(f"zły zakres !!! Podaj liczbę od {
                      minimum} do {maximumu}")
            else:
                break
    return wartosc


def main():
    print(read_int("Podaj liczbę całkowitą", 1, 5))
    print(read_float("Podaj liczbę rzeczywistą", 1, 5))


if __name__ == "__main__":
    main()
