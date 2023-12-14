"""prosty generator przykład"""
from os import system
system("cls")


def generator(koniec):
    num = 0
    while num < koniec:
        yield num
        num += 1


def nieskonczony():
    num = 0
    while True:
        yield num
        num += 1


for i in generator(5):
    print(i, end=" ")


for i in nieskonczony():
    print(i, end=" ")
