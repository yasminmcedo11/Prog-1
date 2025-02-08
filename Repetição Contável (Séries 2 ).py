n = int(input())
soma = n + 1
x = 5
for i in range(50):
    if(i % 2 == 0):
        soma = soma + (n + x)
    else:    
        soma = soma + (n * x)
    x = x + 4
print(x)    
    