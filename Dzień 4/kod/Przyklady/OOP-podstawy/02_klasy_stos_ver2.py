""""
ukryty stos :enkapsulacja
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
obj_stos1.push(11)
obj_stos1.push(22)
obj_stos1.push(33)

# print(obj_stos1.__stos_lst)
# genereuje blad Atribute Error

print("wielkość stosu", obj_stos1.count())

print(obj_stos1.pop())
print(obj_stos1.pop())
print(obj_stos1.pop())

print("wielkość stosu", obj_stos1.count())
