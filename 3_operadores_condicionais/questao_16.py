# Peça que o usuário insira um ano.
# Retorne True se o ano for bissexto e False se não for.

ano = int(input('Digite um ano: '))

if ano % 4 == 0:
    if ano % 100 == 0:
        if ano % 400 == 0:
            print(True)
        else:
            print(False)
    else:
        print(True)
else:
    print(False)
