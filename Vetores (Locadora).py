lista1 = [0] * 10
lista2 = [0] * 10
jogos = 0
for i in range(10):
    lista1[i] = int(input())
    for j in range(10):
        while lista1[j] >= 5:
            lista1[j] = lista1[j] - 5
            lista2[j] = lista2[j] + 1
print(lista2)      
     
    