"""
pliki - tradycyjna obsługa otwórz / zamknij
"""

from os import system
from sys import exit
system("cls")

# odczyt z pliku

in_file_name = "testowy.txt"
out_file_name = "slowa_z_pliku.txt"
file_path = "d:\\dane\\"     # "d:\dane\"

try:
    # otwarcie pliku do odczytu
    f_in = open(file_path + in_file_name, "rt", encoding="utf-8")
except IOError:
    print("Nie udało się otworzyć pliku do odczytu")
    exit()

try:
    # otwarcie pliku do zapisu
    f_out = open(file_path + out_file_name, "wt", encoding="utf-8")
except IOError:
    print("Nie udało się otworzyć pliku do zapisu")
    f_in.close()  # nie jest to konieczne
    exit()

f_out.write("To jest moj plik ze słowami" + "\n\n")
while True:
    # odczyt za posrednictewm readline
    linia = f_in.readline()
    if len(linia) == 0:
        break
    else:
        # przykład
        lista_slow = linia.split()
        for slowo in lista_slow:
            # zapis za posrednictwem write
            f_out.write(slowo + "\n")

f_in.close()
f_out.close()
