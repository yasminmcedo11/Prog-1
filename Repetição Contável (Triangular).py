n = int(input())
s = False
for i in range(1,n):
    if(i * (i + 1) * (1 + 2)) == n:
        print(i)
        print(i + 1)
        print(1 + 2)
        s = True
        break
print("não")