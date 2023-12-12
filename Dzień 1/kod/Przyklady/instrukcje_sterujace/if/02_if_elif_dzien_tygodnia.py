"""
Przykłady ilustrujące wykorzystanie instrujci if elif i else
"""
import os
os.system("cls")

print("Podaj dzień tygodnia gdzie ")
print("1 - to poniedziałek a 7 to niedziela ")

day_number = int(input(" ? "))  # podana warosc konwertuje na int
if day_number == 1:
    print("Poniedziałek")
elif day_number == 2:
    print("Wtorek")
elif day_number == 3:
    print("Środa")
elif day_number == 4:
    print("Czwartek")
elif day_number == 5:
    print("Piątek")
elif day_number == 6:
    print("Sobota")
elif day_number == 7:
    print("Niedziela")
else:
    print("Nieprawidłowy numer dnia tygodnia.")
