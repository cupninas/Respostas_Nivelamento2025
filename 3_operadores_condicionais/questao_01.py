#Peça um número ao usuário, verifique se esse número está entre 0 e 100 e exiba o resultado.

num = int(input("Digite um número: "))

if(num < 0):
    print(f"O número {num} é menor que 0.")

elif(num > 100):
    print(f"O número {num} é maior que 100.")

else:
    print(f"O número {num} está entre 0 e 100!")