import random


def jogar():  # Função

    print("*********************************")
    print("Bem vindo ao jogo de Adivinhação!")
    print("*********************************")

    # Variáveis
    numero_secreto = round(random.randrange(1, 101))  # Random de 1 a 100
    tentativas = 0  # Inicia com 0, aumenta baseado no nível
    pontos = 1000  # Inicia com 1000 e diminui baseado nos erros

    # Nível
    print("Qual o nível de dificuldade?")
    print("(1) Fácil, (2) Médio, (3) Difícil")
    nivel = 0
    while nivel < 1 or nivel > 3:
        nivel = int(input("Defina o nível: "))
        if nivel == 1:
            tentativas = 20
        elif nivel == 2:
            tentativas = 10
        elif nivel == 3:
            tentativas = 5
        else:
            print("O nível deve ser 1, 2 ou 3!")

    # Chute
    for rodada in range(1, tentativas + 1):
        print("Tentativa {} de {}".format(rodada, tentativas))
        chute = int(input("Digite um número entre 1 e 100: "))
        if (chute < 1 or chute > 100):
            print("Você deve digitar um número entre 1 e 100!")
            continue  # Inicia uma nova iteraçao do laço

        # Condições
        acertou = chute == numero_secreto
        maior = chute > numero_secreto

        if acertou:
            print("Você acertou e fez {} pontos!".format(pontos))
            break  # Encerra o laço
        else:
            pontos_perdidos = abs(numero_secreto - chute)  # 40-60 = 20
            pontos = pontos - pontos_perdidos
            if maior:
                print("Você errou! O seu chute foi maior que o número secreto.")
            else:
                print("Você errou! O seu chute foi menor que o número secreto.")
            if rodada == tentativas:
                print("O número secreto era {}. Você fez {} pontos.".format(numero_secreto, pontos))

    print("Fim do jogo")


if __name__ == "__main__":
    jogar()
