"""
Listy - kopiowanie
"""
import os
os.system("cls")

lst1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]            # Tworzenie listy

# kopiowanie list - ale czy napewno
lst2 = lst1
print(lst1)
print(lst2)
del lst1[1:-1]
print(lst1)
print(lst2)

if id(lst1) == id(lst2):
    print("lst1 i lst2 to dwie różne nazwy tej samej listy ")

lst1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
lst3 = lst1[:]
print(lst1)
print(lst3)
del lst1[1:-1]
print(lst1)
print(lst3)

if id(lst1) == id(lst3):
    print("lst1 i lst3 to dwie różne nazwy tej samej listy ")
else:
    print("teraz sa rozne")


# kopiowanie list 2
lst1 = list("Ala ma kota i kot nie ma ali")
lst4 = lst1.copy()
print(lst1)
print(lst4)
del lst1[3:-3]
print(lst1)
print(lst4)

if id(lst1) == id(lst4):
    print("lst1 i lst4 to dwie różne nazwy tej samej listy ")
else:
    print("teraz sa rozne")
