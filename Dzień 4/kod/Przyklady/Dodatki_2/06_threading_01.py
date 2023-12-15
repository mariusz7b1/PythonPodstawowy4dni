import threading
from os import system
system("cls")


def print_numbers():
    for i in range(100):
        print(i, end=" ")


def print_letters():
    for letter in 'abcdefghijsdaasdas':
        print(letter, end="-")


# tworzymy
t1 = threading.Thread(target=print_numbers)
t2 = threading.Thread(target=print_letters)

# uruchamiamy
t1.start()
t2.start()

# Na końcu używamy metody join() na każdym z wątków,
# aby poczekać, aż oba wątki zakończą swoje działaniec
t1.join()
t2.join()
