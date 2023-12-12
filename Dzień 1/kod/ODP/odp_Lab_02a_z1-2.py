# Zadanie 1
liczba = int(input("Podaj liczbę: "))
if liczba % 2 == 0:
    print("Liczba parzysta")
else:
    print("Liczba nieparzysta")

# Zadanie 2
liczba1 = int(input("Podaj pierwszą liczbę: "))
liczba2 = int(input("Podaj drugą liczbę: "))
liczba3 = int(input("Podaj trzecią liczbę: "))
if liczba1 > liczba2 and liczba1 > liczba3:
    print("Największa liczba to:", liczba1)
elif liczba2 > liczba1 and liczba2 > liczba3:
    print("Największa liczba to:", liczba2)
else:
    print("Największa liczba to:", liczba3)
