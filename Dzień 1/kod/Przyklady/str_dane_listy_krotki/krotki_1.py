tup1 = 1, 2, 3, 4

print(type(tup1), end="\t")
print(tup1)

tup2 = ('a', 'b', 'c')
print(type(tup2), end="\t")
print(tup2)


tup3 = tup1+tup2
print(type(tup3), end="\t")
print(tup3)

tup1 = tup1+tup1
print(tup1)

# del tup3[1]  - niedopuszczalne
del tup3

print(tup1[2])
tup5 = 1
tup5 = (1)      # to nie jest krotka
print(type(tup5))

tup5 = (1,)      # teraz ok
print(type(tup5))

tup5 = tup5*10
print(len(tup5))
print(tup5)
