try:
    age = int(input("Podaj swój wiek: "))
    if age < 0:
        raise ValueError("Wiek nie może być ujemny")
except ValueError as e:
    print(e)
