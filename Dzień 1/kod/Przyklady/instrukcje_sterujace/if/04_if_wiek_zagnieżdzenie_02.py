
# przyklad 2
# if zagnieżdzony
wiek = int(input("Podaj swoj wiek ? "))
if wiek >= 18:
    print("jestes pełnoletni")
    print("do 100 lat zostało ci ", 100-wiek)
    if wiek == 18:
        print("18 latek !!!- gratulacje")
else:
    print("dzieciak...")
