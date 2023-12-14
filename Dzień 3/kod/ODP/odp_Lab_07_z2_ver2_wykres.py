""""wymaga posiadania zewnetrznego pakietu  
pip install matplotlib
import matplotlib
print(matplotlib.__version__)
(cmd)  pip install --upgrade matplotlib

"""
import matplotlib.pyplot as plt


def maluj_wykres(dane):
    # Etykiety dla legendy

    labels = [f'{i} ({p:.2f}%)' for i, p in dane.items()]
    dane = dane.values()
    # Rysuj wykres kołowy
    plt.pie(dane, labels=labels, autopct='%1.1f%%')
    # Dodaj legendę
    plt.legend(labels, title="Dane", loc="center left",
               bbox_to_anchor=(1, 0, 0.5, 1))
    # Pokaż wykres
    plt.show()


def sortuj_slow(war):
    return war[1]


def sortuj_list(war):
    return len(war)


def czysc_slowo(slowo):
    slowo = slowo.strip()
    while len(slowo) > 0 and not slowo[0].isalpha():
        slowo = slowo[1:]
    while len(slowo) > 0 and not slowo[-1].isalpha():
        slowo = slowo[:-1]
    slowo = slowo.lower()
    return slowo


def main():
    try:
        f_in = open('d:\\dane\\ksiazka.txt', 'rt', encoding='utf-8')
        f_out = open('d:\\dane\\raport2.txt', 'wt', encoding='utf-8')
    except Exception as e:
        print("Wystąpił błąd podczas próby otwarcia pliku.")
        print(f"Blad: {e}")
        exit()

    slownik_liter = {}
    list_slow = []

    # wczytuje kolejna linie
    linia = f_in.readline()
    # tak dlugo jak mam co czytac
    while len(linia) != 0:
        # zamieniam na male litery
        linia = linia.lower()
        # wycinam ewentualne spacje , choć split to zrobi ale :)
        linia = linia.strip()
        # po słowach w linii i jak dluższe niż 3 to dodaję do słownika
        for slowo in linia.split():
            slowo = czysc_slowo(slowo)
            if 3 <= len(slowo) <= 12 and slowo.isalpha():
                list_slow.append(slowo)
        # dla każdej litery w lini
        for litera in linia:
            # jeśli jest to litera
            if litera.isalpha():
                # jesli nowa to dodaj element słownika i ustal wartość na 1
                if litera not in slownik_liter:
                    slownik_liter[litera] = 1
                else:
                    # Inkrementujemy wartość litery o 1
                    slownik_liter[litera] += 1
        linia = f_in.readline()

    # Wyświetlamy procentową częstotliwość wystąpienia każdej litery
    calkowita_liczba_liter = sum(slownik_liter.values())

    # Sortowanie po wartościach
    # lista_liter = sorted(slownik_liter.items(), \
    # key=lambda x: x[1], reverse=True)
    lista_liter = sorted(slownik_liter.items(), key=sortuj_slow, reverse=True)

    # Wyświetlamy statystykę
    wynik = {}
    for litera, liczba_wystąpień in lista_liter:
        procent = 100 * liczba_wystąpień / calkowita_liczba_liter
        str1 = f"Litera {litera}:{liczba_wystąpień} {procent:.2f}%"
        if procent >= 3:
            wynik[litera] = procent
        print(str1)
        f_out.write(str1 + "\n")
    wynik["reszta"] = 100 - sum(wynik.values())

    str1 = f"Calkowita_liczba_liter w tekscie: {calkowita_liczba_liter}"
    print(str1)
    f_out.write(str1 + "\n")

    lista_slow_unik = list(set(list_slow))
    str1 = f"Ilosc unikalnych slow: {len(lista_slow_unik)}"
    print(str1)
    f_out.write(str1 + "\n")

    # Sortowanie po dlugosci słow
    lista_slow_unik.sort(key=len, reverse=True)
    # lista_slow_unik.sort(key=sortuj_list, reverse=True)
    najdluzsze = len(lista_slow_unik[0])
    licznik = 1
    while len(lista_slow_unik[licznik]) == najdluzsze:
        licznik += 1

    str1 = f"najdłuższe słowo ma {najdluzsze} i  takich słów jest {licznik}"
    print(str1)
    f_out.write(str1 + "\n")

    f_in.close()
    f_out.close()
    maluj_wykres(wynik)


main()
