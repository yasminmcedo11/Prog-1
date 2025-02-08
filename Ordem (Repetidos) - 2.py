n = int(input())
x = [0] * n
y = []
for i in range(n):
    x[i] = int(input())
for i in x:
    if not i in y:
        y.append(i)
for k in range(len(y)):
    for j in range(len(y)-1):
        if(y[j] > y[j+1]):
            t = y[j]
            y[j] = y[j+1]
            y[j+1] = t
print(y)            