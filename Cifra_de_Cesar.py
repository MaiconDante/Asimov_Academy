# Crie um código que implementa a "Cifra de César", isto é, que
# transforma um string movendo cada letra um certo número de
# passos no alfabeto. O número de passos é dado por uma chave.
# Letra com acentos, espaços e pontuação permanecem iguais.

# Exemplos:
# "abc" com chave 1 = "bcd"
# "ABCDE" com chave 2 = "CDEFG"
# "Cachorro" com chave -1 = "Bzbgnqqn"
# "Olá Mundo!" com chave 3 = "Roá Pxqgr!"

# DICA: construa 2 strings com as letras do alfabeto em ordem,
# um para letra minúsculas e outra para as maiúsculas, e use este
# string para guiar as substituições.

def cifra_de_cesar(texto, deslocamento, operacao):
    # Define a string de caracteres válidos (alfabeto)
    alfabeto_lower = "abcdefghijklmnopqrstuvwxyz"
    alfabeto_upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    # Inicializa o texto resultante
    texto_resultado = ""

    # Para cada caractere do texto
    for c in texto:
        if c in alfabeto_lower:
            # Encontra a posição da letra no alfabeto minúsculo
            indice = alfabeto_lower.index(c)
            # Se for criptografar, soma o deslocamento, se for descriptografar, subtrai
            if operacao == "criptografar":
                novo_indice = (indice + deslocamento) % 26
            else:
                novo_indice = (indice - deslocamento) % 26
            # Adiciona o novo caractere ao texto resultante
            texto_resultado += alfabeto_lower[novo_indice]
        
        elif c in alfabeto_upper:
            # Encontra a posição da letra no alfabeto maiúsculo
            indice = alfabeto_upper.index(c)
            # Se for criptografar, soma o deslocamento, se for descriptografar, subtrai
            if operacao == "criptografar":
                novo_indice = (indice + deslocamento) % 26
            else:
                novo_indice = (indice - deslocamento) % 26
            # Adiciona o novo caractere ao texto resultante
            texto_resultado += alfabeto_upper[novo_indice]
        
        else:
            # Se o caractere não for uma letra, adiciona-o diretamente ao texto resultante
            texto_resultado += c

    # Retorna o texto resultante
    return texto_resultado
    
print(cifra_de_cesar("Roá Pxqgr!", 3, ""))