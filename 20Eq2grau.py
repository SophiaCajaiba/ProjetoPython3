import math


# Procedimento do exercício 20
def exercicio20():

    # Declarar variáveis
    global a, b, c, delta, x1, x2

    # Entrada de dados
    a = float(input("Digite o valor de A: "))
    b = float(input("Digite o valor de B: "))
    c = float(input("Digite o valor de C: "))

    # Calcular delta
    delta = b ** 2 - 4 * a * c

    # Verificar as raízes
    if delta < 0:
        print("Não existem raízes reais.")

    elif delta == 0:
        x1 = -b / (2 * a)

        # Mostrar resultado
        print("Existe uma raiz real:")
        print("x =", x1)

    else:
        x1 = (-b + math.sqrt(delta)) / (2 * a)
        x2 = (-b - math.sqrt(delta)) / (2 * a)

        # Mostrar resultado
        print("Existem duas raízes reais:")
        print("x1 =", x1)
        print("x2 =", x2)


# Parte principal
def main():
    exercicio20()


# Chamada da função principal
main()