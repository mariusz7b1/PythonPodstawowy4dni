""""
Dziedziczenie równoległe po 3 klasach
"""


class Klasa1:
    def __init__(self, zm_klasa="jestesmy zmienna klasy 1"):
        self.zm_klasa1 = zm_klasa

    def metoda1(self):

        print("metoda1 z Klasy1")


class Klasa2:
    def __init__(self, zm_klasa="jestesm zmienna klasy 2"):
        self.zm_klasa2 = zm_klasa

    def metoda2(self):
        print("metoda2 z Klasy2")


class Klasa3:
    def __init__(self, zm_klasa="jestesm zmienna klasy 2"):
        self.zm_klasa3 = zm_klasa

    def metoda3(self):
        print("metoda3 z Klasy3")

# Klasa Dziedziczaca dziedziczy po Klasa1, Klasa2, Klasa3


class KlasaDziedziczaca1(Klasa1, Klasa2, Klasa3):
    def metoda_wlasna(self):
        print("metoda własna Klasy Dziedziczacej")


class KlasaDziedziczaca2(Klasa1, Klasa2, Klasa3):
    def __init__(self, zm_klasa="jestesm zmienna klasy X"):
        pass
        # super().__init__(zm_klasa)

    def metoda_wlasna(self):
        print("metoda własna Klasy Dziedziczacej")


# Tworzenie instancji Klasy Dziedziczacej
obiekt1 = KlasaDziedziczaca1()
obiekt2 = KlasaDziedziczaca2()

# Wywołanie metod z klas bazowych
obiekt1.metoda1()
obiekt1.metoda2()
obiekt1.metoda3()
print(obiekt1.zm_klasa1)

print(obiekt1.zm_klasa2)
print(obiekt1.zm_klasa2)
