
import os
def mostrar_lista(lista):
    print('=' * 20)
    print(f'{"LISTA":^20}')
    print('-' * 20)
    if not lista:
        print(f'{"LISTA VAZIA":^20}')
    else:
        for item in lista:
            l= f'{item:^20}'
            print(l.upper())
    print('=' * 20)
    print()


def refazer():
    global historico
    if historico:
        tudo.append(historico.pop())
        mostrar_lista(tudo)
        print()
        return
    print('não há oque refazer. ')
    mostrar_lista(tudo)
    print()


def desfazer():
    global historico
    global tudo
    if tudo:
        historico.append(tudo.pop())
        mostrar_lista(tudo)
        print()
        return
    print('não há oque desfazer.')
    mostrar_lista(tudo)
    print()



tudo = []
historico =[]
comando = [ 'listar', 'desfazer', 'refazer']
while True:
    print('Digite um comando')
    acao = input('listar | desfazer | refazer: ').lower().strip()
    os.system('cls')
    if acao == '':
        print('digite algo valido!')
        continue
    if acao in comando:
        match acao:
            case 'listar':
                mostrar_lista(tudo) 
            case 'desfazer':
                desfazer()
            case 'refazer':
                refazer()
    else:
        tudo.append(acao)
        historico.clear()
        mostrar_lista(tudo)
