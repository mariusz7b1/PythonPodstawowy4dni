# Zadanie 6
punkty = int(input("Podaj liczbę punktów: "))
if punkty < 50:
    print("Ocena niedostateczna")
elif punkty < 70:
    print("Ocena dostateczna")
elif punkty < 90:
    print("Ocena dobra")
else:
    print("Ocena bardzo dobra")

# Zadanie 7
a = int(input("Podaj długość pierwszego boku: "))
b = int(input("Podaj długość drugiego boku: "))
c = int(input("Podaj długość trzeciego boku: "))
if a == b == c:
    print("Trójkąt równoboczny")
elif a == b or b == c or c == a:
    print("Trójkąt równoramienny")
else:
    print("Trójkąt różnoboczny")

# Zadanie 8
dzien = int(input("Podaj numer dnia tygodnia: "))
if dzien == 1:
    print("Poniedziałek")
elif dzien == 2:
    print("Wtorek")
elif dzien == 3:
    print("Środa")
elif dzien == 4:
    print("Czwartek")
elif dzien == 5:
    print("Piątek")
elif dzien == 6:
    print("Sobota")
else:
    print("Niedziela")

# Zadanie 9
miesiac = int(input("Podaj numer miesiąca: "))
if miesiac == 1:
    print("Styczeń")
elif miesiac == 2:
    print("Luty")
elif miesiac == 3:
    print("Marzec")
elif miesiac == 4:
    print("Kwiecień")
elif miesiac == 5:
    print("Maj")
elif miesiac == 6:
    print("Czerwiec")
elif miesiac == 7:
    print("Lipiec")
elif miesiac == 8:
    print("Sierpień")
elif miesiac == 9:
    print("Wrzesień")
elif miesiac == 10:
    print("Październik")
elif miesiac == 11:
    print("Listopad")
else:
    print("Grudzień")

# Zadanie 10
stan_cywilny = input("Podaj swój stan cywilny: ")
if stan_cywilny.lower() == "kawaler" or stan_cywilny.lower() == "panna":
    print("Jesteś osobą wolną")
elif stan_cywilny.lower() == "żonaty" or stan_cywilny.lower() == "zamężna":
    print("Jesteś osobą zamężną")
else:
    print("Nie rozpoznano stanu cywilnego")
