# na podstawie
# https://chyla.org/artykuly/python/python-tutorial/formatowanie-napisow.html
# https://pl.python.org/docs/lib/typesseq-strings.html

# format_spec [[fill]align][sign][#][0][width][grouping_option][.precision][type]
'''
format_spec     ::=  [[fill]align][sign][#][0][width][grouping_option][.precision][type]
fill            ::=  <any character>
align           ::=  "<" | ">" | "=" | "^"
sign            ::=  "+" | "-" | " "
width           ::=  digit+
grouping_option ::=  "_" | ","
precision       ::=  digit+
type            ::=  "b" | "c" | "d" | "e" | "E" | "f" | "F" | "g" | "G" | "n" | "o" | "s" | "x" | "X" | "%"
'''
# format_spec [[fill]align][sign][#][0][width][grouping_option][.precision][type]

from math import pi
liczba_kotow = 5

# 1 - nazwanie parametrów
napis = 'Ala ma {} kotow'.format(liczba_kotow)
print(napis)

# 2
napis = '{kto} ma {ile} kotow'.format(ile=liczba_kotow, kto="Ala")
print(napis)

# 3 - Numerowanie parametrów
napis = '{1} ma {0} kotow'.format(liczba_kotow, "Ala")
print(napis)

napis = '{0} ma {1} kotow'.format(liczba_kotow, "Ala")
print(napis)


napis = '{1} ma {0} kotow'.format(liczba_kotow, "Ala")
print(napis)

# align
# < - wyrównanie do lewej,
# > - wyrównanie do prawej,
# ^ - wyśrodkowanie.
napis = '{1:<10} ma {0} kotow'.format(liczba_kotow, "Ala")
print(napis)

napis = '{1:>10} ma {0} kotow'.format(liczba_kotow, "Ala")
print(napis)

napis = '{1:^10} ma {0} kotow'.format(liczba_kotow, "Ala")
print(napis)


# sign
# + (plus) - liczby dodatnie otrzymują znak plus, ujemne znak minus przed cyframi
# - (minus) - liczby dodatnie nie otrzymują znaku plus, ujemne otrzymują znak minus przed cyframi,
# spacja - liczby dodatnie poprzedza spacja, ujemne otrzymują znak minus przed cyframi

liczba1 = 10
liczba2 = -20

napis = 'Pierwsza liczba to {0:<+4} druga liczbato {1:<+4}'.format(
    liczba1, liczba2)
print(napis)

napis = 'Pierwsza liczba to {0:<-4} druga liczbato {1:<-4}'.format(
    liczba1, liczba2)
print(napis)

napis = 'Pierwsza liczba to {0:< 4} druga liczbato {1:< 4}'.format(
    liczba1, liczba2)
print(napis)

# grouping_option:
# , (przecinek) - użycie przecinka jako separatora dla tysięcy.
# _ (podkreślnik/podłoga) - użycie podłogi jako separatora dla tysięcy.

liczba1 = 1024344
liczba2 = -202343
napis = 'Pierwsza liczba to {0:+9_} druga liczbato {1:<+9,}'.format(
    liczba1, liczba2)
print(napis)

# precision i # Wybrane identyfikatory typu prezentacji (pole type):
# d liczba całkowita
# f liczba zmiennoprzecinkowa

# chcemy miecz liczby po przecinku
liczba3 = liczba1/-liczba2


napis = 'Trzecia to {0:-9,.3f} a wartość pi wynosi {1:<+9,.2f}'.format(
    liczba3, pi)
print(napis)
