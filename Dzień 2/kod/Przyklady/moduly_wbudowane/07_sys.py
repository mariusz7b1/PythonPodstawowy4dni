import sys
from os import system
system("cls")

# wypisz element modulu radnom nie zaczynajace sie od "_"
for ele in dir(sys):
    if ele[0] != "_":
        print(ele)

print("\n\n")
print("scieżki ....")
for p in sys.path:
    print(p)
