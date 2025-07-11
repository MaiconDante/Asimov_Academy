# Crie um "jogo dos estados". Neste jogo, o jogador precisa responder o nome da capital de cada Estado do Brasil.
# O jogo deve perguntar ao usuário "Qual a capital do Estado X?", e checar se o usuário respondeu de forma correta.
# Após cada pergunta, o usuário pode escolher parar o jogo ou continuar para a próxima pergunta.
# Quando o usuário decidir parar, ou quando todas as perguntas forem respondidas, o código mostra o número bruto e porcentagem de acertos.

import time, sys

print("*" * 80)
print("|JOGO DOS ESTADOS|")
print("*" * 80)
print()

questions = {
    "Santa Catarina": "Florianopolis",
    "Acre": "Rio Branco",
    "Bahia": "Salvador",
    "Maranhão": "São Luis",
    "Rio de Janeiro": "Rio de Janeiro",
}

hits = 0
answer = 1
print("As perguntas irão INICIAR:")
print("Serão no total |5| perguntas")
time.sleep(2)

for state, capital in questions.items():
    response = input(f"\nPergunta {answer} -> Qual a capital do Estado do(a) {state} R: ").lower()
    answer += 1
    if response == capital.lower():
        print("-" * 50)
        print("Você acertou !!!")
        print("-" * 50)
        hits += 1
    else:
        print("-" * 50)
        print("Você errou !!!")
        print("-" * 50)

    if answer <= 5:
        exit = input("\nDeseja continuar? Digite S para SIM ou N para NÃO R: ").lower()
        if exit == "s" and answer <= 5:
            print("\nVamos para a próxima pergunta...")
            time.sleep(2)
            continue
        elif exit == "n":
            print("*" * 80)
            print(f"Você acertou {hits} de {len(questions)} perguntas.")
            print("*" * 80)
            break
        else:
            while True:
                exit = input("\nDigite apenas S para SIM ou N para NÃO R: ").lower()
                if exit == "s" and answer <= 5:
                    break 
                elif exit == "n":
                    print("*" * 80)
                    print(f"Você acertou {hits} de {len(questions)} perguntas.")
                    print("*" * 80)
                    print("\n")
                    sys.exit()
                else:
                    print("\nOpção inválida! Digite apenas 'S' para SIM ou 'N' para NÃO.")
        print("\nVamos para a próxima pergunta...")
    else:
        print("*" * 80)
        print(f"Você acertou {hits} de {len(questions)} perguntas.")
        print("*" * 80)
        print("\n")
        sys.exit()
        time.sleep(2)