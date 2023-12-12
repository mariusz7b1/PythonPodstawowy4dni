# Zadanie 5
rok = int(input("Podaj rok: "))
if rok % 4 == 0 and (rok % 100 != 0 or rok % 400 == 0):
    print("Rok przestępny")
else:
    print("Rok nieprzestępny")
