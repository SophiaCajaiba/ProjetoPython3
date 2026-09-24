# Procedimento do exercício 28
def exercicio28(venda_mensal, preco_atual):

    # Declarar variável local
    preco_novo = preco_atual

    # Verificar as condições
    if venda_mensal < 500 and preco_atual < 30:
        preco_novo = preco_atual * 1.10

    elif venda_mensal >= 500 and venda_mensal < 1000 and preco_atual >= 30 and preco_atual < 80:
        preco_novo = preco_atual * 1.15

    elif venda_mensal >= 1000 and preco_atual >= 80:
        preco_novo = preco_atual * 0.95

    # Mostrar resultado
    print("Preço atual:", preco_atual)
    print("Preço novo:", preco_novo)


# Parte principal
def main():

    # Declarar variáveis
    venda_mensal = int(input("Digite a venda mensal: "))
    preco_atual = float(input("Digite o preço atual: "))

    # Chamar o procedimento passando os parâmetros
    exercicio28(venda_mensal, preco_atual)


# Chamada da função principal
main()