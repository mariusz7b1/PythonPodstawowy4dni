"""
Funkcje - podstawy, zakres zmiennych
"""

from os import system
system('cls')


def fun0():         # funkcja ma dostęp do zmiennych globalnych (skryptu)
    print(a, b)


def fun1():
    a = 11          # nie modyfikuje globalnej a tylko tworze lokalne a
    print(id(a))    # przykrywam globalne a
    b = 21
    print(a, b)


def fun2():
    global a        # funcja korzysta z globalnego a
    print(id(a))
    a = 11
    b = 21
    print(a, b)


a = 1
b = 10
print(id(a))
fun0()
print(f"Przed wywolaniem funkcj a={a},b={b}")
fun1()
print(f"Po wywolaniu fun1 a={a},b={b}")
fun2()
print(f"Po wywolaniu fun2 a={a},b={b}")
