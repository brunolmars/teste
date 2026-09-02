Numeber  = int(input("Digite o primeiro numero: "))
Numeber1  = int(input("Digite o segundo numero: "))

operadorUsado = int(input("Digite o operador, sendo 1: soma, 2:subtração, 3: adicão, 4;multiplicação, 5:divisao, 6:pontencializacao  "))
print("caso deseja sair digite zero ou 7 ")

while operadorUsado < 7 and operadorUsado > 0:
    if operadorUsado == 1:
        print(Numeber + Numeber1)

    elif operadorUsado == 2:
        print(Numeber - Numeber1)

    elif operadorUsado == 3:
        print(Numeber * Numeber1)

    elif operadorUsado == 4:
        print(Numeber / Numeber1)

    elif operadorUsado == 5:
        print(Numeber ** Numeber1)

    else:
        print("Operador invalido")

    operadorUsado = int(input("Digite o operador, sendo 1: soma, 2:subtração, 3: adicão, 4;multiplicação, 5:divisao, 6:pontencializacao  "))

print("programa encerrado")
