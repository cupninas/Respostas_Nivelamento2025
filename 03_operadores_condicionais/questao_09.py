# Em um parque de diversões, existe um brinquedo que não permite a entrada de crianças com altura inferior a 1.2m,
# permite a entrada de crianças com altura entre 1.2m e 1.5m caso estejam acompanhadas de um responsável
# e permite a entrada de crianças com altura maior que 1.5m.
# Faça um programa que receba a altura da criança e exiba a situação.

altura = float(input("Qual é a altura da criança?: "))

if(altura < 1.2):
    print("A criança não pode entrar...")

elif(altura >= 1.2 and altura < 1.5):
    print("A criança pode entrar apenas acompanhada.")

elif(altura >= 1.5):
    print("A criança pode entrar no brinquedo!!")

else:
    print("Altura inválida.")