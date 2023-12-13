"""
pliki - obsługa w wykorzystaniem with ()
"""
from os import system
system("cls")

# odczyt z pliku
in_filename = "testowy.txt"
file_path = "d:\\dane\\"

try:
    with open(file_path+in_filename, "r", encoding="utf-8") as f_in:
        for linia in f_in:
            print(linia)
except IOError:
    print("Wystąpił błąd podczas odczytu pliku.")


try:
    with open(file_path+in_filename, "r", encoding="utf-8") as f_in:
        tekst = f_in.read()
        tekst = tekst.splitlines()   # zwraca liste lini z tekstu
        for linijka in tekst:
            print(linijka)
except IOError:
    print("Wystąpił błąd podczas odczytu pliku.")
