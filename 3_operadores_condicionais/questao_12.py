# Crie um programa que receba 3 números e retorne a soma dos 2 menores números.

x = float(input('Digite um número: '))
y = float(input('Digite um número: '))
z = float(input('Digite um número: '))

if x >= y and x >= z:
    print(y + z)
elif y >= x and y >= z:
    print(x + z)
else:
    print(x + y)
