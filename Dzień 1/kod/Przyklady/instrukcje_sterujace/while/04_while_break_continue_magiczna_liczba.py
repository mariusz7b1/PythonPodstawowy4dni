from os import system
system('cls')
# podanie magicznej liczby konczy dzialanie. Ale czy tylko ?
# Przeanalizuj kod i zastanow się jak działa program

magiczna_liczba = 0
while magiczna_liczba != 33:

    magiczna_liczba = int(input("podaj magiczną liczbę :) "))

    if magiczna_liczba == 99:
        continue
    if magiczna_liczba % 66 == 0:
        break

    print(magiczna_liczba)
else:
    print("Podałeś magiczną liczbę ")

print("Koniec petli")
