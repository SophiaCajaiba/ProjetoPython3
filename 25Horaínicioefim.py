# Procedimento do exercício 25
def exercicio25():

    # Declarar variáveis
    global hora_inicio, minuto_inicio
    global hora_fim, minuto_fim
    global inicio, fim, duracao, horas, minutos

    # Entrada de dados
    hora_inicio = int(input("Digite a hora de início: "))
    minuto_inicio = int(input("Digite o minuto de início: "))

    hora_fim = int(input("Digite a hora de término: "))
    minuto_fim = int(input("Digite o minuto de término: "))

    # Converter os horários para minutos
    inicio = hora_inicio * 60 + minuto_inicio
    fim = hora_fim * 60 + minuto_fim

    # Verificar se terminou no dia seguinte
    if fim <= inicio:
        fim = fim + 24 * 60

    # Calcular duração
    duracao = fim - inicio

    # Converter para horas e minutos
    horas = duracao // 60
    minutos = duracao % 60

    # Mostrar resultado
    print("Duração do jogo:", horas, "hora(s) e", minutos, "minuto(s).")


# Parte principal
def main():
    exercicio25()


# Chamada da função principal
main()