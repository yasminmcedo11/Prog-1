x = int(input())
if( x >= 500) and (x < 800):
  print(x - ((10/100)* x))
else:
    if(x >= 800) and (x < 1000):
        print(x - ((15/100)* x))
    elif(x >= 1000):
        print(x - ((80/100)* x))
    else:
        if(x < 500):
          print(x)