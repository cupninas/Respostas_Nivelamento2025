# LEIA O ANO ATUAL E O ANO DE NASCIMENTO DE UMA PESSOA. ESCREVA NA TELA UMA MENSAGEM SE ELA JÁ TEM 
# IDADE TIRAR A CNH OU NÃO.

ano_atual = int(input('Informe o ano atual:'))
ano_nascimento = int(input('Informe o seu ano de nascimento:'))

if ano_atual - ano_nascimento >= 18:
    print('Você pode tirar CNH.')
else:
    print('Você não pode tirar CNH.')
