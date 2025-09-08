'''
- até 10 anos: mirim
- até 14 anos: infantil
- até 19 anos: júnior
- até 48 anos: senior
- acima de 48: master
'''
from datetime import date

atual = date.today().year
nasc = int(input("Ano de nascimento do(a) nadador(a): \n"))
idade = atual - nasc
print("O atleta tem {} anos em {}.".format(idade, atual))

if idade <= 10:
    print("Classificação: Mirim.".format(idade))
elif idade <= 14:
    print("Classificação: Infantil.".format(idade))
elif idade <= 19:
    print("Classificação: Júnior.".format(idade))
elif idade <= 48:
    print("Classificação: Senior.".format(idade))
else:
    print("Classificação: Master.".format(idade))