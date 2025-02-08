n = int(input())
x = []
soma = 0
media = 0
menores = 0
for i in range(n):
    y = [0] * n
    x.append(y)
for i in range(n):
    for j in range(n):
        x[i][j] = int(input())
for k in range(n):
    for m in range(n):
        media = media + x[k][m]
        if(m > k):
            soma = soma + x[k][m]
media = media/(n*n)
for a in range(n):
    for b in range(n):
        if(x[a][b] < media):
            menores = menores + 1
print(soma)
print(menores)
            
        
    