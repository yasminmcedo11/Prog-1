n = int(input())
m = int(input())
x = []
for i in range(n):
    y = [0] * m
    x.append(y)
for i in range(n):
    for j in range(m):
        x[i][j] = int(input())
v = []        
for i in range(n):
    for j in range(m):
        c = x[i][j]
        v.append(c)
for i in range(n*m):
    for j in range((n*m)-1):
        if(v[j] < v[j+1]):
            t = v[j]
            v[j] = v[j+1]
            v[j+1] = t
a = []
for i in range(n):
    b = []
    for j in range(m):
        B = v[i+j*n]
        b.append(B)
    a.append(b)
print(a)                    