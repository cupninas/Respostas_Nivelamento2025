# Crie um algoritmo que leia um número inteiro entre 1 e 12 e escreva o mês correspondente.
# Além disso, escreva o semestre que esse mês se encontra e a estação do ano.
# Caso o usuário digite um número fora desse intervalo, coloque uma mensagem de erro.

numero = int(input('Digite um número: '))

if numero == 1:
    print('Janeiro, Primeiro Semestre, Verão')
elif numero == 2:
    print('Fevereiro, Primeiro Semestre, Verão')
elif numero == 3:
    print('Março, Primeiro Semestre, Outono')
elif numero == 4:
    print('Abril, Primeiro Semestre, Outono')
elif numero == 5:
    print('Maio, Primeiro Semestre, Outono')
elif numero == 6:
    print('Junho, Primeiro Semestre, Inverno')
elif numero == 7:
    print('Julho, Segundo Semestre, Inverno')
elif numero == 8:
    print('Agosto, Segundo Semestre, Inverno')
elif numero == 9:
    print('Setembro, Segundo Semestre, Primavera')
elif numero == 10:
    print('Outubro, Segundo Semestre, Primavera')
elif numero == 11:
    print('Novembro, Segundo Semestre, Primavera')
elif numero == 12:
    print('Dezembro, Segundo Semestre, Verão')
else:
    print('Mês inválido.')
