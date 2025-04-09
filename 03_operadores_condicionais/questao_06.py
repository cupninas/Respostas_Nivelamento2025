#Em um verdureiro, as maçãs custam R$0,50 por unidade e R$0,45 pelo menos 12 unidades são compradas. 
#Escreva um programa que leia o número de maçãs compradas, calcule e escreva o valor total da compra.

macas_compradas = int(input('informe quantas maçãs foram compradas:'))

if macas_compradas < 12: 
    valor_total = macas_compradas*0.50
else: 
    valor_total = macas_compradas*0.45
    
print(valor_total)
