"""
Przykład z dziedziczeniem wielokrotnym:
"""


class Pojazd:
    def __init__(self, kola):
        self.kola = kola

    def jedz(self):
        print(f"Pojazd na {self.kola} kołach jedzie.")


class Samochod(Pojazd):
    def __init__(self, marka, model, kola):
        super().__init__(kola)
        self.marka = marka
        self.model = model

    def jedz(self):
        print(f"{self.marka} {self.model} jedzie na {self.kola} kołach")


class SportowySamochod(Samochod):
    def __init__(self, marka, model, kola, moc):
        super().__init__(marka, model, kola)
        self.moc = moc

    def jedz(self):
        print(
            f"{self.marka} {self.model} jedzie z mocą {self.moc} \
                KM na {self.kola} kołach")


bmw = SportowySamochod("BMW", "M3", 4, 450)
auto1 = Samochod("skoda", "octavia", 4)
bmw.jedz()
auto1.jedz()
