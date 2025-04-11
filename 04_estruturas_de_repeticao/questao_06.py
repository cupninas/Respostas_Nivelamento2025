# FAÇA UM PROGRAMA QUE RECEBA UM NÚMERO E EXIBA A TABUADA EXPONENCIAL (X**1, X**2, X**3, …) DO NÚMERO.

numero = int(input('Insira um valor:'))

for i in range(11):
    print(f'{numero}**{i} = {numero**i}')
