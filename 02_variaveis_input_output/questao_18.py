# Faça um algoritmo que recebe o salário de um funcionário e o percentual de reajuste. calcule esse valor e mostre na tela o novo salário.

salario = float(input("Digite o salário do funcionário: "))
percentual_reajuste = float(input("Digite o percentual de reajuste: "))

aumento = salario * percentual_reajuste / 100
novo_salario = salario + aumento
print(f"O novo salário do funcionário é: R$ {novo_salario}")
