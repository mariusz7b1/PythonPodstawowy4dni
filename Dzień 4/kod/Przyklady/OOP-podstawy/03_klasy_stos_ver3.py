"""
wykorzystanie 2 stosów
2 instancje klasy
"""


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


obj_stos1 = Stos()
obj_stos2 = Stos()

obj_stos1.push(11)
obj_stos2.push(111)

obj_stos1.push(22)
obj_stos2.push(222)
obj_stos2.push(333)


print("wielkość stosu 1:", obj_stos1.count())
print("wielkość stosu 2:", obj_stos2.count())

print(obj_stos1.pop())
print(obj_stos2.pop())
