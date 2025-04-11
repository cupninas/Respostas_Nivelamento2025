#FAÇA UM PROGRAMA QUE RECEBA 5 NÚMEROS E EXIBA ELES DE FORMA ORDENADA (CRESCENTE)

n1 = n2 = n3 = n4 = n5 = 0

for i in range(5):
    num = int(input(f"Digite o {i + 1} número: "))
    if i == 0:
        n1 = num
    elif i == 1:
        n2 = num
    elif i == 2:
        n3 = num
    elif i == 3:
        n4 = num
    else:
        n5 = num

for _ in range(5):
    if n1 > n2: #compara e troca n1 e n2
        n1, n2 = n2, n1
    if n2 > n3: #compara e troca n2 e n3
        n2, n3 = n3, n2
    if n3 > n4: #compara e troca n3 e n4
        n3, n4 = n4, n3
    if n4 > n5: #compara e troca n4 e n5
        n4, n5 = n5, n4

print("Numeros ordenados: ", n1, n2, n3, n4, n5)