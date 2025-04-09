# Na UFPA, o conceito final é decidido pela média aritmética das 3 notas de um aluno.
# Inferior a 5: "Insuficiente". Entre 5 e 6.9: "Regular". Entre 7 e 8.9: "Bom". Maior ou igual a 9: "Excelente".
# Faça um programa que receba três notas de um aluno, exiba o conceito final juntamente de uma mensagem.


nota1 = float(input('insira a primeira nota:'))
nota2 = float(input('insira a segunda nota:'))
nota3 = float(input('insira a terceira nota:'))

media = (nota1 + nota2 + nota3)/3 

if media < 5: 
    print('INSUFICIENTE.')
elif media >= 5 and media <= 6.9: 
    print('REGULAR.')
elif media >= 7 and media <= 8.9: 
    print('BOM.')
else: 
    print('EXCELENTE.')
