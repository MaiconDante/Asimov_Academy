from pathlib import Path
import os

caminho = Path(__file__)

def retorna_tamanho(caminho, profundidade):
    while profundidade != 1 or profundidade != 2:
        prof = int(input("Digite somente 1 ou 2 para niveis de profundidade:  -> "))
        if prof == 1 or prof == 2:
            escolha = 3
            while escolha < 0 or escolha > 2:
                escolha = int(input("Escolha o caminho desejado: [0]-/Users/maicondante/Downloads - [1]-/Users/maicondante - [2]-/Users"))
            caminho = caminho.parents[escolha]
            qtde = "*"*prof
            print("Nome   -- Tamanho")
            for diretorio in caminho.glob(f"{qtde}/*"):
                if diretorio.is_dir() and not diretorio.name.startswith("."):
                    tamanho = 0
                    tamanho += os.path.getsize(diretorio)
                    print(f"{diretorio.name} -- {(tamanho /1024 /1024):.5f} mb")
        print("------FIM------")
        break

retorna_tamanho(caminho, profundidade=0)