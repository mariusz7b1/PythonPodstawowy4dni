# dodaj input i int

number = input("Podaj liczbę ? ")

if not number.isdigit():
    print("miałeś podac liczbę !!!! czy to takie trudne ?")
else:
    number = int(number)
    if number > 7 or number < -7:
        print("Liczba jest większa niż 7 lub mniejsza niż -7.")
    else:
        print("Liczba mieści się w przedziale od -7 do 7.")
