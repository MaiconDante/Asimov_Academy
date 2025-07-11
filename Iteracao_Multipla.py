# Dado duas listas, printe todos os valores que aparecerem duplicados nas duas listas.

import os

os.system('cls' if os.name == 'nt' else 'clear')
print()
list_1 = [1,2,3,8,9,0]
list_2 = [1,2,3,4,5,6]
list_duplicates = []

for n1 in list_1:
    for n2 in list_2:
        if n1 == n2:
            list_duplicates.append(n1)

print("+"*80)
print("Lista dos valores DUPLICADOS nas duas listas")
print(list_duplicates)
print("+"*80)
print()

# Dado duas listas, printe uma mensagem dizendo se existe algum elemento em comum entre elas ou não.

list_1 = [1,2,3,8,9,0]
list_2 = [1,2,3,4,5,6]

status = False

for n1 in list_1:
    for n2 in list_2:
        if n1 == n2:
            status = True

if status:
    print("+"*80)
    print("As duas listas possuem elementos em comum !!!")
    print("+"*80)
    print()
else:
    print("+"*80)
    print("As duas listas Não possui elementos em comum !!!")
    print("+"*80)
    print()