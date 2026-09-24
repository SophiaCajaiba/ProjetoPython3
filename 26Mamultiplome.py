# Procedimento do exercício 26
def exercicio26():

    # Declarar variáveis
    global numero1, numero2, maior, menor

    # Entrada de dados
    numero1 = int(input("Digite o primeiro número: "))
    numero2 = int(input("Digite o segundo número: "))

    # Verificar o maior e o menor
    if numero1 > numero2:
        maior = numero1
        menor = numero2
    else:
        maior = numero2
        menor = numero1

    # Verificar se o maior é múltiplo do menor
    if maior % menor == 0:
        print("O maior número é múltiplo do menor.")
    else:
        print("O maior número não é múltiplo do menor.")


# Parte principal
def main():
    exercicio26()


# Chamada da função principal
main()