n = int(input())
A = []
for i in range(n):
    x = [0] * n
    A.append(x)
for i in range(n):
    for j in range(n):
        A[i][j] = int(input())
B = []
for i in range(n):
    B.append([0]*n)
for i in range(n):
    for j in range(n):
        for k in range(n):
            B[i][j] = B[i][j] + (A[i][k] * A[k][j])
D = []
for i in range(n):
    D.append([0]*n)
for p in range(n):
    for q in range(n):
       D[p][q] = A[q][p]
C = []            
for i in range(n):
    C.append([0]*n)
for y in range(n):
    for z in range(n):
        C[y][z] = B[y][z] + D[y][z]
print(C)        
        
        
        
            
