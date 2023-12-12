"""
Lista 01a Zadanie 5
"""
# czysci ekran
from os import system
system('cls')


x = float(input("Wprowadź wartość dla x: "))
y = 1 / (x + (1 / (x+(1/(x+1/x)))))
print("y =", y)
input()
