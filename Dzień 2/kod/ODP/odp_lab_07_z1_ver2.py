"""Rozwiązanie zadania 7a.1 wersja tradycyjna"""
# Definiowanie samogłosek
from sys import exit as exit_prog
SAMOGLOSKI = "aeiouyAEIOUY"


def main():
    in_file_name = "testowy.txt"
    file_path = "d:\\dane\\"

    try:
        # otwarcie pliku do odczytu
        f_in = open(file_path + in_file_name, "rt", encoding="utf-8")
    except IOError:
        print("Nie udało się otworzyć pliku do odczytu")
        exit_prog()

    tekst = f_in.read()
    liczba_a = tekst.count('a')
    rozne_znaki = set(tekst)

    liczba_samoglosek = 0
    for samogloska in SAMOGLOSKI:
        liczba_samoglosek += tekst.count(samogloska)

    # Otwarcie pliku do zapisu
    with open("d:\\dane\\raport1-b.txt", "wt", encoding="utf-8") as plik_raport:
        plik_raport.write(f"Liczba wystąpień litery 'a': {liczba_a}\n")
        plik_raport.write(f"Liczba różnych znaków: {len(rozne_znaki)}\n")
        plik_raport.write(f"Liczba wystąpień samogłosek: {liczba_samoglosek}\n")


main()
