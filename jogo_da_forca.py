import random

palavras = ['banana', 'mesa']
palavra_escolhida = random.choice(palavras)
numero_letras = len(palavra_escolhida)

# para avaliar se está tudo certo
print(palavra_escolhida)

# Inicialização da lista de "_"
lugar_para_encontrar = ["_" for _ in range(numero_letras)]

tentativas = 6
contador_erros = 0

print(f'Você só pode errar {tentativas} vezes até acertar a palavra!')
print(" ".join(lugar_para_encontrar))  # Transforma a lista em uma string para exibição

lista_correta = []

while contador_erros < tentativas and lugar_para_encontrar != list(palavra_escolhida):
    letra_escolhida = input('Escolha uma letra: ')
    if letra_escolhida in palavra_escolhida:
        lista_correta.append(letra_escolhida)
        indices = [i for i, letra in enumerate(palavra_escolhida) if letra == letra_escolhida]
        for indice in indices:
            lugar_para_encontrar[indice] = letra_escolhida
        print(" ".join(lugar_para_encontrar))
    else:
        contador_erros = contador_erros + 1
        print('Você errou, tente outra letra')

if contador_erros >= tentativas:
    print(f'Você perdeu! A palavra era "{palavra_escolhida}".')
else:
    print('Você acertou!')