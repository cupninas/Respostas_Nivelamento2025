# Faça um algoritmo que recebe o número total de eleitores de um município, o valor de votos nulos, brancos e válidos. 
# Ao final, calcule o percentual de cada e mostre na tela.

total_votos = int(input('Informe o total de votantes: '))
votos_nulos = int(input('Informe o total de votos nulos: '))
votos_brancos = int(input('Informe o total de votos em branco: '))
votos_validos = int(input('Informe o total de votos validos: ')) 

perc_nulos = (votos_nulos * 100) / total_votos
perc_brancos = (votos_brancos * 100) / total_votos
perc_validos = (votos_validos * 100) / total_votos

print(f'O percentual de votos nulos é de: {perc_nulos}%')
print(f'O percentual de votos brancos é de: {perc_brancos}%')
print(f'O percentual de votos validos é de: {perc_validos}%')
