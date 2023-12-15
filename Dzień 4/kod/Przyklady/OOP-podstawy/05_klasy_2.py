""" Test"""


class Druga_Klasa:
    def __init__(self):
        self.__zm1 = 0

    def fun1(self):
        self.__zm1 += 1
        print("hej")
        self.__fun2()

    def __fun2(self):
        self.__zm1 += 1
        print("hejHO")

    def get_war(self):
        return self.__zm1


obj_2_1 = Druga_Klasa()
obj_2_1.fun1()

# print(obj_2_1.__zm1)

print(obj_2_1.get_war())


print(vars(obj_2_1))

print(dir(obj_2_1))

print(obj_2_1.get_war())


# obj_2_1.__fun2()  # generuje bład
