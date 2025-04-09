# Uma loja oferece 5% de desconto para os clientes que pagarem utilizando cartão de crédito,
# Nenhum para quem utilizar o cartão de débito e 10% para quem utilizar Pix.
# Faça um programa que receba o valor da compra, a forma de pagamento e exiba o valor final da compra.

valor = int(input("Olá! Qual é o valor da compra?: "))

print("""Qual é a forma de pagamento?
      1 - Cartão de crédito (5% de desconto)
      2 - Cartão de débito
      3 - PIX (10% de desconto)""")

forma = int(input("Qual é a forma de pagamento?: "))

if(forma == 1):
    total = valor - valor * 0.05
    print(f"O valor total é: R${total}")

elif(forma == 2):
    print(f"O valor total é: R${valor}")

elif(forma == 3):
    total = valor - valor * 0.1
    print(f"O valor total é: R${total}")

else:
    print("Escolha inválida!")