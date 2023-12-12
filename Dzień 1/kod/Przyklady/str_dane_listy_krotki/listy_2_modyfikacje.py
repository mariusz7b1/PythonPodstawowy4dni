"""
Listy - wycinki, operatory 'in' 'not in'  sortowanie
"""
import os
os.system("cls")

lst1 = []                   # Tworzenie pustej listy.
for i in range(10):
    lst1.append(i + 1)
print(lst1)

pass
# wycinanie podstawowe
lst1_wycinek1 = lst1[1:3]   # element 1 i 2 ale 3 NIE
lst1_wycinek2 = lst1[3:-1]
lst1_wycinek3 = lst1[:-2]
lst1_wycinek4 = lst1[-1:]

print(lst1_wycinek1)
print(lst1_wycinek2)
print(lst1_wycinek3)
print(lst1_wycinek4)

# wycinanie z krokiem
lst1_wycinek1 = lst1[1:5:2]
lst1_wycinek2 = lst1[::3]
lst1_wycinek3 = lst1[::-1]    # ciekawe wykorzystannie
lst1_wycinek4 = lst1[::-2]

print(lst1_wycinek1)
print(lst1_wycinek2)
print(lst1_wycinek3)
print(lst1_wycinek4)

#  in,  not in
var1 = 8
if var1 in lst1:
    print(f"wartość {var1} jest na liście")
else:
    print(f"wartość {var1} NIE jest na liście")

var1 = 14
if var1 not in lst1:
    print(f"wartość {var1} NIE jest na liście")
else:
    print(f"wartość {var1} jest na liście")

#  sort , reverse
lst2 = [1, 3, 9, 4, 5, 2]
print(lst2)
lst2.sort()
print(lst2)

lst2.reverse()
print(lst2)

t1 = "Ala ma kota"
lst3 = list(t1)     # funkcja list !!!
lst3.sort()
print(lst3)
