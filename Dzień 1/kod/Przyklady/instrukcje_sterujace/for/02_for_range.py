"""
Przykłady ilustrujące wykorzystanie for i range
"""

from os import system
system('cls')

print("Przyklad 1")
# i = 0 do i < 10  czyli od 0 do 9
for i in range(10):
    print(i, end="-")


pass
print("\nPrzyklad 2")
for i in range(1, 21):
    if i % 2 == 0:      # liczba parzysta
        print(i)

print("\nPrzyklad 3")
for i in range(1, 21, 2):   # 1,3,5   ....
    if i % 2 == 0:          # liczba parzysta
        print(i)            # Czyli nigdy tu się nie znajdziemy
else:
    print("Skonczyłem działać")


print("\nPrzyklad 4")
for i in range(1, 10):
    if i == 5:
        break
    if i == 2:
        continue
    print(i)

print(i)

print("\nPrzyklad 5")
for i in range(-3, -10, -2):  # od do liczby ujemne
    print(i)
