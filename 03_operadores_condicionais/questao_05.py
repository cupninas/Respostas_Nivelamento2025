# Faça um programa que receba 3 números (abates, mortes e assistências) de um jogador 
# e diga se o saldo dele no jogo (saldo = (abates + assitências) - mortes) é 
# positivo (maior que 0) ou negativo (menor que 0) ou neutro (igual a 0).

abates = int(input('informe o número de abates:'))
mortes = int(input('informe o número de mortes:'))
assistencias = int(input('informe o número de assistências:'))

saldo = abates + assistencias - mortes 

if saldo > 0:
    print('Saldo positivo.')
elif saldo < 0:
    print('Saldo negativo.')
elif saldo == 0: 
    print('Saldo neutro.')
