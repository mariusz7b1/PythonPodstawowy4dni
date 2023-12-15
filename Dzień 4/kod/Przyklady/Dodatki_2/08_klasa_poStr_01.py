class MyString(str):

    def reverse(self):
        return self[::-1]

    def myenumer(self):
        return list(enumerate(self))


mystr1 = MyString("Ala ma kota")

print(mystr1)
print(mystr1.reverse())     # moja metoda
print(mystr1.split())       # metoda oryg
print(mystr1.upper())
print(mystr1.myenumer())
mystr1.unick = set(mystr1)
print(mystr1.unick)
