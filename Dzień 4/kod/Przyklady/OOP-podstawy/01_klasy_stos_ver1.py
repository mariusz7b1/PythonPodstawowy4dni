"""
stos podstawowy -  bez ukrytego stosu :)
mozliwy bezposredni dostep
"""


class Stos:
    def __init__(self) -> None:
        self.stos_lst = []

    def push(self, val):
        self.stos_lst.append(val)

    def pop(self):
        val = self.stos_lst[-1]
        del self.stos_lst[-1]
        return val

    def count(self):
        return len(self.stos_lst)

    def clear(self):
        self.stos_lst = []


obj_stos = Stos()

obj_stos.push(11)
obj_stos.push(22)
obj_stos.push(33)


print("wielkość stosu", obj_stos.count())

# moge bezposrednio odwolac się do zmiennej instancji
# print(obj_stos.stos_lst)
# del obj_stos.stos_lst[-2]

print(obj_stos.pop())
print(obj_stos.pop())
print(obj_stos.pop())


print("wielkość stosu", obj_stos.count())
