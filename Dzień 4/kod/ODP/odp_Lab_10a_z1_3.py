from datetime import date

# ZAD 1


class Kwadrat:
    def __init__(self, dlugosc_boku):
        # należy zabezpieczyć się na wypadek wartości < 0
        self.__dlugosc_boku = dlugosc_boku

    def oblicz_powierzchnie(self):
        return self.__dlugosc_boku*self.__dlugosc_boku

    def oblicz_obwod(self):
        return self.__dlugosc_boku*4


figura1 = Kwadrat(12)
print(figura1.oblicz_obwod())
print(figura1.oblicz_powierzchnie())

# ZAD 2


class Kalkulator:
    def __init__(self, liczba1, liczba2):
        # należy zabezpieczyć się na wypadek wartości < 0
        self.__liczba1 = liczba1
        self.__liczba2 = liczba2

    def oblicz_sume(self):
        print(self.__liczba1+self.__liczba2)

    def oblicz_iloczyn(self):
        print(self.__liczba1*self.__liczba2)

    def oblicz_iloraz(self):
        if self.__liczba2 != 0:
            print(f"{self.__liczba1/self.__liczba2:.3f}")
        else:
            print("NIE dzielimy przez 0")

    def oblicz_roznice(self):
        print(self.__liczba1-self.__liczba2)


oblicz = Kalkulator(16, 45)
oblicz.oblicz_iloraz()
oblicz.oblicz_iloczyn()

# ZAD 3


class Samochod:
    def __init__(self, marka, model, rok_prod, przebieg):
        self.__marka = marka
        self.__model = model
        assert isinstance(rok_prod, int), "Oczekiwana wartosc 'int'"
        self.__rok_prod = rok_prod
        assert isinstance(rok_prod, int), "Oczekiwana wartosc 'int'"
        self.__przebieg = przebieg

    def przebieg_roczny(self):
        rok = date.today().year
        if rok > rok-self.__rok_prod:
            przebieg_r = self.__przebieg/(rok-self.__rok_prod)
        else:
            przebieg_r = 0
        return przebieg_r

    def przejedz_km(self, ile_km):
        assert isinstance(ile_km, int), "Oczekiwana wartosc 'int'"
        if ile_km > 0:
            self.__przebieg += ile_km


corolka1 = Samochod("Toyota", "Corolla,", 2019, 40000)
oktawiusia1 = Samochod("Skoda", "Octavia", 2016, 140000)
print(f"Aktualny przebieg roczny {corolka1.przebieg_roczny()} km")
corolka1.przejedz_km(1000)
print(f"Aktualny przebieg roczny {corolka1.przebieg_roczny()} km")
