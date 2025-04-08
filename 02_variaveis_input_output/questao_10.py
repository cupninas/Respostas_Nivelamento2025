# Crie uma variável para armazenar o raio de um círculo. Calcule e exiba a área do círculo e o comprimento da circunferência.

raio = float(input('Digite o raio: '))
pi = 3.14

area = pi * raio ** 2
comprimento = 2 * pi * raio

print(f'A área do círculo é {area} e o comprimento da circunferência é {comprimento}.')
