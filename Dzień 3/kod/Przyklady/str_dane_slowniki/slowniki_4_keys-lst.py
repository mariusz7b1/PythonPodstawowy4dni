dct = {}
dct["imie"] = "Jan"
dct["nazwisko"] = "Nowak"
dct["wiek"] = 12
dct["adres"] = {"ulica": "Kosciuszki", "nrdomu": 12,
                "nrmieszkania": 6, "poczta": ("wrocław", 45676)}
dct["adresy_mail"] = ("jan.nowak@gmail.com",
                      "nowak@gmail.com", "j.nowak@gmail.com")

lst = []
for i in dct.keys():
    print(type(dct[i]))
    # lst.append(i)

print(lst)
