n = int(input("Digite um número inteiro positivo: "))
numero = 2

while numero < n:
    if(n % numero == 0):
      print(numero)
    numero = numero + 1
   