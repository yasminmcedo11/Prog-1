x = int(input())
y = 3
z = 7
soma = 0
for i in range(1,100,1):
    if(i % 2 == 0):
      soma = soma - ((x * y)/z)
    else:
        soma = soma + ((x * y)/z)
    y = y + 5
    z = z + 2
soma = soma + x    
print("%.3f"%soma)    
