""""Demonstaracja  zmienne instancji  """

from os import system
system("cls")


class TestKlasa:
    def __init__(self, wartosc=1):
        self.__pierwsza = wartosc

    def ustaw_druga(self, wartosc=2):
        self.__druga = wartosc


ob1 = TestKlasa()
ob2 = TestKlasa(2)

ob2.ustaw_druga(3)
# print(ob2.__druga)


ob2.__druga = 999

ob3 = TestKlasa(4)
ob3.__trzecia = 5
ob3.czwarta = 10


print(ob1.__dict__)
print(ob2.__dict__)

print(ob3.__dict__)
print(ob3.czwarta)
print(ob2.__druga)
