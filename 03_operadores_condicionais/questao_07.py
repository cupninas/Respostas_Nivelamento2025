# NA UFPA, O CONCEITO FINAL É DECIDIDOPELA MÉDIA ARITMÉTICA DAS 3 NOTAS DE UMALUNO. INFERIOR 
# A 5:“INSUFICIENTE”.ENTRE 5 E 6.9:“REGULAR”. ENTRE 7 E 8.9: “BOM” MAIOR OU IGUAL A 9: “EXCELENTE". 
# FAÇA UM PROGRAMA QUE RECEBA TRÊS NOTAS DE UM ALUNO, EXIBA O CONCEITO FINAL JUNTAMENTE DE UMA MENSAGEM.

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
