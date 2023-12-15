"""
Destruktor
"""


class Pliki:
    # Konstruktor
    def __init__(self, plik_in="d:\\dane\\testowy.txt",
                 plik_out="slownik.txt"):
        print('Utowrzony objekt')
        self.__tekst = ""
        self.__f_in = open(plik_in, 'rt', encoding='utf-8')
        self.__f_out = open(plik_out, 'at', encoding='utf-8')

    def czytaj_tekst(self, ile):
        self.__text = self.__f_in.read(ile)

    def zwroc_dane(self):
        return self.__text

    # Destruktor

    def __del__(self):
        print('Zabity objekt')
        self.__f_in.close()
        self.__f_out.close()


obj = Pliki()
obj.czytaj_tekst(100)
print(obj.zwroc_dane())
del obj
