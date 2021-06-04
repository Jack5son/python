
'''
#Teste IF

a = int (input("Digite o valor de a: "))
b = 150
c = 151

if (a == b):
    print("São Iguai!")
else:
    print("São diferentes")

if (a > b and a > c):
    print("a é maior que b e c")
elif (b > c ):
    print("b é maior que a e c")
else:
    print("c é maior que a e b")


exercicio = int(input("Quantos minutos você se exercita por dia: "))

if (exercicio < 30):
    print("VocÊ devia se exercitar mais..")
elif ( exercicio >= 30 and exercicio <= 60):
    print("Você esta no caminho, Continue assim!")
elif (exercicio > 60 and exercicio <= 120):
    print("Você é um atleta nato! Parabens")
else:
    print("Você é galatico!")

#Teste LOOPS

trabalho = input("Você vai trabalhar hoje? ")
dia = input("O dia esta bonito? ")
preguica = input("Você esta com preguiça bb? ")

if trabalho == "sim":
    print("Que pena")
elif (trabalho == "não"):
    print("Obaa, aproveite o dia")

if trabalho == "não" and dia == "sim":
    print("Aproveite para pedalar")
elif trabalho == "não" and dia == "não":
    print("Aproveite para assistir um filme :)")

if trabalho == "não" and preguica == "sim":
    print("Aproveite para dormir mais nenem")
elif trabalho == "não" and preguica == "não":
    print("Boaa, aproveite para estudar Python *_* ")



# FOR
# FOR em listas

cor = ["vermelho","amarelo","azul","preto","branco","roxo"]

for x in cor:
    print(x)


#FOR em Strings

for y in 'pneumoultramicroscopicossilicovulcanoconiótico':
    print(y)

#FOR e break

numeros = (1,2,3,4,5,6,7,8,9,10)

for i in numeros:
    print(i)
    if i == 7:
        break

#While
#Faz um loop enquanto uma condição for verdadeira

i = 0
while i <= 10:
    print(i)
    i += 1

# while com break
u = 0
v = 0
while u <= 10:
    print(u)
    if u == 7:
        break
    u += 1

# while com continue
while v < 10:
    v += 1
    #Pula o 7
    if v == 7:
        continue
    print(v)

#Range
#Faz o loop a quantidade de vezes dedinida no range
# range(Incio,fim + 1, salto)
for x in range(1,31,2):
    print(x)

#def
#Funções em python
def soma (x,y):
    return x+y
print('a Soma de x e y é: ' + str(soma(1,2)))

#IMC
peso = float(input("Qual é o seu peso? "))
altura = float(input('Qual é sua altura? '))

def imc(p, a):
    imc = p/(a**2)
    if imc < 18.5:
        print("Você ta magro demais :)")
    elif imc > 18.5 and imc <= 24.9:
        print("Continue assim seu peso esta de acordo! *_*")
    elif imc >25.0 and imc <= 29.9:
        print("Sobrepeso :(")
    elif imc >30.0 and imc <= 39.9:
        print("Obsidade I :(")
    else:
        print("Obsidade II :(")

    print("Seu imc é de " + str(imc))
    return

imc(peso,altura)


#Funções lambda ( não precisa nomear as funções)

soma2 = lambda x,y: x+y
print(str(soma2(1,2)))

'''

#Modulos é um conjunto de funções
#Importar modulo
# import nome_do_modulo
# Importar partes de um modulo
# from math import sqrt
#usando os modulos
#nome_do_modulo.funcao()
#exemplo:
import math
raiz_quadrada = math.sqrt(9)
print(raiz_quadrada)

#pacote: Pacotes são conjuntos de modulos
#pip é o gerenciador de pacotes em python (Instalar, atualizar e desinstalar)

#instalar pacotes
#!pip install seaborn
#pip install seaborn

#atualizar pacotes
#pip --upgrade seaborn

#instalar versão especifica
#pip install seaborn==0.90

#importação e pacotes
#import pandas as pd
#import numpy as mp
# utiliza-se o as como alias para apelidar o pacote, para facilicar na hora de chamar







