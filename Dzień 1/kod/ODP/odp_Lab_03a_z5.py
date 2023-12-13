"""
Przykładowa relizacja:
Zadanie 5  z Laboratorium 03a
"""
import os
os.system("cls")

DNI_TYGODNIA = ['Poniedziałek', 'Wtorek', 'Środa',
                'Czwartek', 'Piątek', 'Sobota', 'Niedziela']


print("Podaj dzień tygodnia gdzie ")
print("1 - to poniedziałek a 7 to niedziela ")
dzien_tygodnia = int(input(" ? "))  # podana warosc konwertuje na int

if 1 <= dzien_tygodnia <= 7:
    print(DNI_TYGODNIA[dzien_tygodnia-1])
else:
    print("Nieprawidłowy numer dnia tygodnia.")
