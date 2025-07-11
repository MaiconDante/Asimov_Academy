# Desafio - Crie um programa que:
# - Pede por um nome de usuário e uma senha.
# - Se ambos forem corretos, exibe uma mensagem de sucesso.
# - Caso contrário, exibe uma mensagem de erro. A mensagem é diferente quando o usuário está incorreto, e quando a senha está incorreta.
# - O usuário/senha "corretos" podem ser definidos como variávies dentro do próprio código.

import os

os.system('cls' if os.name == 'nt' else 'clear')
print()
registered_user = "maicon"
registered_password = "1234"

while True:
    print()
    print("|--> SISTEMA DE LOGIN <--|")
    print()
    user = input("Digite o USUÁRIO: ").lower()
    password = input("Digite a SENHA: ")

    if user == registered_user and password == registered_password:
        print("-"*50)
        print("| LOGIN EFETUADO COM SUCESSO |")
        print("-"*50)
        break
    elif user != registered_user and password == registered_password:
        print("-"*50)
        print("| O seu usuário está INCORRETO |")
        print("-"*50)
    elif user == registered_user and password != registered_password:
        print("-"*50)
        print("| A sua senha está INCORRETA |")
        print("-"*50)
    else:
        print("-"*50)
        print("| Usuário e senha INCORRETOS |")
        print("-"*50)