""" Test modułów 2 + pomiar czasu"""
import datetime
from random import randint
from os import system
import mpmodul_2

system("cls")
# print(dir(mpmodul_2))

print(f"Ilość wywołań funkcji z moduły wynosi {mpmodul_2.__licznik}")

lst = [randint(0, 100) for i in range(100000)]   #


# test 1 - unique  z wykorzystaniem set
start = datetime.datetime.now()
lst_wynik = mpmodul_2.unique_list(lst)
duration = datetime.datetime.now() - start

# print(lst_wynik)
print(f"czas wykonania(uniq set): wynosi {duration.microseconds:,}  μs")


# test 2 - unique tradycyjne
start = datetime.datetime.now()
lst_wynik = mpmodul_2.unique_list_2(lst)
duration = datetime.datetime.now() - start

# print(lst_wynik)
print(f"czas wykonania(uniq trady): wynosi {duration.microseconds:,}  μs")


# test 3 suma tradycyjna
start = datetime.datetime.now()
suma = mpmodul_2.sum_lst(lst)

duration = datetime.datetime.now() - start
print(
    f"suma wynosi {suma} a czas wykonania wynosi:{duration.microseconds:,} μs")

# test 4 suma wbudowana
start = datetime.datetime.now()
suma = sum(lst)
duration = datetime.datetime.now() - start
print(
    f"suma wynosi {suma} a czas wykonania wynosi:{duration.microseconds:,} μs")

print(f"Ilość wywołań funkcji z moduły wynosi {mpmodul_2.__licznik}")
