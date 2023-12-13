"""
Przykładowa relizacja:
Zadanie 7  z Laboratorium 03a
"""
liczby = [10, 20, 30, 40, 50]
index = int(input("Podaj indeks: "))
nowa_wartosc = int(input("Podaj nową wartość: "))
if 0 <= index < len(liczby):
    liczby[index] = nowa_wartosc
    print(liczby)
else:
    print("Podany indeks jest poza zakresem.")
