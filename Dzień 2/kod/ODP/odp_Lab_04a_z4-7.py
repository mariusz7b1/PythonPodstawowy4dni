
# Zadanie 4

def cyfry_w_liczbie(n):
    lst = [int(cyfra) for cyfra in str(n)]
    return lst

# Zadanie 4 klasycznie


def cyfry_w_liczbie2(n):
    lst = []
    s1 = str(n)
    for zm1 in s1:
        lst.append(int(zm1))
    return lst


# Zadanie 5


def srednia(*args):
    if len(args) == 0:
        return None
    else:
        return sum(args) / len(args)


# Zadanie 6


def pierwsze_n(n):
    liczby_pierwsze = []  # pusta lista na przechowanie liczb pierwszych
    i = 2  # zaczynamy od 2, która jest najmniejszą liczbą pierwszą

    while len(liczby_pierwsze) < n:  # pętla wykonuje się dopóki nie znajdziemy n liczb pierwszych
        jest_pierwsza = True  # zakładamy na początku, że i jest liczbą pierwszą

        for p in liczby_pierwsze:  # sprawdzamy wszystkie już znalezione liczby pierwsze
            if i % p == 0:  # jeżeli i jest podzielne przez p
                jest_pierwsza = False  # to nie jest liczbą pierwszą
                break  # i nie musimy sprawdzać dalszych liczb

        if jest_pierwsza:  # jeżeli i jest liczbą pierwszą
            liczby_pierwsze.append(i)  # dodajemy i do listy liczb pierwszych

        i += 1  # przechodzimy do następnej liczby

    return liczby_pierwsze  # zwracamy znalezione liczby pierwsze


# Zadanie 7

def suma_kwadratow(*args):
    return sum(x**2 for x in args)


def main():
    print(cyfry_w_liczbie(321323))
    l_pier = pierwsze_n(30)
    print(l_pier)
    print(srednia(*l_pier))
    print(suma_kwadratow(*l_pier))


main()
