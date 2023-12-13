# testowanie f string
liczba_1 = 2
liczba_2 = 10

s2 = f"liczba {liczba_1} podniesiona do potegi {liczba_2} to ? "
wynik = int(input(s2))
if wynik == pow(liczba_1, liczba_2):
    print("Hurra zdales")
else:
    s1 = f" BLAD !!! liczba {liczba_1} podniesiona do potegi {liczba_2} wynosi\
        {pow(liczba_1,liczba_2)}"
    print(s1)
