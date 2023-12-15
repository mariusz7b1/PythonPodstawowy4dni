""""
Dziedziczenie równoległe po 2 klasach
"""

from os import system
system('cls')


class Osoba:
    def __init__(self, imie, nazwisko):
        self.imie = imie
        self.nazwisko = nazwisko
        self.nazwa = imie + ' ' + nazwisko

    def get_info(self):
        print(self.imie + ' ' + self.nazwisko)


class StanowiskoPracy:
    def __init__(self, stanowisko, poziom):
        self.stanowisko = stanowisko
        self.poziom = poziom
        self.nazwa = poziom + ' ' + stanowisko

    def get_info(self):
        print(self.poziom + ' ' + self.stanowisko)


class Pracownik(Osoba, StanowiskoPracy):
    def __init__(self, imie, nazwisko, stanowisko, poziom):
        Osoba.__init__(self, imie, nazwisko)
        StanowiskoPracy.__init__(self, stanowisko, poziom)

    def get_info(self):
        Osoba.get_info(self)
        StanowiskoPracy.get_info(self)


janek = Pracownik('Jan', 'Kowalski', 'sysadmin', 'junior')
janek.get_info()


# print ('{} {} jest zatrudniony jako {} {}
# '.format(janek.imie,janek.nazwisko,janek.poziom,janek.stanowisko) )
