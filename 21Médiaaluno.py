# Procedimento do exercício 21
def exercicio21():

    # Declarar variáveis
    global nota1, nota2, nota3, nota4, media

    # Entrada de dados
    nota1 = float(input("Digite a primeira nota: "))
    nota2 = float(input("Digite a segunda nota: "))
    nota3 = float(input("Digite a terceira nota: "))
    nota4 = float(input("Digite a quarta nota: "))

    # Calcular média
    media = (nota1 + nota2 + nota3 + nota4) / 4

    # Mostrar média
    print("Média:", media)

    # Verificar situação do aluno
    if media >= 6:
        print("APROVADO")
    elif media >= 3:
        print("EXAME")
    else:
        print("RETIDO")


# Parte principal
def main():
    exercicio21()


# Chamada da função principal
main()