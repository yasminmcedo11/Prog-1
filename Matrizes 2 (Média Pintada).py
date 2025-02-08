n = int(input())
media = 0
soma = 0
x = []
for i in range(n):
    y = [0] * n
    x.append(y)
for i in range(n):
    for j in range(n):
        x[i][j] = int(input())        
for i in range(n):
    for j in range(n):
        if(i > (n-1-j)) and (i > j):
            media = media + x[i][j]
            soma = soma + 1
        if(i < (n-1-j)) and (i < j):
            media = media + x[i][j]
            soma = soma + 1 
media = media/soma
print("%.2f"%media)
        