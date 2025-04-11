# CRIE UM MENU COM 3 OPÇÕES: 1 - DIZER “OI”, 2 - DIZER “TCHAU” E 3 - SAIR. O PROGRAMA DEVE PEDIR OPÇÕES AO 
# USUÁRIO ATÉ QUE A OPÇÃO 3 SEJA ESCOLHIDA.

opcao = 0

while opcao != 3:
    opcao = int(input(f'1 - Dizer “Oii”\n2 - Dizer "Tchau”\n3 - Sair\nEscolha uma opção:'))
    if opcao == 1:
        print('Oii')
    else:
        print('Tchau')
