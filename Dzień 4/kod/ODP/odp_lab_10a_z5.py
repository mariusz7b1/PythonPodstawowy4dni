from os import system
system('cls')


class KontoBankowe:
    def __init__(self, numer_konta, saldo, wlasciciel):
        self.numer_konta = numer_konta
        self.saldo = saldo
        self.wlasciciel = wlasciciel

    def wplac(self, kwota):
        self.saldo += kwota

    def wyplac(self, kwota):
        if self.saldo >= kwota:
            self.saldo -= kwota
        else:
            print("Niewystarczające środki na koncie.")


konto = KontoBankowe("1234567890", 1000, "Jan Kowalski")
konto.wplac(500)
print(konto.saldo)  # Wyświetli: 1500

konto.wyplac(200)
print(konto.saldo)  # Wyświetli: 1300

konto.wyplac(2000)  # Wyświetli: Niewystarczające środki na koncie.
