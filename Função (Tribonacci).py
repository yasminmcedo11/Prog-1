def tribonacci(v):
    for i in range(len(v)):
        if(i == 0):
            v[i] = 1
        elif(i == 1):
            v[i] = 1
        elif(i == 2):
            v[i] = 2
        else:
            v[i] = v[i-1] + v[i-2] + v[i-3]
    return v    
                
n = int(input())
v = [0] * n
tribonacci(v)
print(v)

    
    
    