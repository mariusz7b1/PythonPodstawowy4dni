""" Funkcja anonimowa lambda cd """
from os import system
system("cls")


def myfunc(n):
    return lambda a: a * n


mydoubler_2 = myfunc(2)
mydoubler_4 = myfunc(4)


print(type(mydoubler_2))
print(type(mydoubler_4))

print(mydoubler_2(11))
print(mydoubler_4(11))
