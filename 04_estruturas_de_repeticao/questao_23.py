# FAÇA UM PROGRAMA QUE IMPLEMENTE UMA CAIXA REGISTRADORA. O PROGRAMA DEVERÁ RECEBER UM NÚMERO DESCONHECIDO DE VALORES REFERENTES
# À PREÇOS. UM VALOR ZERO INFORMADO PELO OPERADOR DEVE INDICAR O FINAL DA COMPRA. O PROGRAMA DEVE MOSTRAR O VALOR TOTAL E
# RECEBER O VALOR EM DINHEIRO DO PAGAMENTO. DEPOIS DEVE CALCULAR E MOSTRAR O VALOR DO TROCO.

num = float(input("Digite o preço: "))

valorTotal = 0

while num != 0:
    valorTotal += num
    print(f"O valor total está em: R$ {valorTotal}")
    num = float(input("Digite o preço: "))

print("Parando de adicionar itens...")

pagamento = float(input("Qual é o valor do pagamento?: "))

pagando = True

while pagando == True:
    if(pagamento <= 0):
        print("Valor inválido!")
        pagamento = float(input("Qual é o valor do pagamento?: "))
    
    elif(pagamento < valorTotal):
        print("Valor insuficiente!")
        pagamento = float(input("Qual é o valor do pagamento?: "))

    else:
        pagando = False
        troco = pagamento - valorTotal

print("Calculando troco...")
print(f"O valor total foi de: R${valorTotal}, o pagamento foi de: R${pagamento} e o troco é: R${troco}.")