x = int(input())
y = int(input())
z = 1
continua = True
while z < x and continua:
    w = int(input())
    z = z + 1
    if(w < y):
        continua = False
        w = y
if(continua):
    print("sim")
else:
    print("não")
