def maior_menor(v):
    y = 1
    z = []
    soma = 0
    for i in range(len(v)):
        for j in range(len(v)-1):
            if(v[j] > v[j+1]):
                y = y + 1
            else:
                z.append(y)
                soma = soma + 1
                y = 1
    for k in range(soma):
        for p in range(soma-1):
            if(z[p] < z[p+1]):
                t = z[p]
                z[p] = z[p+1]
                z[p+1] = t
    print(z[0])        
    return v
            
n = int(input())
v = [0] * n
for i in range(n):
    v[i] = int(input())
maior_menor(v)   
