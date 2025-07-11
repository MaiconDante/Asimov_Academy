# Desafio - Crie um programa que:
# - Escolhe um número secreto.
# - Pede por um chute do usuário.
# - Indica se o usuário acertou ou não.
# - Se não acertou, dá uma dica, dizendo se o número é mais alto ou mais baixo.
# - Repete isso até 3 vezes!

import os
import random

os.system('cls' if os.name == 'nt' else 'clear')
number_secret = random.randint(1,10)

print()
for i in range(1,4):
    print("----> ADVINHE O NÚMERO SECRETO <----")
    guess = int(input("Digite um número de 1 a 10 para sua resposta -> "))

    if guess == number_secret:
        print("="*50)
        print("Você |acertou| o NÚMERO SECRETO")
        print(f"O número secreto era {number_secret} e acertou na {i}ª tentativa")
        print("="*50)
        break
    elif guess < number_secret:
        print("="*50)
        print("Você |errou| o NÚMERO SECRETO")
        print(f"O número secreto é mais alto e você usou {i}ª tentativa")
        print("="*50)
    else:
        print("="*50)
        print("Você |errou| o NÚMERO SECRETO")
        print(f"O número secreto é mais baixo e você usou {i}ª tentativa")
        print("="*50)

    if i == 3:
        print("="*50)
        print("Suas TENTATIVAS SE ESGOTARAM")
        print(f"O Total de {i}ª tentativas")
        print("="*50)
        break