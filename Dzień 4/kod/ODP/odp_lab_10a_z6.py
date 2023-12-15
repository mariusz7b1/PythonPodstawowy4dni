from os import system
system('cls')


class Zespol:
    def __init__(self, nazwa, rok_zalozenia, czlonkowie=[]):
        self.nazwa = nazwa
        self.rok_zalozenia = rok_zalozenia
        self.czlonkowie = czlonkowie

    def dodaj_czlonka(self, nowy_czlonek):
        self.czlonkowie.append(nowy_czlonek)

    def usun_czlonka(self, czlonek):
        if czlonek in self.czlonkowie:
            self.czlonkowie.remove(czlonek)


zespol = Zespol("The Example", 2010, ["Alicja", "Piotr"])
print(zespol.czlonkowie)  # Wyświetli: ['Alicja', 'Piotr']

zespol.dodaj_czlonka("Krzysztof")
print(zespol.czlonkowie)  # Wyświetli: ['Alicja', 'Piotr', 'Krzysztof']

zespol.usun_czlonka("Alicja")
print(zespol.czlonkowie)  # Wyświetli: ['Piotr', 'Krzysztof']
