# FAÇA UM PROGRAMA QUE AUMENTE UM NÚMERO (COMEÇANDO EM 0) DE 10 EM 10, ENQUANTO O USUÁRIO NÃO DISSER PARA PARAR.

continuar = 'S'
valor = 0 

while continuar != 'N':
    continuar = input('Deseja Iniciar/Continuar?')
    valor += 10
    print(valor)
