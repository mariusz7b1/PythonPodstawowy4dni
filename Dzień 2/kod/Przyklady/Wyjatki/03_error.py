import os
os.system("cls")

try:
    x = float(input("Wprowadź liczbę: "))
    y = 1 / x
    print(y)
except Exception as e:
    print("Pojawił się bład ", e)

print("KONIEC.")
