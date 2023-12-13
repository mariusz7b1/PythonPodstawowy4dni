"""
Zrobić z tego zadanie
"""
from os import system
system('cls')


def wykonaj_sprawdzenie(*args):
    for war in args:
        assert isinstance(war, int), "argumenty muszą być int"


def wykonaj_dzialanie(*args):
    assert len(args) > 2, "Brak argumentów muszą być conajmniej 3"
    assert args[0] in ("+", "*"), "pierwszy argument to '+' lub '*'"
    for i in range(1, len(args)):
        assert isinstance(args[i], int), "Argumenty muszą być int"
    wynik = args[1]
    if args[0] == '+':
        for i in range(2, len(args)):
            wynik += args[i]
    else:
        for i in range(2, len(args)):
            wynik *= args[i]
    return wynik


# wykonaj_sprawdzenie(1, 2, 3)
# wykonaj_sprawdzenie(1, '2', 3)
print(wykonaj_dzialanie(1, 2, 9))
print(wykonaj_dzialanie("*", 1, 2, 9))
print(wykonaj_dzialanie("+", 1, 2, 9))
