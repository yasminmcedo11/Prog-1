x = int(input())
y = int(input())
z = int(input())
if(x > y) and (x > z):
  m = (x + y + z)/3
  s = x + y + z
  p = x * y * z
  if(y > z):
      menor = z
      maior = x
      print("%.1f"%m)
      print(s)
      print(p)
      print(menor)
      print(maior)
  else:
      menor = y
      maior = x
      print("%.1f"%m)
      print(s)
      print(p)
      print(menor)
      print(maior)
else:
    if(y > z) and (y > x):
      m = (x + y + z)/3
      s = x + y + z
      p = x * y * z
      if(z > x):
          menor = x
          maior = y
          print("%.1f"%m)
          print(s)
          print(p)
          print(menor)
          print(maior)
      else:
          menor = z
          maior = y
          print("%.1f"%m)
          print(s)
          print(p)
          print(menor)
          print(maior)
    elif(z > y) and (z > x):
        m = (x + y + z)/3
        s = x + y + z
        p = x * y * z
        if(y > x):
            menor = x
            maior = z
            print("%.1f"%m)
            print(s)
            print(p)
            print(menor)
            print(maior)
        else:
            menor = y
            maior = z
            print("%.1f"%m)
            print(s)
            print(p)
            print(menor)
            print(maior)
     
  
