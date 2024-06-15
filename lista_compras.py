import os
from time import sleep

def limpar_terminal():
    if os.name == 'nt':
        os.system('cls')


def mostrar_lista():
    print('\033[30m=\033[m' * 20)
    print(F'{"LISTA DE COMPRAS":^20}')
    print('\033[30m=\033[m' * 20)
    for k, v in enumerate(lista_compras):
        print(f'\033[36m{k}\033[m: \033[1;33m{v}\033[m')
    if lista_compras == []:
        print(f'{"VAZIA":^20}')
    print('\033[30m=\033[m' * 20)


lista_compras = []
while True:
    digitou = input('selecione uma opção\n'
          '[i]nserir [a]pagar [l]istar: ').strip().lower()[0]
    if digitou not in 'ial':
        print('Função invalida. Tente novamente!')
        continue
    limpar_terminal()
    match digitou:
        case 'l':
            mostrar_lista()
        case 'a':
            try:
                mostrar_lista()
                print('digite o numero do item que deseja apagar. ([999] para voltar)')
                apagar = int(input('Qual item: '))
                if apagar == 999:
                    print('Voltando...')
                    sleep(1)
                    limpar_terminal()
                    continue
                limpar_terminal()
                print(f'{lista_compras[apagar]} sendo apagado...')
                sleep(1)
                print('\033[31mAPAGADO!\033[m')
                lista_compras.pop(apagar)
                sleep(1)
                limpar_terminal()
            except ValueError:
                limpar_terminal()
                print('\033[31mvoce não digitou nada. Tente novamente\033[m')
            except IndexError:
                limpar_terminal()
                print('\033[7;97mSelecione um item valido.\033[m')
                print()
        case 'i':
            limpar_terminal()
            mostrar_lista()
            inserir = input('Oque deseja inserir: ([x] para sair) ').strip().title()
            if inserir.lower() == 'x':
                print('nada foi adicionado.')
                sleep(1)
            if inserir.isnumeric():
                print('ITEM INVÁLIDO! TENTE NOVAMENTE')
                continue
            print(f'inserindo \033[1;32m{inserir.title()}\033[m na lista...')
            sleep(1)
            print('\033[1;32mADICIONADO!\033[m')
            lista_compras.append(inserir)
            sleep(1)
            limpar_terminal()

            
            