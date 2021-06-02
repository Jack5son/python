

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


