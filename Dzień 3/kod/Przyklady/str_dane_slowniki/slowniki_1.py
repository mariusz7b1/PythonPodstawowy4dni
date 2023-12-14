"""Przykłady słowniki"""
from os import system
system("cls")

# słownik
pol_ang = {
    "kwiat": "flower",
    "woda": "water",
    "gleba": "soil",
    "drzewo": "tree",
    "trawa": "grass"
}

ele1 = pol_ang["gleba"]  	# przykład 1
print(ele1)    			    # wydrukuje: soil
# ele1 = pol_ang["glebba"]  	# bład brak klucza

ele2 = pol_ang.get("woda")  # przykład 2a
print(ele2)      			# wydrukuje: water

ele2 = pol_ang.get("wodda")  # przykład 2b
print(ele2)      			 # wydrukuje: None


pol_ang["zamek"] = "castle"  # dodanie elementu do slownika
pol_ang["zamek"] = "key"     # zamiana wartości pod kluczem zamek

test = pol_ang.items()
print(type(pol_ang.items()))
#
print(pol_ang)
print(pol_ang.keys())
print(pol_ang.values())


# petla 1
print("")
for element in pol_ang:
    print(element, end="->")
    print(pol_ang[element])

# petla 2 - ten sam efekt
print("")
for klucz in pol_ang.keys():
    print(f"{klucz}->{pol_ang[klucz]}")


# petla 3 - tylko wartości
print()
for war in pol_ang.values():
    print(war, end=" ")

print()
# usuwanie
print(len(pol_ang))     # na wyjściu 6:
del pol_ang["gleba"]    # usuwa element o kluczu gleba


wartosc = pol_ang.popitem()   # do wartość przypisana jest krotka
# z kluczem i wartością a element ostatni ulega skasowaniu
print(wartosc)

# do wartośc przypisywana jest wartość z klucza kwiat i element jest usuwany
wartosc = pol_ang.pop("kwiat")
print(wartosc)

print(pol_ang)
print(len(pol_ang))     # na wyjściu 3:


if "okno" not in pol_ang.keys():
    pol_ang["okno"] = "window"

print(pol_ang)

print(len(pol_ang))     # na wyjściu 4:
pol_ang.clear()   	    # usuwa wszystkie elementy

print(len(pol_ang))    	# na wyjściu: 0
del pol_ang    		    # usuwa cały słownik
