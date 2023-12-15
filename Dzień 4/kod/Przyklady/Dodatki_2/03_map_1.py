from os import system
system("cls")

numbers = [7, 4, 9, 6, 8, 1]


def multiple_hash(multi):
    return "#" * multi


def pow2(war):
    return pow(2, war)


for ele in map(multiple_hash, numbers):
    print(ele)


for ele in map(pow2, numbers):
    print(ele)
