# FAÇA UM PROGRAMA QUE RECEBA DIVERSOS VALORES (UM POR VEZ) E CONTINUE LENDO OS VALORES ATÉ QUE O USUÁRIO 
# DIGITE O “0”. LOGO DEPOIS, EXIBA A MÉDIA DOS NÚMEROS DIGITADOS (IGNORANDO O “0”)

valor = 1
cont = 0 
soma_valores = 0 

while valor != 0: 
    valor = int(input('informe um valor:'))
    cont += 1
    soma_valores += valor

media = soma_valores/(cont-1)
print(media)
