""""Demonstaracja zmienne klasy """


class TestKlasa:
    licznik = 0
    __licznik = 0

    def __init__(self, wartosc=1):
        self.__pierwsza = wartosc
        TestKlasa.licznik += 1
        TestKlasa.__licznik += 2


print(TestKlasa.licznik)
# print(TestKlasa.__licznik)

ob1 = TestKlasa(1)
ob2 = TestKlasa(2)
ob3 = TestKlasa(3)

print(ob1.__dict__, ob1.licznik)
print(ob2.__dict__, ob2.licznik)
print(ob3.__dict__, ob3.licznik)

print(TestKlasa.__dict__)
print(TestKlasa.licznik)

# to wygenereuje bład
# print(TestKlasa.__licznik)
# ale to już nie
# dostep do zmiennej prywatnej Klasy
print("Licznik prywatny Klasy    ", ob1._TestKlasa__licznik)
print("Zmienna prywatny Obiektu 1", ob1._TestKlasa__pierwsza)
print("Zmienna prywatny Obiektu 2", ob2._TestKlasa__pierwsza)

# odwołanie do klasy a nie obiektu
