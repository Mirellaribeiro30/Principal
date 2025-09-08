num = int(input ("Digite um número a ser convertido: \n"))
base = int(input('''escolha a base da conversao:
para binário digite 1
para octal digite 2
para hexadecimal digite 3
sua escolha: \n'''))
if base==1:
    print("conversao para binário")
    print("{} convertido para binário é: {}".format(num, bin(num)[2:]))
elif base==2:
    print("conversao para octal")
    print("{} convertido para octal é: {}".format(num, oct(num)[2:]))
elif base==3:
    print("conversao para hexadecimal")
    print("{} convertido para hexadecimal é: {}".format(num, hex(num)[2:]))
else:
    print("Por gentileza, escolha uma das opções acima ameba")