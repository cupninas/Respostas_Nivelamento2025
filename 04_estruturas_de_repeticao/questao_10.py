#"questão 10"
soma_primos = 0

for numero in range(1, 51):
    primo = True
    if numero < 2:
        primo = False
    else:
        for i in range(2, int(numero**0.5) + 1): #tira a raíz para ver se o número pode ser divísivel ou não por outros, pega o proxímo para poder verificar o único
            if numero % i == 0:
                primo = False
    if primo == True:
        soma_primos += numero

print(f"Soma dos primos = {soma_primos}")
