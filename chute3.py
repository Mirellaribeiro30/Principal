print("********************************")
print("Bem vindo ao jogo de Adivinhação")
print("********************************")

numero_secreto= 40

chute = int(input("Digite um número: "))
print("Você digitou: ", chute)

if(numero_secreto == chute):
    print("Você acertou!")
else:
    if (chute > numero_secreto):
        print("Você errou! O seu chute foi maior que o número secreto.")
    else:
        print("Você errou! O seu chute foi menor que o número secreto.")

print("Fim de jogo")