lista1 = [0] * 5
media = 0
menor = 200
for i in range(5):
    lista1[i] = float(input())
    media = media + lista1[i]
media = media/ 5
for j in range(5):
    lista1[j] = lista1[j] - media
    if(lista1[j] > menor):
        menor = lista1[j]
        lista1[j] = menor + media
print("%.2f"%lista1[j])
        