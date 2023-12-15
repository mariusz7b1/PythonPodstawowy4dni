class Student:
    def __init__(self, imie, nazwisko, rok_urodzenia, oceny=[]):
        self.imie = imie
        self.nazwisko = nazwisko
        self.rok_urodzenia = rok_urodzenia
        self.oceny = oceny

    def dodaj_ocene(self, ocena):
        self.oceny.append(ocena)

    def wylicz_srednia(self):
        return sum(self.oceny) / len(self.oceny)


student = Student("Anna", "Nowak", 1995, [4, 5, 3])
print(student.oceny)  # Wyświetli: [4, 5, 3]

student.dodaj_ocene(4)
print(student.oceny)  # Wyświetli: [4, 5, 3, 4]


def wylicz_srednia(student):
    return sum(student.oceny) / len(student.oceny)


srednia = wylicz_srednia(student)
print(srednia)  # Wyświetli: 4.0
