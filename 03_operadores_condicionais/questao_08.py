# Sabe-se que uma pessoa é considerada “criança” se ela tem entre 0 e 11 anos, “adolescente” se ela tem entre 12 e 17 anos, 
# “adulta” se ela tem entre 18 e 59 anos e “idosa” se ela tem 60 ou mais anos.
# Faça um programa que receba a idade de uma pessoa e exiba a sua classificação etária.

idade = int(input("Digite a sua idade: "))

if(idade >= 0 and idade <= 11):
    print("Você é criança!")

elif(idade >= 12 and idade <= 17):
    print("Você é adolescente!")

elif(idade >= 18 and idade <= 59):
    print("Você é adulto(a)!")

elif(idade >= 60):
    print("Você é idoso(a)!")

else:
    print("Idade inválida!")   