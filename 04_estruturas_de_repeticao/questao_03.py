# PEÇA UM NÚMERO AO USUÁRIO E EXIBA O FATORIAL DESSE NÚMERO.

numero = int(input('informe um número:'))

fatorial = 1

for i in range(0,numero):
    fatorial = fatorial * (numero-i)

print(fatorial)
