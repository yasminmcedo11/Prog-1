x = int(input())
y = int(input())
anos = 0
while x < y:
    x = x//1 + (x * 0.5)
    y = y//1 + (y * 0.3)
    anos = anos + 1
print(anos)
