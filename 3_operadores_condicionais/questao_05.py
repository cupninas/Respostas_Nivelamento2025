# FAÇA UM PROGRAMA QUE RECEBA 3 NÚMEROS (ABATES, MORTES E ASSISTÊNCIAS) DE UM JOGADOR E DIGA SE O SALDO
# DELE NO JOGO (SALDO = (ABATES + ASSISTÊNCIAS) - MORTES) É POSITIVO (MAIOR QUE 0) OU NEGATIVO 
# (MENOR QUE 0) OU NEUTRO (IGUAL A 0).

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
