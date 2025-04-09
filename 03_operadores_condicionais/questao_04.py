# Leia o ano atual e o ano de nascimento de uma pessoa. 
# Escreva na tela uma mensagem se ela já tem idade para tirar a CNH ou não.

ano_atual = int(input('Informe o ano atual:'))
ano_nascimento = int(input('Informe o seu ano de nascimento:'))

if ano_atual - ano_nascimento >= 18:
    print('Você pode tirar CNH.')
else:
    print('Você não pode tirar CNH.')
