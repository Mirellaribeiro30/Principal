import os
import time

# Configurações do jogo
width = 40
height = 20
ball_pos = [width // 2, height // 2]
ball_dir = [1, 1]
paddle1_pos = height // 2  # Raquete do jogador 1
paddle2_pos = height // 2  # Raquete do jogador 2
score1 = 0
score2 = 0

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def draw():
    clear_screen()
    print(f"Score: Jogador 1: {score1} | Jogador 2: {score2}")
    for y in range(height):
        for x in range(width):
            if (x == 0 and y in range(paddle1_pos - 1, paddle1_pos + 2)) or (x == width - 1 and y in range(paddle2_pos - 1, paddle2_pos + 2)):
                print('|', end='')
            elif x == ball_pos[0] and y == ball_pos[1]:
                print('O', end='')
            else:
                print(' ', end='')
        print()

def update():
    global ball_pos, ball_dir, paddle1_pos, paddle2_pos, score1, score2

    # Atualiza a posição da bola
    ball_pos[0] += ball_dir[0]
    ball_pos[1] += ball_dir[1]

    # Colisão com o topo e o fundo
    if ball_pos[1] <= 0 or ball_pos[1] >= height - 1:
        ball_dir[1] *= -1

    # Colisão com raquetes
    if ball_pos[0] == 0 and paddle1_pos - 1 <= ball_pos[1] <= paddle1_pos + 1:
        ball_dir[0] *= -1
        score1 += 1
    elif ball_pos[0] == width - 1 and paddle2_pos - 1 <= ball_pos[1] <= paddle2_pos + 1:
        ball_dir[0] *= -1
        score2 += 1
    elif ball_pos[0] < 0:
        print("Jogador 2 ganhou!")
        return False
    elif ball_pos[0] >= width:
        print("Jogador 1 ganhou!")
        return False

    return True

def main():
    global paddle1_pos, paddle2_pos
    while True:
        draw()
        if not update():
            break

        # Movimento da raquete do jogador 1
        command1 = input("Jogador 1 (w/s): ").strip().lower()
        if command1 == 'w' and paddle1_pos > 1:
            paddle1_pos -= 1
        elif command1 == 's' and paddle1_pos < height - 2:
            paddle1_pos += 1

        # Movimento da raquete do jogador 2
        command2 = input("Jogador 2 (↑/↓): ").strip().lower()
        if command2 == 'up' and paddle2_pos > 1:
            paddle2_pos -= 1
        elif command2 == 'down' and paddle2_pos < height - 2:
            paddle2_pos += 1

        time.sleep(0.1)

if __name__ == "__main__":
    main()