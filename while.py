print("")
print("********************************")
print("Bem vindo ao jogo de Adivinhação")
print("********************************")

numero_secreto = 40
total_de_tentativas = 3
rodada = 1

while (rodada <= total_de_tentativas):
    print("Tentativa", rodada, "de", total_de_tentativas)
    chute = int(input("Digite um número: "))
    print("Você digitou: ", chute)
    rodada = rodada + 1


    if (numero_secreto == chute):
        print("Você acertou!")
    else:
        if (chute > numero_secreto):
            print("Você errou! O seu chute foi maior que o número secreto.")
        else:
            print("Você errou! O seu chute foi menor que o número secreto.")

print("")

print("Fim de jogo!")