"""
z punktu widzenia wykorzystania w innych projektach
klasa stos jest niemodyfikowalna - (Nie powinieniem jej modyfikowac)
"""

from os import system
# from sys import exit
system('cls')


class Stos:
    def __init__(self) -> None:
        self.__stos_lst = []

    def push(self, val):
        self.__stos_lst.append(val)

    def pop(self):
        val = self.__stos_lst[-1]
        del self.__stos_lst[-1]
        return val

    def count(self):
        return len(self.__stos_lst)

    def clear(self):
        self.__stos_lst = []


class Stos_Dodawanie(Stos):
    """
    Dodajmy nową klasę do obsługi Stosów.
    Nowa klasa powinna mieć możliwość usykania sumy  elementów
    aktualnie przechowywanych w Stosie.
    """

    def __init__(self):
        #  wywołanie kontruktora
        # print('Wywolanie w klasie Stos_Dodawanie nazwa klasy:', self.__class__.__name__)
        # print(self)

        super().__init__()
        # Stos.__init__(self)  # alternatywa
        self.__sum = 0

    def get_suma(self):
        return self.__sum

    def push(self, val):
        self.__sum += val
        super().push(val)
        # Stos.push(self, val)

    def pop(self):
        # val = Stos.pop(self)
        val = super().pop()
        self.__sum -= val
        return val


# test = Stos()
stos_dod_o1 = Stos_Dodawanie()

for i in range(5):
    stos_dod_o1.push(i)
# odwołuje się do metod

print("wielkość stosu wynosi", stos_dod_o1.count())
print("suma elementów na stosie wynosi ", stos_dod_o1.get_suma())
print("Kolejne elementy stosu to ", end="")

for i in range(5):
    print(stos_dod_o1.pop(), end=" ")
