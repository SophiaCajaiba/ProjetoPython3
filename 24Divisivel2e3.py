# Procedimento do exercício 24
def exercicio24():

    # Declarar variáveis
    global numero

    # Entrada de dados
    numero = int(input("Digite um número inteiro: "))

    # Verificar se é divisível por 2 e 3
    if numero % 2 == 0 and numero % 3 == 0:
        print("O número é divisível por 2 e 3.")
    else:
        print("O número não é divisível por 2 e 3.")


# Parte principal
def main():
    exercicio24()


# Chamada da função principal
main()