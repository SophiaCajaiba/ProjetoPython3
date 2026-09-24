# Procedimento do exercício 27
def exercicio27(voltas, extensao, tempo):

    # Calcular distância total
    distancia = voltas * extensao

    # Converter metros para quilômetros
    distancia_km = distancia / 1000

    # Converter minutos para horas
    tempo_horas = tempo / 60

    # Calcular velocidade média
    velocidade = distancia_km / tempo_horas

    # Mostrar resultado
    print("Velocidade média:", velocidade, "km/h")


# Parte principal
def main():

    # Declarar variáveis
    voltas = int(input("Digite o número de voltas: "))
    extensao = float(input("Digite a extensão do circuito em metros: "))
    tempo = float(input("Digite o tempo de duração em minutos: "))

    # Chamar o procedimento passando os parâmetros
    exercicio27(voltas, extensao, tempo)


# Chamada da função principal
main()