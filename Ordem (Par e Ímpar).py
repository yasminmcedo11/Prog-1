n = int(input())
x = [0] * n
for i in range(n):
    x[i] = int(input())
for i in range(n):    
    for j in range(n-1):
       if(x[j] % 2 == 0):
           if(x[j] > x[j+1]):
              t = x[j]
              x[j] = x[j+1]
              x[j+1] = t
       if(x[j] % 2 != 0):
           if(x[j] < x[j+1]):
              t = x[j]
              x[j] = x[j+1]
              x[j+1] = t
       if(x[j] % 2 != 0) and (x[j+1] % 2 == 0):
            t = x[j]
            x[j] = x[j+1]
            x[j+1] = t  
print(x)






            