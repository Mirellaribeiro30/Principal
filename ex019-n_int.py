import math

num = float(input("digite um número real: "))
print("o valor digitado é {} e a sua porção inteira é {}".format(num, int(num)))

print("o valor digitado é {} e a sua porção inteira é {}".format(num, math.ceil(num)))

print("o valor digitado é {} e a sua porção inteira é {}".format(num, math.trunc(num)))

print("o valor digitado é {} e a sua porção inteira é {}".format(num, math.floor(num)))
