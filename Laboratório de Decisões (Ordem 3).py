a = int(input())
b = int(input())
c = int(input())
if(a == b) and (a == c):
   print("iguais")
else:
     if(a == b): 
        print(a + b - c)
     elif(a == c):
         print(a + c - b)
     elif(b == c):
         print(b + c - a)
     else:
         if(a > b > c):
           print(a,b,c)
         elif(b > a > c):
             print(b,a,c)
         elif(b > c > a):
             print(b,c,a)
         elif(c > b > a):
             print(c,b,a)
         elif(c > a > b):
             print(c,a,b)
         elif(a > c > b):
            print(a,c,b)