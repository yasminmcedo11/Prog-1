a = int(input())
b = int(input())
div = 0
for i in range(a,b+1):
    for j in range(1,11,1):
        if(i % j == 0):
           div = div + 1
        if(div == 2):    
           print(a)
a = a + 1   