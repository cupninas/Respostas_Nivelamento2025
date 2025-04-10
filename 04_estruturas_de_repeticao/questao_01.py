#peça um número ao usuário e exiba a tabuada desse número

numero = int(input('insira um número:'))

for i in range(11): 
    print(f'{numero} x {i} = {numero*i}')
