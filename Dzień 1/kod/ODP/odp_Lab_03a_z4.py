"""
Przykładowa relizacja:
Zadanie 4  z Laboratorium 03a
"""
from os import system
system('cls')


lst = [15, 6, 4, 2, 1, 88, 6, 7, 9, 11]
print(lst)

# a
lst2 = lst[1:]+lst[0:1]
print(lst2)

# b
lst3 = lst[-1:]+lst[0:-1]
print(lst3)

# c
lst4a = lst.copy()
lst4a.reverse()
# alternatywnie
lst4b = lst[::-1]
print(lst4a)
print(lst4a)

# d
lst5 = []
for ele in lst:
    if ele % 2 == 0:
        lst5.append(ele)
print(lst5)

# e
lst6 = []
for i in range(0, len(lst), 2):
    if lst[i] % 2 != 0:
        lst6.append(lst[i])
print(lst6)
