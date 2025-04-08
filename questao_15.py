#Faça um programa que receba via teclado o seu nome, sua idade e seu curso e exiba no formato: “Olá, [nome]! Você tem [idade] anos e faz [curso]!”.

nome = input("Qual é o seu nome? ")
idade = int(input("Qual é a sua idade? "))
curso = input("Qual é o seu curso?")

print(f"Olá, {nome}! Você tem {idade} anos e faz {curso}!")