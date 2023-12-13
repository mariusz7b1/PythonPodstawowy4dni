"""
format_spec     ::=  [[fill]align][sign][#][0][width][grouping_option]
[.precision][type]
fill            ::=  <any character>
align           ::=  "<" | ">" | "=" | "^"
sign            ::=  "+" | "-" | " "
width           ::=  digit+
grouping_option ::=  "_" | ","
precision       ::=  digit+
type            ::=  "b" | "c" | "d" | "e" | "E" | "f" | "F" | "g"
| "G" | "n" | "o" | "s" | "x" | "X" | "%"
"""

from math import pi
liczba_kotow = 5

# 1 - nazwanie parametrów
napis = f"Ala ma {liczba_kotow} kotow"
print(napis)

# 2
kto = "Ewa"
napis = f"{kto} ma {liczba_kotow} kotow"
print(napis)


# align
# < - wyrównanie do lewej,
# > - wyrównanie do prawej,
# ^ - wyśrodkowanie.

napis = f"{kto:<10} ma {liczba_kotow} kotow"
print(napis)

napis = f"{kto:>10} ma {liczba_kotow} kotow"
print(napis)

napis = f"{kto:^10} ma {liczba_kotow} kotow"
print(napis)


# sign
# + (plus) - liczby dodatnie otrzymują znak plus, ujemne znak minus
# - (minus) - liczby dodatnie nie otrzymują znaku plus,
#                    ujemne otrzymują znak minus przed cyframi,
# spacja - liczby dodatnie poprzedza spacja,
#                 ujemne otrzymują znak minus przed cyframi

liczba1 = 10
liczba2 = -20

napis = f"Pierwsza liczba to {liczba1:<+4} druga liczba to {liczba2:<+4}"
print(napis)

napis = f"Pierwsza liczba to {liczba1:<-4} druga liczba to {liczba2:<-4}"
print(napis)

napis = f"Pierwsza liczba to {liczba1:< 4} druga liczba to {liczba2:< 4}"
print(napis)

# grouping_option:
# , (przecinek) - użycie przecinka jako separatora dla tysięcy.
# _ (podkreślnik/podłoga) - użycie podłogi jako separatora dla tysięcy.

liczba1 = 1024344
liczba2 = -202343
napis = f"Pierwsza liczba to {liczba1:+9_} druga liczba to {liczba2:<+9,}"
print(napis)

# precision i # Wybrane identyfikatory typu prezentacji (pole type):
# d liczba całkowita
# f liczba zmiennoprzecinkowa

# chcemy miecz liczby po przecinku
liczba3 = liczba1/-liczba2


napis = f"Trzecia to {liczba3:-9,.3f} a wartość pi wynosi {pi:<+9,.2f}"
print(napis)
