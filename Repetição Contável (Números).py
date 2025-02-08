n1 = int(input())
media = 0
soma = 0
produto = 1
maior = 0
menor = -1
for i in range(0,n1):
    n2 = int(input())
    soma = soma + n2
    media = soma/ n1
    produto = produto * n2
    if(menor == -1) or (n2 < menor):
        menor = n1
    if(n2 > maior):
        maior = n2
print("%.2f"%media)
print(soma)
print(produto)
print(menor)
print(maior)