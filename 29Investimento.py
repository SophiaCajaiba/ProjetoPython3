# Procedimento do exercício 29
def exercicio29(tipo, valor):

    # Verificar o tipo de investimento
    if tipo == 1:

        # Calcular rendimento da poupança
        valor_corrigido = valor * 1.03

        # Mostrar resultado
        print("Investimento: Poupança")
        print("Valor corrigido:", valor_corrigido)

    elif tipo == 2:

        # Calcular rendimento da renda fixa
        valor_corrigido = valor * 1.05

        # Mostrar resultado
        print("Investimento: Renda fixa")
        print("Valor corrigido:", valor_corrigido)

    else:

        # Mostrar mensagem de erro
        print("Tipo de investimento inválido.")


# Parte principal
def main():

    # Declarar variáveis
    tipo = int(input("Digite o tipo de investimento (1 ou 2): "))
    valor = float(input("Digite o valor do investimento: "))

    # Chamar o procedimento passando os parâmetros
    exercicio29(tipo, valor)


# Chamada da função principal
main()