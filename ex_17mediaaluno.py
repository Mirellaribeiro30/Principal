n1 = float(input("Digite a primeira nota: "))
n2 = float(input("Digite a segunda nota: "))
m = ((n1 + n2) / 2)

if m < 5.0:
    print("Média {}. Você foi REPROVADO.".format(m))
elif m > 6.9:
    print("Média {}. Você foi APROVADO".format(m))
else:
    print("Média {}. RECUPERAÇÃO.".format(m))