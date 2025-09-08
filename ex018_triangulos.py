'''
- equilátero: todos os lados iguais
- isósceles: dois lados iguais
- escaleno: todos os lados diferentes
'''

a = float(input("Primeiro lado da forma: \n"))
b = float(input("Segundo lado da forma: \n"))
c = float(input("Terceiro lado da forma: \n"))

if (a + b > c) and (a + c > b) and (b + c > a):
    print("O triângulo que existe é um ", end="")
    if a == b == c:
        print("triângulo EQUILÁTERO.")
    elif (a == b) or (a == c) or (b == c):
        print("triângulo ISÓSCELES.")
    else:
        print("triângulo ESCALENO.")
else:
    print("O triângulo inexiste.")