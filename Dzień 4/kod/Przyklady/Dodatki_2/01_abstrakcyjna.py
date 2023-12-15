from abc import ABC, abstractmethod


class Figura(ABC):   # moja klasa abstr.

    @abstractmethod
    def oblicz_pole(self):
        pass

    @abstractmethod
    def oblicz_obwod(self):
        pass


class Kwadrat(Figura):

    def __init__(self, bok):
        self.bok = bok

    def oblicz_pole(self):
        return self.bok * self.bok

    def oblicz_obwod(self):
        return self.bok * 4


kwadrat = Kwadrat(4)
print(kwadrat.oblicz_pole())  # Wynik: 16
