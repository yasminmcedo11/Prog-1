n = int(input())
x = [0] * n
soma = 0
m = 0
nulo = 0
for i in range(n):
    x[i] = int(input())
for i in range(n):
    for j in range(n-1):
        if(x[j] > x[j+1]):
            t = x[j]
            x[j] = x[j+1]
            x[j+1] = t
for p in range(n-1):        
    if(x[p] == x[p+1]):
        soma = soma + 1
m = n - soma
y = [0] * m
if(soma == 0):
    print(x)
else:
    if(m == 1):
        for u in range(m):
            y[u] = x[u]
    else:    
       for k in range(m+1):
          if(x[k] == x[k-1]):
             nulo = nulo + 1
          if(x[k] != x[k-1]):
             y[k-nulo] = x[k]    
    print(y) 
        
            
            
    
