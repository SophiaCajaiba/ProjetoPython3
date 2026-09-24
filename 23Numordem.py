# Procedimento do exercício 23
def exercicio23():

    # Declarar variáveis
    global n1, n2, n3, n4

    # Entrada de dados
    n1 = int(input("Digite o primeiro valor: "))
    n2 = int(input("Digite o segundo valor: "))
    n3 = int(input("Digite o terceiro valor: "))
    n4 = int(input("Digite o quarto valor: "))

    # Verificar a posição do quarto número
    if n4 < n1:
        print(n4, n1, n2, n3)

    elif n4 < n2:
        print(n1, n4, n2, n3)

    elif n4 < n3:
        print(n1, n2, n4, n3)

    else:
        print(n1, n2, n3, n4)


# Parte principal
def main():
    exercicio23()


# Chamada da função principal
main()