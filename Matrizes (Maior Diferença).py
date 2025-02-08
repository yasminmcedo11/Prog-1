n = int(input())
m = int(input())
x = []
maior = -1
for i in range(n):
    y = [0] * m
    x.append(y)
for i in range(n):
    for j in range(m):
        x[i][j] = int(input())
for k in range(n):
    for z in range(m):
        if(x[k][z] > maior):
            maior = x[k][z]
for a in range(n):
    for b in range(m):
        x[a][b] = x[a][b] - maior
print(x)        
        
        
    
    
    
