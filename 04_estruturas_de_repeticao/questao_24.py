# FAÇA UM PROGRAMA QUE PEÇA UM VALOR N
#  E IMPRIMA UMA PIRÂMIDE INVERTIDA DE
#  ASTERISCOS.
#  EXEMPLO:
#  ****
#   ***
#    **
#     *

n = int(input("Digite o valor de N: "))

for i in range(n, 0, -1):
    linha = ' ' * (n - i) + '*' * i
    print(linha)