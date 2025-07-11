# Desafio - Crie um programa que:
# - Pede pelo seu nome e idade.
# - Dá oi para você.
# - Conta quantas letras seu nome possui.
# - Fala quantos anos você terá daqui a 5 anos.

import os

os.system('cls' if os.name == 'nt' else 'clear')
print()
name = input("Digite seu nome: -> ")
age = int(input("Digite sua idade: -> "))
print()
print("="*80)
print(f"Oi, seja bem vindo a programação, {name}, você possui {age} anos")
print(f"Seu nome possui {len(name)} letras")
print(f"Daqui a 5 anos você terá {age + 5} anos")
print("="*80)
print()