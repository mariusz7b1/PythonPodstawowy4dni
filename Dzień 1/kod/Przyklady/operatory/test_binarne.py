import os
import time

os.system("cls")
x = int(input("Podaj pierwszą liczbę: "))
y = int(input("Podaj drugą liczbę: "))

print(f"{x} & {y} czyli {bin(x)} & {bin(y)}= { x & y}")  # binarne AND
print(f"{x} | {y} czyli {bin(x)} | {bin(y)}= { x | y}")  # binarne OR
print(f"{x} ^ {y} czyli {bin(x)} ^ {bin(y)}= { x ^ y}")  # binarne XOR

print(f"Przesuniecie w prawo o 1 'y >> 1' {y >> 1}")
print(f"Przesuniecie w lewo  o 1 'y <<1' {y << 1}")
x = input("Naciśnij enter aby zakonczyć")
time.sleep(2)
