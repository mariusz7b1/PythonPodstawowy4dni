from os import system
system("cls")


class Osoba:
    def __init__(self, imie, nazwisko, wiek, adres):
        self.imie = imie
        self.nazwisko = nazwisko
        self.wiek = wiek
        self.__adres = adres

    @property
    def adres(self):
        return self.__adres

    @adres.setter
    def adres(self, nowy_adres):
        self.__adres = nowy_adres


jan = Osoba("Jan", "Kowalski", 30, "ul. Kwiatowa 5")
print(jan.adres)  # Wyświetli: ul. Kwiatowa 5

jan.adres = "ul. Słoneczna 10"
print(jan.adres)  # Wyświetli: ul. Słoneczna 10
