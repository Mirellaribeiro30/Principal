from random import choice
from time import sleep

choices_list = ["pedra", "papel", "tesoura"]
print("""
COMPUTADOR: Vamos jogar Pedra, Papel, Tesoura!
As regras são as seguintes:
- Papel vence Pedra e perde para Tesoura
- Pedra vence Tesoura e perde para Papel
- Tesoura vence Papel e perde para Pedra
""")

player_prompt = input("Você escolhe pedra, papel ou tesoura? \n").lower()

print("JO")
sleep(0.5)
print("KEN")
sleep(0.5)
print("PÔ!!!")

def judge(computer, player):
    print(f"""
Jogador: {player}
Computador: {computer}
""")

    # Verifica se a jogada do jogador é válida
    if player not in choices_list:
        print(f"{player} não é uma opção válida. Escolha pedra, papel ou tesoura!")
        return

    # Empate
    if computer == player:
        print("Empate. Vamos jogar novamente!")
        return

    # Definindo as regras de vitória
    if (player == "pedra" and computer == "tesoura") or \
       (player == "tesoura" and computer == "papel") or \
       (player == "papel" and computer == "pedra"):
        print(f"{player.capitalize()} vence {computer}. Jogador ganhou.")
    else:
        print(f"{computer.capitalize()} vence {player}. Computador ganhou.")

judge(choice(choices_list), player_prompt)
