class Kwadraty:
    def __init__(self, limit):
        self.limit = limit

    def __iter__(self):
        self.aktualna = 0
        return self

    def __next__(self):
        self.aktualna += 1
        if self.aktualna > self.limit:
            raise StopIteration
        return self.aktualna ** 2


kwadraty = Kwadraty(5)
for kwadrat in kwadraty:
    print(kwadrat)
