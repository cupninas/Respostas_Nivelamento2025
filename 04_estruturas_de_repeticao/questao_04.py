# FAÇA UM PROGRAMA QUE RECEBA DOIS NÚMEROS (X E Y). RETORNE TODOS OS NÚMEROS ENTRE 0 E X**Y.

x = int(input('informe um valor:'))
y = int(input('informe outro valor:'))

for i in range(0,x**y+1): 
    print(i)
