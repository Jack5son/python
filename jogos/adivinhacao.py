import random
print("################################")
print("Bem vindo ao jogo de adivinhação!")
print("################################")

# usuario tem 3 tentativas para execução
tentativas = 5
numero_secreto = int(round(random.random() * 100))

chute = 0

acertou = False
maior = False

while tentativas > 0:
    print("Restam {} tentativas".format(tentativas))
    chute = int (input("Digite um numero entre 1 e 100: "))
    print("Você digitou:", chute)
    acertou = chute == numero_secreto
    maior   = chute > numero_secreto

    if chute < 1 or chute > 100:
        print("Ops, digite um numero entre 1 e 100")
        continue

    if (acertou):
        print("Você acertou!!!")
        print("O numero correto é: " + str(numero_secreto))
        break
    else:
        tentativas = tentativas - 1
        print("Não foi dessa vez :(")
        if (tentativas == 0):
            print("O numero correto era: " + str(numero_secreto))
            break
        if(maior):
            print("Tente um numero mais baixo!")
        else:
            print("Tente um numero mais alto")

print("Fim do jogo!")