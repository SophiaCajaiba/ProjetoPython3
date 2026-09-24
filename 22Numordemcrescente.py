# Procedimento do exercício 22
def exercicio22():

    # Declarar variáveis
    global valor1, valor2

    # Entrada de dados
    valor1 = int(input("Digite o primeiro valor: "))
    valor2 = int(input("Digite o segundo valor: "))

    # Verificar a ordem crescente
    if valor1 < valor2:

        # Mostrar resultado
        print(valor1, valor2)
    else:

        # Mostrar resultado
        print(valor2, valor1)


# Parte principal
def main():
    exercicio22()


# Chamada da função principal
main()