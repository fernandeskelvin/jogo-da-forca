import random
import os
from time import sleep

def painel():
    os.system('cls' if os.name == 'nt' else 'clear')
    print(f'Você só pode errar {tentativas} vezes até acertar a palavra!\n')
    print(" ".join(lugar_para_encontrar))
    letra_escolhida = input('\nEscolha uma letra: ').lower()
    return letra_escolhida

def painel_errado():
    os.system('cls' if os.name == 'nt' else 'clear')
    print(f'Você só pode errar {tentativas} vezes até acertar a palavra!\n')
    print(" ".join(lugar_para_encontrar))
    print('\n\nLetras erradas: ' + ' - '.join(letra.upper() for letra in lista_errada))
    letra_escolhida = input('\nEscolha uma letra: ').lower()
    return letra_escolhida

nome_usuario = input('Olá, qual é o seu nome? ')
print(f'\nOlá, {nome_usuario}! Seja Bem-vinda(o) ao Jogo da Forca!\U0001F600 \n\n')

palavras = ['banana', 'laranja', 'maça', 'uva', 'morango',
'abacaxi', 'limao', 'pera', 'kiwi', 'melancia']

while True:
    palavra_escolhida = random.choice(palavras)
    numero_letras = len(palavra_escolhida)
    lugar_para_encontrar = ["_" for _ in range(numero_letras)]
    lista_correta = []
    lista_errada = []
    tentativas = 6
    contador_erros = 0

    print(f'Sua palavra tem {numero_letras} letras!\n')
    siga = input('Pressione Enter para iniciar o jogo ...')

    while contador_erros < tentativas and lugar_para_encontrar != list(palavra_escolhida):

        if tentativas == 6:
            letra_escolhida = painel()
        else:
            letra_escolhida = painel_errado()

        if letra_escolhida in palavra_escolhida:
            print('Woow! Essa letra existe na sua palavra!')
            sleep(1)
            lista_correta.append(letra_escolhida)
            indices = [i for i, letra in enumerate(palavra_escolhida) if letra == letra_escolhida]
            for indice in indices:
                lugar_para_encontrar[indice] = letra_escolhida
        else:
            print('Você errou, esta letra não tem na palavra')
            sleep(1)
            tentativas = tentativas - 1
            lista_errada.append(letra_escolhida)

    os.system('cls' if os.name == 'nt' else 'clear')

    if contador_erros >= tentativas:
        print(f'Você perdeu!\n\nA palavra correta era "{palavra_escolhida.upper()}".\n')
    else:
        print(f'Parabéns! Você acertou a palavra!\n\nA palavra correta era {palavra_escolhida.upper()}!\n')

    jogar_novamente = input('Deseja jogar novamente? (S/N) ')
    os.system('cls' if os.name == 'nt' else 'clear')

    if jogar_novamente.lower() != 's':
        os.system('cls' if os.name == 'nt' else 'clear')
        print('Obrigado por jogar!')
        break