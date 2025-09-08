numero_secreto= 42
chute_str = input("Digite um número: ")
chute = int(chute_str)
print("Você digitou: ", chute)
if(numero_secreto==chute):
    print("Você acertou!")
else:
    print("Você errou")
    print("Fim de jogo")