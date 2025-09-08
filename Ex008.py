import random
def gerar_número_roleta():
    return random.randint(1,60)
número_sorteado=gerar_número_roleta()
print(f"O número sorteado foi: {número_sorteado}")