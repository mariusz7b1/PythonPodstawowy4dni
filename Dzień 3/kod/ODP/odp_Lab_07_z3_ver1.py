""" Przykadowe rozwiazanie zadania 7.3"""


def main():
    in_file_name = "dane_01.txt"
    out_file_nama = "imiona.txt"
    file_path = "d:\\dane\\"

    # operuje na małych literach
    szukane_imie = "ewa"
    try:
        with open(file_path + in_file_name, "rt", encoding="utf-8") as file:
            ilosc_wystapien_imienia = 0
            lista_imion = []
            for linia in file:
                dane = linia.split(";")
                imie = dane[0].lower()
                if imie not in lista_imion:
                    lista_imion.append(imie)
                if imie == szukane_imie:
                    ilosc_wystapien_imienia += 1
        print(
            f"Imię {szukane_imie.title()} wystąpiło \
                {ilosc_wystapien_imienia} razy")
    except Exception as e:
        print("Wystąpił błąd podczas odczytu pliku.")
        print(f"Blad: {e}")
        exit()

    try:
        with open(file_path + out_file_nama, "wt", encoding="utf-8") as file:
            for imie in lista_imion:
                file.write(f"{imie.title()}" + "\n")
    except IOError:
        print("Wystąpił błąd podczas zapisu do pliku.")


if __name__ == "__main__":
    main()
    print("Koniec działania programu")
