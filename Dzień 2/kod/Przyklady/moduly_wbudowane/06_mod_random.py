from random import randrange, randint, random, choice, sample

for ele in dir(random):
    if ele[0] != "_":
        print(ele, end=", ")

print(randrange(100))
print(randrange(0, 100))
print(randrange(0, 100, 2))
print(randint(0, 100))

for i in range(20):
    print(randrange(0, 20, 2), end=" ")


lst = []
for i in range(1, 50):
    lst.append(i)
print(lst)

print(choice(lst))  # wybiera 1
print(sample(lst, 6))  # wybiera 6
