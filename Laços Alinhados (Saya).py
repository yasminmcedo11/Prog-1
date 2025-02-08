x = 0
i = 1
j = 2
s = 0
r = 1
while (r == 1):
    x = int(input())
    print(1)
    print(2)
    i = 1
    j = 2
    s = (i * j) + 1
    print(s)
    for i in range(1,x-2,1):
        s = (s * j) + 1
        j = j + 1
        print(s)
    r = int(input())
          
    