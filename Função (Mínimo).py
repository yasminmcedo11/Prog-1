def maior_numero(v,x):
    y = []
    l = 0
    for i in range(len(v)):
        for j in range(len(v)-1):
            if(x[0] <= j <= x[1]):
                if(j == x[0]):
                    l = j
                else:
                    if(l > v[j]):
                        l = j
    return l

n = int(input())
v = [0] * n
for i in range(n):
    v[i] = int(input())
m = int(input())
for j in range(m):
    x = [0] * 2
    for k in range(2):
        x[k] = int(input())
    l = maior_numero(v,x)
    print(l)


    