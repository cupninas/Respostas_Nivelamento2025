# A prefeitura de Belém abriu uma linha de crédito para os funcionários estatutários.
# O valor máximo da prestação não poderá ultrapassar 25% do salário bruto.
# Faça um algoritmo onde o usuário informa o salário bruto e o valor da prestação.
# Após isso, informe se o empréstimo pode ser concedido.

salario = float(input('Digite o valor do salário: '))
prestacao = float(input('Digite o valor da prestação: '))

if prestacao <= salario * 0.25:
    print('O empréstimo pode ser concedido.')
else:
    print('O empréstimo não pode ser concedido.')
