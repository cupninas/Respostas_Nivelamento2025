#PEÇA DOIS NÚMEROS. RETORNE TRUE SE ELES FOREM PRIMOS ENTRE SI E FALSE SE NÃO FOREM.

num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))

if num1 < num2:
    menor = num1
else:
    menor = num2

primos_entre_si = True
i = 2
while i <= menor: 
    if num1 % i == 0 and num2 % i == 0:
        primos_entre_si = False
        break
    i += 1

print(primos_entre_si)