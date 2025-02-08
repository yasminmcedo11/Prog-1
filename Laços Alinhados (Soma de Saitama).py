n = int(input())
m = int(input())
s = 0
i = 1
j = 1
n1 = 0
n2 = 0
for i in range(1,n+1):
    for j in range(1,m+1):
        n1 = n1 + ((i**2)*j)
        n2 = n2 + (3**i)*((j*(3**i))+(i*(3**j)))
        s = s + (n1/n2)
        j = j + 1
    i = i + 1    
print("%.4f"%s)    
    