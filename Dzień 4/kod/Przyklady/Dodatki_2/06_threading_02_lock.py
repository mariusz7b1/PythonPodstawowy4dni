import threading


"""
Ponieważ oba wątki korzystają z tego samego zasobu
(tj. standardowego wyjścia, do którego jest kierowany print()),
musimy upewnić się, że tylko jeden wątek korzysta
z tego zasobu w danym momencie.
"""
# Tworzymy blokadę (Lock)
lock = threading.Lock()


def print_numbers():
    with lock:
        # Ten blok kodu jest chroniony blokadą
        for i in range(100):
            print(i, end=" ")


def print_letters():
    with lock:
        # Ten blok kodu jest chroniony blokadą
        for letter in 'abcdefghij':
            print(letter, end="-")


# Uruchamiamy dwa wątki
t1 = threading.Thread(target=print_numbers)
t2 = threading.Thread(target=print_letters)
t1.start()
t2.start()
t1.join()
t2.join()
