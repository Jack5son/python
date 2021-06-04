print("################################")
print("Bem vindo ao jogo de adivinhação!")
print("################################")

numero_secreto = 28
chute = int (input("Digite o seu numero: "))

print("Você digitou:", chute)

acertou = chute == numero_secreto
maior   = chute > numero_secreto

if (acertou):
    print("Você acertou!!!")
else:
    print("Não foi dessa vez :(")
    if(maior):
        print("Tente um numero mais baixo!")
    else:
        print("Tente um numero mais alto")

print("Fim do jogo!")