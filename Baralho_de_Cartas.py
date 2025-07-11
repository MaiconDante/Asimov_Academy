# Crie um código que simula um baralho de cartas.
# O código deve conter as seguintes funções:

# gerar_baralho -> retorna um baralho novo. Parâmetros da função
# definem quantas cópias retornar (1 baralho, 2 baralhos, ...),
# se o baralho deve conter coringas, e se deve ser embaralhado
# antes de ser retornado.

# mostrar_baralho -> exibe a quantidade de cartas no baralho e
# mostra quais são.

# dar_as_cartas -> distribui as cartas do baralho entre X
# jogadores, de forma que cada jogador recebe Y cartas.

# mostrar_jogadores -> exibe a quantidade de cartas na mão de
# cada jogador e mostra quais são.

# A partir dessas funções, o código deve:
# - gerar o baralho e exibi-lo
# - dar as cartas para os jogadores
# - exibir o baralho após as cartas terem sido distribuídas
# - exibir a mão de cada jogador

# DICA: utilize os símbolos ♠ ♥ ♦ ♣ para representar os naipes.
# DICA: utilize a função random.shuffle (módulo random) para embaralhar.

import random

def gerar_baralho():
    # Baralho padrão sem coringas
    baralho = [
        "|♠2|", "|♠3|", "|♠4|", "|♠5|", "|♠6|", "|♠7|", "|♠8|", "|♠9|", "|♠10|", "|♠J|", "|♠Q|", "|♠K|", "|♠A|",
        "|♥2|", "|♥3|", "|♥4|", "|♥5|", "|♥6|", "|♥7|", "|♥8|", "|♥9|", "|♥10|", "|♥J|", "|♥Q|", "|♥K|", "|♥A|",
        "|♦2|", "|♦3|", "|♦4|", "|♦5|", "|♦6|", "|♦7|", "|♦8|", "|♦9|", "|♦10|", "|♦J|", "|♦Q|", "|♦K|", "|♦A|",
        "|♣2|", "|♣3|", "|♣4|", "|♣5|", "|♣6|", "|♣7|", "|♣8|", "|♣9|", "|♣10|", "|♣J|", "|♣Q|", "|♣K|", "|♣A|",
    ]
    
    coringas = ["||", "||"]  # Coringas

    # Pergunta se quer adicionar coringas ao baralho
    coringas_baralho = input("\nGostarias de adicionar cartas coringas ao baralho? Digite S para sim ou N para não: -> ").lower()
    if coringas_baralho == "s":
        baralho.extend(coringas)
    
    # Pergunta quantos baralhos o usuário quer gerar
    qtde_baralho = int(input("\nQuantos jogos de baralho você gostaria de ter? -> "))
    
    baralho_completo = []
    for _ in range(qtde_baralho):
        baralho_completo.extend(baralho.copy())  # Repete o baralho conforme a quantidade de cópias
    
    # Pergunta se deseja embaralhar o baralho
    embaralhar_baralho = input("\nGostarias de embaralhar os baralhos? Digite S para sim ou N para não: -> ").lower()
    if embaralhar_baralho == "s":
        random.shuffle(baralho_completo)
    
    return baralho_completo

def mostrar_baralho(cartas):
    print("\n|---------------> MOSTRAR INFORMAÇÕES DO BARALHO <---------------|")
    print(f"A quantidade de cartas no baralho é: {len(cartas)}")
    print("-" * 62)
    print("*" * 149)
    print(cartas)
    print("*" * 149)

def dar_as_cartas(cartas):
    # Pergunta quantos jogadores participarão
    jogadores = int(input("\nQuantos jogadores jogarão? -> "))
    
    lista_jogadores = [[] for _ in range(jogadores)]
    
    # Pergunta quantas cartas cada jogador deve receber
    qtde_cartas_jogadores = int(input("\nQuantas cartas cada jogador deve receber? -> "))
    
    # Calcula o total de cartas que serão distribuídas
    total_cartas_distribuidas = qtde_cartas_jogadores * jogadores
    
    # Valida se há cartas suficientes no baralho
    while total_cartas_distribuidas > len(cartas):
        print(f"\nERRO: O baralho só possui {len(cartas)} cartas restantes.")
        qtde_cartas_jogadores = int(input("\nDigite novamente quantas cartas cada jogador deve receber: -> "))
        total_cartas_distribuidas = qtde_cartas_jogadores * jogadores
    
    # Distribui as cartas para os jogadores
    for j in range(jogadores):
        for _ in range(qtde_cartas_jogadores):
            carta = cartas.pop(random.randint(0, len(cartas) - 1))  # Remove uma carta aleatória do baralho
            lista_jogadores[j].append(carta)
    
    return lista_jogadores

def mostrar_jogadores(lista_jogadores):
    print("\n|---------------> MÃO DE CADA JOGADOR <---------------|")
    for i, jog in enumerate(lista_jogadores):
        print(f"Jogador {i + 1} possui {len(jog)} cartas: -> {', '.join(jog)}")

def main():
    # Gerar e mostrar o baralho
    cartas = gerar_baralho()
    mostrar_baralho(cartas)
    
    # Dar as cartas aos jogadores
    jogadores = dar_as_cartas(cartas)
    
    # Mostrar as cartas restantes no baralho
    mostrar_baralho(cartas)
    
    # Mostrar a mão de cada jogador
    mostrar_jogadores(jogadores)

main()