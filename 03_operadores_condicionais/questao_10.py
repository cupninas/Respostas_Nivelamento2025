# Faça uma calculadora com as operações de adição, subtração, multiplicação e divisão com dois números.

print('+ | Adição ')
print('- | Subtração ')
print('* | Multiplicação ')
print('/ | Divisão ')

operacao = str(input('Digite a operação: '))

x = float(input('Digite o primeiro número: '))
y = float(input('Digite o segundo número: '))

if operacao == '+':
    print(x + y)
elif operacao == '-':
    print(x - y)
elif operacao == '*':
    print(x * y)
elif operacao == '/':
    print(x / y)
else:
    print('Operação inválida.')
