
from os import system
system('cls')

a = 1  # None
assert a, "Zmienna 'a' nie moze być pusta"

x = float(input('Wprowadz liczbe: '))

assert x != 0.0
x = 1 / x
print(x)

ile_elementow = int(input('podaj wielkość listy '))
lst = [i for i in range(ile_elementow)]
assert len(lst) > 0, 'lista nie może być pusta'

str1 = input(' ciag znaków ')
assert str1, 'Nie pusty'

str1 = input(' podaj nazwę ')
assert str1.isalpha(), 'tylko litery'

str1 = input(' podaj nazwę ')
assert str1.isalpha() or str1.isdigit(), 'tylko litery i cyfry'
