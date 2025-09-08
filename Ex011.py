def situacao(nota1, nota2, nota3):
    media = (nota1 + nota2 + nota3) / 3
    if media >= 60:
        return "Aprovado"
    elif 50 <= media < 60:

        return "Recuperação"
    else:
        return "Reprovado"

nota1 = float(input("digite a primeira nota: "))
nota2 = float(input("digite a segunda nota: "))
nota3 = float(input("digite a terceira nota: "))
resultado = situacao(nota1, nota2, nota3)
print(f"O aluno está {resultado}.")