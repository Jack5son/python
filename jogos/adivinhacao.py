print("################################")
print("Bem vindo ao jogo de adivinhação!")
print("################################")

# usuario tem 3 tentativas para execução
tentativas = 5
numero_secreto = 28
chute = 0

acertou = False
maior = False

while acertou == False and tentativas > 0:
    chute = int (input("Digite o seu numero: "))
    print("Você digitou:", chute)
    acertou = chute == numero_secreto
    maior   = chute > numero_secreto

    if (acertou):
        print("Você acertou!!!")
    else:
        tentativas = tentativas - 1
        print("Não foi dessa vez :(")
        if(maior):
            print("Tente um numero mais baixo!")
        else:
            print("Tente um numero mais alto")
        print("Restam" ,tentativas , "tentativas")

print("Fim do jogo!")