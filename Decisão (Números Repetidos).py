x = int(input())
y = int(input())
z = int(input())
if(x == y) and (x == z) and (y == z):
   print(0)
elif(x == y):
    print(z)
elif(x == z):
    print(y)
elif(y == z):
    print(x)
elif(y != x) and (x != z) and (z != y):
    print(x + y + z)
