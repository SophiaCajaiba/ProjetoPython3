# Procedimento do exercício 18
def exercicio18():

    # Declarar variáveis
    global valor1, valor2, diferenca

    # Entrada de dados
    valor1 = int(input("Digite o primeiro valor: "))
    valor2 = int(input("Digite o segundo valor: "))

    # Calcular a diferença
    if valor1 > valor2:
        diferenca = valor1 - valor2
    else:
        diferenca = valor2 - valor1

    # Mostrar resultado
    print("A diferença do maior pelo menor é:", diferenca)


# Parte principal
def main():
    exercicio18()


# Chamada da função principal
main()