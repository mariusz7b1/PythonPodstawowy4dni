"""  wersja z Buforem (przerobiona wersja 2)"""

# Definiowanie samogłosek
SAMOGLOSKI = "aeiouyAEIOUY"
# Bufor na wczytywane znaki
BUFOR = 100


def main():
    # scieżka i nazwy plików
    in_file_name = "testowy.txt"
    file_path = "d:\\dane\\"

    try:
        # otwarcie pliku do odczytu
        f_in = open(file_path + in_file_name, "rt", encoding="utf-8")
    except IOError:
        print("Nie udało się otworzyć pliku do odczytu")
        exit()

    liczba_a = 0
    rozne_znaki = set()
    liczba_samoglosek = 0

    while True:
        tekst = f_in.read(BUFOR)
        if not tekst:
            break

        liczba_a += tekst.count('a')
        rozne_znaki.update(tekst)

        for samogloska in SAMOGLOSKI:
            liczba_samoglosek += tekst.count(samogloska)

    print("Liczba wystąpień litery 'a':", liczba_a)
    print("Liczba różnych znaków:", len(rozne_znaki))
    print("Liczba wystąpień samogłosek:", liczba_samoglosek)

    f_in.close()

    # Otwarcie pliku do zapisu
    with open("d:\\dane\\raport1-c.txt", "wt", encoding="utf-8") as plik_raport:
        plik_raport.write(f"Liczba wystąpień litery 'a': {liczba_a}\n")
        plik_raport.write(f"Liczba różnych znaków: {len(rozne_znaki)}\n")
        plik_raport.write(f"Liczba wystąpień samogłosek: {liczba_samoglosek}\n")


main()
