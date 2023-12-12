# sposób tradycyjny
lista1 = []
for i in range(4):
    lista1.append(str(i))
print(lista1)

pass
# wyrazenie listowe
lista1 = [str(i) for i in range(4)]
print(lista1)


lista2 = [pow(ele, 3) for ele in range(11)]
lista3 = [ele**3 for ele in range(11)]
print(lista2)
print(lista3)
