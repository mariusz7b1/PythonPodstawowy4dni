"""
wersja niekompletna tylko fragment zadania
bez zapisu do pliku
Otwieramy plik do odczytu
"""

with open("d:\\dane\\testowy.txt", "r", encoding="utf-8") as f:
    # Tworzymy pusty słownik
    slownik = {}
    # Dla każdego wiersza w pliku
    for linia in f:
        # Dla każdej litery w wierszu
        for litera in linia:
            # Jeśli litera jest literą
            if litera.isalpha():
                # Zamieniamy literę na małą literę
                litera = litera.lower()
                # Jeśli litera nie jest już w słowniku, dodajemy
                # ją z wartością 1
                if litera not in slownik:
                    slownik[litera] = 1
                else:
                    # Inkrementujemy wartość litery o 1
                    slownik[litera] += 1
    # Liczymy całkowitą liczbę liter
    calkowita_liczba_liter = sum(slownik.values())

# Wyświetlamy procentową częstotliwość wystąpienia każdej litery
for litera, liczba_wystapien in slownik.items():
    procent = 100 * liczba_wystapien / calkowita_liczba_liter
    str1 = f"Litera {litera}:{liczba_wystapien} {procent:.2f}%"
    print(str1)

print(calkowita_liczba_liter)
