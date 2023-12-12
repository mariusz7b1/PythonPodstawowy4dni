#   Lista 01b Zadanie 1

liczba = int(input("Wprowadź dowolną liczbę całkowitą: "))
wynik = liczba ** 2
print(f"{liczba} podniesiona do potegi drugiej to {wynik}")
wynik = liczba ** 3
print(f"{liczba} podniesiona do potegi trzeciej to {wynik}")
wynik = liczba ** 4
print(f"{liczba} podniesiona do potegi czwartej to {wynik}")


#   Lista 01b Zadanie 2
liczba = float(input("Wprowadź dowolną liczbę rzeczywistą: "))
polowa = liczba / 2
print("Połowa wprowadzonej liczby to:", polowa)

#   Lista 01b Zadanie 3
liczba1 = int(input("Wprowadź dowolną liczbę całkowitą: "))
liczba2 = float(input("Wprowadź dowolną liczbę rzeczywistą: "))
suma = liczba1 + liczba2
print("Suma wprowadzonych liczb to:", suma)

#   Lista 01b Zadanie 4
tekst = input("Wprowadź dowolny ciąg znaków: ")
dlugosc = len(tekst)
print("Długość wprowadzonego ciągu znaków to:", dlugosc)

#   Lista 01b Zadanie 5
liczba = float(input("Wprowadź dowolną liczbę rzeczywistą: "))
zaokraglona = round(liczba)
print("Wartość wprowadzonej liczby zaokrąglona do najbliższej liczby\
       całkowitej to:", zaokraglona)

#   Lista 01b Zadanie 6
liczba1 = int(input("Wprowadź pierwszą liczbę całkowitą: "))
liczba2 = int(input("Wprowadź drugą liczbę całkowitą: "))
srednia = (liczba1 + liczba2) / 2
print("Średnia arytmetyczna wprowadzonych liczb to:", srednia)


#   Lista 01b Zadanie 7
liczba1 = int(input("Wprowadź pierwszą liczbę: "))
liczba2 = int(input("Wprowadź drugą liczbę: "))
liczba3 = int(input("Wprowadź trzecią liczbę: "))
najwieksza = max(liczba1, liczba2, liczba3)
najmniejsza = min(liczba1, liczba2, liczba3)
print("Największa wprowadzona liczba to:", najwieksza)
print("najmniejsza wprowadzona liczba to:", najmniejsza)
