x = int(input())
a = x % 10
y = x // 10
b = y % 10
z = y // 10
c = z % 10
w = z // 10
d = w % 10
v = w // 10
e = v % 10
a = str(a)
b = str(b)
c = str(c)
d = str(d)
e = str(e)
abcde = str(a),str(b),str(c),str(d),str(e)
edcba = str(e),str(d),str(c),str(b),str(a)
if(abcde == edcba):
    print("sim")
else:
    print("não")