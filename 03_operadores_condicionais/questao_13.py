# Peça 3 números ao usuário e verifique se é um triângulo.
# Caso seja um triângulo, diga se é
# equilátero (3 lados iguais),
# isósceles (2 lados iguais) ou
# escaleno (3 lados diferentes).

a = float(input('Digite o primeiro número: '))
b = float(input('Digite o segundo número: '))
c = float(input('Digite o terceiro número: '))

if a + b > c and a + c > b and b + c > a:
    if a == b == c:
        print('É um triângulo equilátero.')
    if a == b != c or a == c != b or b == c != a:
        print('É um triângulo isósceles.')
    if a != b and a != c and b != c:
        print('É um triângulo escaleno.')
else:
    print('Não é um triângulo.')
