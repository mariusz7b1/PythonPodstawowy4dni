"""
Przykładowa relizacja:
Zadanie 2c  z Laboratorium 03a
"""
from os import system
system('cls')


lst = []
for i in range(1, 11):
    lst.append(i**2)
    # lst.append(pow(i, 2))   # wykorzystanie funkcji 'pow'
print(lst)


for i in range(0, 10):
    if lst[i] % 2 == 0:
        lst[i] = lst[i]*-1

print(lst)
