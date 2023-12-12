from os import system
system('cls')

war = 0
while war != 10:    # rożne od 10
    war = int(input('Podaj liczbę (10-ZAKONCZENIE) '))
    if war == 666:
        print('!! ZLE !!')
        break
else:
    print('Zakonczone z sukcesem')
