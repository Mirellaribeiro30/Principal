def situacao(nota1, nota2, nota3):
    media= (nota1 + nota2 + nota3) / 3
    if media>= 60:
        return "Aprovado"
    else:
        return "Reprovado"
    
nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
nota3 = float(input("Digite a terceira nota: "))
    
resultado = situacao(nota1, nota2, nota3)
print(f"O aluno está {resultado}.")
