import os
import platform


def wyczysc_ekran():
    """
    Czyści ekran terminala niezależnie od systemu operacyjnego.
    """
    system_operacyjny = platform.system()

    # Dla Windows
    if system_operacyjny == 'Windows':
        os.system('cls')

    # Dla Linux i MacOS
    else:
        os.system('clear')


# Użycie funkcji
wyczysc_ekran()
