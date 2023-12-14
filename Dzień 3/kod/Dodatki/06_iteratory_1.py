"""Iterator przyklad"""
from os import system
system("cls")


def wypisz_elementy(lista_elementow):

    iterator = iter(lista_elementow)
    print(type(iterator))
    try:
        while True:
            element = next(iterator)
            print(element)
    except StopIteration:
        print("Koniec listy elementów.")


lista_ksiazek = ["Czysty kod", "Python od podstaw", "Wzorce projektowe"]
wypisz_elementy(lista_ksiazek)
