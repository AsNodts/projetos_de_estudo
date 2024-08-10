from Conta import Conta

import os

from Cliente import Cliente

def limpar_tela():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

def menu():
    print('-' * 20)
    print(f'Cliente: {c1.nome.split()[0]:>11}')
    print(f'Conta: {conta_c1.numero:>13}')
    print(f'Saldo: {conta_c1.saldo:>13.2f}')
    print('-' * 20)


#pegando informações cliente
cliente = str(input('Digite seu nome para validação: ')).title()
telefone = input('Digite seu telefone: ')

#colocando na Classe Cliente
c1 = Cliente(cliente, telefone)

#tratando numero da conta e saldo
while True:
    conta = str(input("Digite o numero da sua conta: ")).strip()
    if conta.isnumeric():
        conta = int(conta)
        break
    else:
        print('Digite apenas numeros')
saldo = input('Qual saldo na conta: ').strip()
if ',' in saldo:
    saldo = saldo.replace(",", ".")
if saldo == '':
    saldo = 0.0
else:
    saldo = float(saldo)
conta_c1 = Conta(cliente, conta, saldo)

limpar_tela()
while True:
    menu()
#opçoes menu
    print("Selecione a opção que desejar:"
                       "\n1 - Saque"
                       "\n2 - Deposito"
                       "\n3 - extrato")
    opcao = int(input())
    match opcao:
        case 1:
            limpar_tela() #limpar tela
            menu()
            saque = float(input("Quanto deseja sacar? "))
            conta_c1.saque(saque)
        case 2:
            limpar_tela()
            menu()
            dep = float(input('Quanto deseja Depósitar? '))
            conta_c1.deposita(dep)
        case 3:
            limpar_tela()
            conta_c1.extrato()
