#FAÇA UM PROGRAMA QUE RECEBA UM ANO INICIAL E UM ANO FINAL. EXIBA OS ANOS BISSEXTOS ENTRE ESSES 2 ANOS.

ano_inicial = int(input("Digite o ano inicial: "))
ano_final = int(input("Digite o ano final: "))

print(f"Anos bissextos entre {ano_inicial} e {ano_final}: ")
for ano in range(ano_inicial, ano_final + 1):
    if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0):
        print(ano)
