import os
os.system("cls")

try:
    x = int(input("Wprowadź liczbę: "))
    y = 1 / x
    print(y)
except ZeroDivisionError:
    print("Nie możesz dzielić przez zero.")
except ValueError:
    print("Musisz wpisać wartość całkowitą.")
except KeyboardInterrupt:
    print("Zostało nacisniete Ctrl C")

print("KONIEC.")
