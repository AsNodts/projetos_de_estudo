import os

def limpar_terminal():
    if os.name == 'nt':
        os.system('cls')
        
        
#logica da palavra secreta
c = 0
palavra_secreta = 'geladeira'
palavra_formatada = ['*'] * len(palavra_secreta)
print('\033[1;35m-=\033[m' * 20)
print(f'{"Adivinhe a palavra secreta!":^40}')
print('\033[1;35m-=\033[m' * 20)

#loop para as tentativas
while True:    
    tentativa = str(input('Tente adivinhar: ')).lower().strip()
    if len(tentativa) > 1:
        print('\033[1;31mdigite apenas uma letra.\033[m')
        continue
    if tentativa.isalpha():
        if tentativa in palavra_secreta:
            for indice, letra in enumerate(palavra_secreta):
                if letra == tentativa:
                    palavra_formatada[indice] = tentativa
            print("".join(palavra_formatada))
    c += 1
    #completando a palavra secreta
    if '*' not in palavra_formatada:
        limpar_terminal()
        print('\033[32mPARABÉNS, VOCÊ ACERTOU!!\033[m')
        print(f'A palavra era {palavra_secreta}')
        print(f'com um total de {c} tentativas!')
        while True:
            try:
                resp = input('Quer continuar? [S]im / [N]ão ').upper().strip()[0]
                if resp in 'SN':
                    break
            except IndexError:
                print('precisa ser digitado alguma coisa')
        if resp == 'N':
            break
print('FINALIZANDO PROGRAMA')