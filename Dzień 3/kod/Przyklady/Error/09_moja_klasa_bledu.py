"""" Obsluga mojego błedu"""


class superError(Exception):
    def __init__(self, komunikat):
        self.komunikat = komunikat
        super().__init__(komunikat)


try:
    # Jakiś kod, który może zgłosić błąd
    raise superError("Coś poszło nie tak")
except superError as e:
    # Obsługa wyjątku
    print(f"Wystąpił błąd: {e}")
