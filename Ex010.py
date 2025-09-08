def calcular_situacao_aluno():
    notas = []
    for i in range(3):
        while True:
            try:
                nota = float(input(f"Digite a nota {i + 1}: "))
                if 0 <= nota <= 100:
                    notas.append(nota)
                    break
                else:
                    print("Nota inválida. Digite uma nota entre 0 e 100.")
            except ValueError:
                print("Entrada inválida. Digite um número.")

    media = sum(notas) / len(notas)

    if media >= 60:
        return "Aprovado"
    elif 50 <= media < 60:

        return "Recuperação"
    else:
        return "Reprovado"


situacao = calcular_situacao_aluno()
print(f"O aluno está {situacao}.")