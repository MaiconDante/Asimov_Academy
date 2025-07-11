# Dado uma sequência de números, calcule a soma e média dos números.
# ATENÇÃO: não vale usar a função sum() !

import os

os.system('cls' if os.name == 'nt' else 'clear')
sequence = int(input("Digite quantos números em sequencia você irá digitar: -> "))
print()

sum = 0
counter = 0
print("="*80)
for i in range(1, sequence+1):
    number = int(input(f"Digite o {i}ª número: ->"))
    sum += number
    counter+=1

print(f"A soma dos números digitados é {sum} e a média entre eles é {number / counter:.2f}")

print("="*80)

# Dado uma sequência de números, calcule o maior valor da sequência.
# ATENÇÃO: não vale usar a função max() !

sequence = int(input("Digite quantos números em sequencia você irá digitar: -> "))
print()

bigger = 0
print("="*80)
for i in range(1, sequence+1):
    number = int(input(f"Digite o {i}ª número: ->"))
    if i == 1:
        bigger = number
    if number > bigger:
        bigger = number

print(f"O maior número digitado é {bigger}")

print("="*80)

# Dado uma lista de palavras, printe todas as palavras que contém pelo menos 5 caracteres.

list_words = ["maicon", "amy", "andrea", "ze", "py", "python"]
print(list_words)
print()
print("Abaixo Nomes da lista que contem abaixo de 5 caracteres: ")
for caractere in list_words:
    if len(caractere) <= 5:
        print(caractere) 