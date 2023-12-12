"""
Listy - podstawy
"""
import os
os.system("cls")

lst1 = [1, 3, 5, 7, 9, 11]


print(lst1)             # wyswietli cała listę ,

print(type(lst1))
print("ilość elementów ", len(lst1))

print(lst1[3])		    # wyswietli element 4
print(lst1[-2])		    # wyswietli przedostatni element list  -1 to ostatni


# usuwanie pojedynczych elementów listy
del lst1[1]   		    # usuwam drugi element listy
del lst1[-1]            # usuwam ostatni element listy

print(lst1)
print("ilość elementów ", len(lst1))

# dodawanie elementów listy
lst1.append(13)     # dodaje na koncu  listy element 13
print(lst1)

lst1.insert(2, 88)
lst1.insert(17, 44)     # ??
print(lst1)


lst2 = []           # utworzylem pusta liste
print(type(lst2))
lst2.append(1)
lst2.append(2)
lst2.append("ABC")
print(lst2)
