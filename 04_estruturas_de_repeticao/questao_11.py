#"questão 11"
soma_salario = 0
media_salario = 0
soma_idade = 0
media_idade = 0
for i in range(10):
    salario = float(input("Insira o valor do seu salário: "))
    idade = int(input("Insira a sua idade: "))
    soma_salario += salario
    soma_idade += idade

media_salario = soma_salario/10
media_idade = soma_idade/10

print(f"Média das idade = {media_idade}\nMédia dos salários = {media_salario}")
