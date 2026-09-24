# Procedimento do exercício 19
def exercicio19():

    # Declarar variáveis
    global valor1, valor2, maior

    # Entrada de dados
    valor1 = float(input("Digite o primeiro valor: "))
    valor2 = float(input("Digite o segundo valor: "))

    # Verificar o maior
    if valor1 > valor2:
        maior = valor1
    else:
        maior = valor2

    # Mostrar resultado
    print("O maior valor é:", maior)


# Parte principal
def main():
    exercicio19()


# Chamada da função principal
main()