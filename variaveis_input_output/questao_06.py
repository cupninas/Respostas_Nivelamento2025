# O setor de RH de uma empresa identificou que o salário médio bruto dos colaboradores é de R$5600,00.
# Em média, os descontos chegam a 15% desse valor. Calcule e exiba o salário médio líquido dos colaboradores.
salario_bruto = 5600.00
percentual_descontos = 15 / 100
descontos = salario_bruto * percentual_descontos
salario_liquido = salario_bruto - descontos

print(f"Salário médio: R${salario_bruto}")
print(f"Salário líquido: R${salario_liquido}")
