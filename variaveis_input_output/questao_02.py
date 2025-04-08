# Crie um programa que recebe dois valores e depois troca os valores entre eles. 

a = int(input('informe um valor:'))
b = int(input('informe outro valor:'))

c = b  
b = a 
a = c 

print(f'A = {a}\nB = {b}')
