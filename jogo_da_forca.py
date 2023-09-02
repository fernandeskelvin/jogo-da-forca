import random
import os
from time import sleep

def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')

def mostrar_painel():
    limpar_tela()
    print(f'Você só pode errar {tentativas} vezes até acertar a palavra! \U0001f6a8\n')
    print(" ".join(lugar_para_encontrar))
    if len(lista_errada) != 0:
        print('\n\n\u274C Letras erradas: ' + ' - '.join(letra.upper() for letra in lista_errada))

palavras = ['banana', 'laranja', 'maça', 'uva', 'morango',
'abacaxi', 'limao', 'pera', 'kiwi', 'melancia', 'manga', 'goiaba',
'ameixa', 'cereja']

nome_usuario = input('Olá, qual é o seu nome? ')
print(f'\nOlá, {nome_usuario}! Seja Bem-vinda(o) ao Jogo da Forca! \U0001f609\n\n')

while True:
    palavra_escolhida = random.choice(palavras)
    numero_letras = len(palavra_escolhida)
    lugar_para_encontrar = ["_" for _ in range(numero_letras)]
    lista_correta = []
    lista_errada = []
    tentativas = 6
    contador_erros = 0

    print(f'Sua palavra tem {numero_letras} letras! \U0001f4a1\n')
    siga = input('Pressione Enter para iniciar o jogo ...')

    while contador_erros < tentativas and lugar_para_encontrar != list(palavra_escolhida):

        mostrar_painel()
        letra_escolhida = input('\n\U0001f449 Escolha uma letra: ').lower()

        if letra_escolhida in lugar_para_encontrar or letra_escolhida in lista_errada:
            print('Você já escolheu esta letra antes!')
            sleep(2)
            continue

        elif letra_escolhida in palavra_escolhida:
            print('Woow! Essa letra existe na sua palavra!')
            sleep(1)
            lista_correta.append(letra_escolhida)
            indices = [i for i, letra in enumerate(palavra_escolhida) if letra == letra_escolhida]
            for indice in indices:
                lugar_para_encontrar[indice] = letra_escolhida
        else:
            print('Você errou, essa letra não existe na palavra! \u274C')
            sleep(1)
            tentativas = tentativas - 1
            lista_errada.append(letra_escolhida)

    limpar_tela()

    if contador_erros >= tentativas:
        print(f'Você perdeu!\n\nA palavra correta era "{palavra_escolhida.upper()}".\n')
    else:
        print(f'Parabéns! Você acertou a palavra! \U0001f389\n\nA palavra correta era {palavra_escolhida.upper()}!\n')

    jogar_novamente = input('Deseja jogar novamente? (S/N) ')
    limpar_tela()

    if jogar_novamente.lower() != 's':
        limpar_tela()
        print('\nObrigado por jogar!\n')
        break