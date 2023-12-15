""" Rozwiazanie """
# importowanie modułow
import sys
import json
from os import system


def get_miasto(adres):
    """"
    Wycina z adresu miasto korzrzystajac z tego ze po przecinku
    zawsze jest kod o stałej dlugości 
    Args:
        adres 
    Returns:
        miasto
    """
    lst_adres = adres.split(",")
    miasto = lst_adres[1]
    miasto = miasto[7:]

    return miasto


def get_mail(mail):
    """"
    Wycina z adresu @ dostawce, 
    używa split traktujac jako separator znaczek @

    Args:
        adres mail
    Returns:
        dostawca
    """
    return mail.split("@")[1]


def raport_anomalii(sciezka, lista_anomalii):
    """
    zapisuje raport anomalii
    """
    try:
        # zrobić scieżkę
        with open(sciezka + 'raport_anomali.txt', "wt", encoding="utf-8") as f_out:
            f_out.writelines(lista_anomalii)   # zapisuje liste do pliku
    except IOError:
        print("Error zapisu anomalii")


def get_data_fromfile(sciezka, plik):
    """Pobiera dane z pliku, zwraca listę ktorej elementami jest słownik"""
    try:
        f_in = open(sciezka + plik, 'rt', encoding='utf-8')
    except IOError:
        print('Brak pliku z danymi zrodłowymi')
        sys.exit()

    dane = []
    anomalie = ["Te linie są niezgodne z formatem:\n"]
    linia = f_in.readline()
    # traktuję pierwszą linię jako wzorcową jeśli chodzi o ilość danych
    # rozdzielonych separatorem, jesli trafi się jakaś linia o innej dlugości
    # bedzie ignorowana
    dane_linia = linia.split(";")
    ilosc_danych = len(dane_linia)

    while linia != '':
        linia = linia.strip()
        dane_linia = linia.split(";")
        if len(dane_linia) == ilosc_danych:  # tylko wlasciwe linie
            imie = dane_linia[0]
            nazwisko = dane_linia[1]
            miasto = get_miasto(dane_linia[4])
            dostawca_mail = get_mail(dane_linia[8])
            dane_wrazliwe = {"pesel": dane_linia[2], "nip": dane_linia[3]}
            # Tworzenie słownika i dodanie do tablicy
            dane.append({"imie": imie,
                        "nazwisko": nazwisko,
                         "miasto": miasto,
                         "dostawca_mail": dostawca_mail,
                         "dane_wrazliwe": dane_wrazliwe})
        else:
            # Anomalie
            anomalie.append(linia + "\n")
        linia = f_in.readline()
    f_in.close()
    raport_anomalii(sciezka, anomalie)

    return dane


def save_date_to_file(sciezka_do_pliku, nazwa_pliku, slownik):
    """
    zapisuje klucze slownika do pliku 
    """
    nazwa_pliku = sciezka_do_pliku + nazwa_pliku + ".txt"
    with open(nazwa_pliku, "wt", encoding="utf-8") as f_out:
        for wartosc in slownik.keys():
            f_out.write(wartosc + "\n")


def get_dic_unique_data(dane, nazwa_klucza):
    """
    na podstawie danych i otrzymanego klucza tworzy slownik
    gdzie kluczem jest unikatowa wartosc ze slonika dane
    a wartoscia ilosc wystapien
    """
    slownik = {}
    for element in dane:
        wartosci = element[nazwa_klucza]
        if wartosci not in slownik:
            slownik[wartosci] = 1
        else:
            slownik[wartosci] += 1
    return slownik


def get_most_popolar(slownik, minmax=0):
    """ zwraca liste z najbardziej popoularna wartoscia
        jesli parametr minmax > 0 to najmniej popularna wartosć
    """
    if minmax == 0:
        wartosc_maks = max(slownik.values())
    else:
        wartosc_maks = min(slownik.values())
    # przewiduje sytuacje ze moze być kilka najmniej/najbardziej popularnych
    # dlatego roboczo tworze liste lst
    lst = []
    for klucz in slownik.keys():
        if slownik[klucz] == wartosc_maks:
            lst.append({klucz: slownik[klucz]})
    return lst


def count_var_in_dic(slownik, var):
    """
    zwraca ilość wystapien danej wartości
    """
    if var in slownik.keys():
        return slownik[var]

    return 0


def zapisz_json(plik, dane):

    with open(plik, "w", encoding="utf-8") as plik_json:
        json.dump(dane, plik_json, ensure_ascii=False, indent=4)


def main():
    system("cls")

    nazwa_pliku = "dane10K.txt"
    sciezka_do_pliku = "d:\\dane\\inne\\"

    # pobranie danych do tablicy
    lst_dane = get_data_fromfile(sciezka_do_pliku, nazwa_pliku)
    zapisz_json(sciezka_do_pliku + "dane_wybrane.json", lst_dane)

    # utworzenie slownika z imionami i czestością ich
    dic_imion = get_dic_unique_data(lst_dane, 'imie')
    save_date_to_file(sciezka_do_pliku, "imiona", dic_imion)

    dic_nazwisk = get_dic_unique_data(lst_dane, 'nazwisko')
    save_date_to_file(sciezka_do_pliku, "nazwisko", dic_nazwisk)

    dic_miasto = get_dic_unique_data(lst_dane, 'miasto')
    save_date_to_file(sciezka_do_pliku, "miasto", dic_miasto)

    dic_mail = get_dic_unique_data(lst_dane, 'dostawca_mail')
    save_date_to_file(sciezka_do_pliku, "mail", dic_mail)

    print("Liczba różnych imion to  ", len(dic_imion))
    print("Liczba różnych nazwisk to", len(dic_nazwisk))
    print("Liczba różnych miast   to", len(dic_miasto))
    print("Liczba różnych dostawców @ to", len(dic_mail))

    polularne_imie = get_most_popolar(dic_imion)
    polularne_nazwisko = get_most_popolar(dic_nazwisk)
    polularne_miasto = get_most_popolar(dic_miasto)
    polularny_dostawca = get_most_popolar(dic_mail)

    print("najbardziej popularne imie/imiona to:", polularne_imie)
    print("najbardziej popularne nazwisko/nazwiska to:", polularne_nazwisko)
    print("najbardziej popularne miasto/miasta to:", polularne_miasto)
    print("najbardziej popularny dostawca @ to :", polularny_dostawca)

    polularne_imie = get_most_popolar(dic_imion, 1)
    polularne_miasto = get_most_popolar(dic_miasto, 1)

    print("najmniej popularne imie/imiona to:", polularne_imie)
    print("najmniej popularne miasto/miasta to:", polularne_miasto)

    print(f"w Opolu mieszka {count_var_in_dic(dic_miasto, "Opole")} mieszkancow")


if __name__ == '__main__':
    main()
    print(" !!!!!!!!!!!! KONIEC")
