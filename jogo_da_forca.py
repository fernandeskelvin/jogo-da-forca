import random
import os
from time import sleep

nome_usuario = input('Olá, qual é o seu nome? ')
print(f'\nOlá, {nome_usuario}! Seja Bem-vinda(o) ao Jogo da Forca!\U0001F600 \n\n')

palavras = ['baleia', 'xadrez', 'formiga', 'cruzeiro', 'mesa']
palavra_escolhida = random.choice(palavras)
numero_letras = len(palavra_escolhida)

# para avaliar se está tudo certo
'''print(palavra_escolhida)'''

siga = input(f'Sua palavra tem {numero_letras} letras!\n\nPressione qualquer tecla para iniciar o jogo ...')

os.system('cls' if os.name == 'nt' else 'clear')

# Inicialização da lista de "_"
lugar_para_encontrar = ["_" for _ in range(numero_letras)]

tentativas = 6
contador_erros = 0

lista_correta = []
lista_errada = []

def painel():
    os.system('cls' if os.name == 'nt' else 'clear')
    print(f'Você só pode errar {tentativas} vezes até acertar a palavra!\n')
    print(" ".join(lugar_para_encontrar))
    letra_escolhida = input('\nEscolha uma letra: ')
    return letra_escolhida

def painel_errado():
    os.system('cls' if os.name == 'nt' else 'clear')
    print(f'Você só pode errar {tentativas} vezes até acertar a palavra!\n')
    print(" ".join(lugar_para_encontrar))
    print('\n\nLetras erradas: ' + ' - '.join(lista_errada))
    letra_escolhida = input('\nEscolha uma letra: ')
    return letra_escolhida

while contador_erros < tentativas and lugar_para_encontrar != list(palavra_escolhida):
    if tentativas == 6:
      letra_escolhida = painel()
    else:
       letra_escolhida = painel_errado()
    if letra_escolhida in palavra_escolhida:
        print('Woow! Essa letra existe na sua palavra!')
        sleep(3)
        lista_correta.append(letra_escolhida)
        indices = [i for i, letra in enumerate(palavra_escolhida) if letra == letra_escolhida]
        for indice in indices:
            lugar_para_encontrar[indice] = letra_escolhida
    elif letra_escolhida not in palavra_escolhida:
        print('Você errou, esta letra não tem na palavra')
        sleep(3)
        tentativas = tentativas - 1
        lista_errada.append(letra_escolhida)
        indices = [i for i, letra in enumerate(palavra_escolhida) if letra == letra_escolhida]
        for indice in indices:
            lista_errada[indice] = letra_escolhida
    else:
        contador_erros = contador_erros + 1
        print('Você errou, tente outra letra')
if contador_erros >= tentativas:
    os.system('cls' if os.name == 'nt' else 'clear')
    print(f'Você perdeu!\nA palavra era "{palavra_escolhida}".')
else:
    os.system('cls' if os.name == 'nt' else 'clear')
    print(f'Parabéns! Você acertou a palavra!\n\nA palavra era {palavra_escolhida}!\n')