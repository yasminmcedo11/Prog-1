n = int(input())
x = []
for i in range(n):
    y = [0] * n
    x.append(y)
for i in range(n):
    for j in range(n):
        x[i][j] = int(input())
for k in range(n):
    for m in range(n):
        if(k == m):
            t = x[k][m]
            x[k][m] = x[k][n-1-m]
            x[k][n-1-m] = t
for a in range(n//2):
    t = x[0][a]
    x[0][a] = x[0][n-1-a]
    x[0][n-1-a] = t
print(x)                