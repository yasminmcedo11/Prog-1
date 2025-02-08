x = int(input())
y = int(input())
z = int(input())
if(x + y == z) or (x + z == y) or (y + z == x):
    print("soma")
elif(x * y == z) or (x * z == y) or (y * z == x):
    print("multi")
elif(x + y + z) % 2 == 0:
     print("par")
else:
     print("ímpar")