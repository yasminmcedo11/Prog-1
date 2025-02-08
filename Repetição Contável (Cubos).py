s = 0
for x in range(100,1000):
    a = int(x/100)
    b = int((x%100)/10)
    c = x%10
    s = (a ** 3) + (b ** 3) + (c ** 3)
    if(s == x):
        print(x)