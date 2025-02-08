n = int(input())
soma = 0
for k in range(n):
    x = [0] * 5
    soma = 0
    for i in range(5):
       x[i] = int(input())   
    for i in range(5):
        for j in range(4):
            if(x[j] > x[j+1]):
              t = x[j]
              x[j] = x[j+1]
              x[j+1] = t
              soma = soma + 1          
    print(soma)
    
            
           
        