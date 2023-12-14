"""Przykłady słowniki"""


def main():
    in_file_name = "baza.txt"
    file_path = "d:\\dane\\"
    # operuje na małych literach
    lista_ludzi = []

    try:
        file_in = open(file_path + in_file_name, "rt", encoding="utf-8")
    except Exception as e:
        print("Wystąpił błąd podczas odczytu pliku.")
        print(f"Blad: {e}")
        exit()

    naglowek = (file_in.readline().strip()).split(";")
    while True:
        linia = file_in.readline().strip()
        if linia == "":
            break
        dane_z_lini = linia.split(";")
        rekord = {}
        rekord = dict.fromkeys(naglowek)
        for i in range(len(naglowek)):
            rekord[naglowek[i]] = dane_z_lini[i]

        lista_ludzi.append(rekord)


if __name__ == "__main__":
    main()
    print("Koniec działania programu")
