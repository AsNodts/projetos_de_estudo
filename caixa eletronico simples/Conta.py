from time import sleep

class Conta:
    def __init__(self, titular, numero, saldo=0):
        self._saldo = saldo
        self._numero = numero
        self._titular = titular

    @property
    def saldo(self):
        return self._saldo

    @saldo.setter
    def saldo(self, saldo=0):
        if saldo < 0:
            print('O saldo não pode ser negativo')
        else:
            self._saldo = saldo

    @property
    def numero(self):
        return self._numero

    def saque(self, valor):
        if self.saldo >= valor:
            self.saldo -= valor
            print('Saque realizado com sucesso!')
            sleep(1)
        else:
            print('Saldo insuficiente')
            sleep(1)


    def deposita(self, valor):
        if valor > 0:
            self.saldo += valor
            print("Deposito realizado com sucesso!")
            sleep(1)
        else:
            print("Valor invalido para deposito!")
            sleep(1)


    def extrato(self):
        print(f'Cliente {self._titular} \nSaldo Atual: R${self._saldo:.2f}')
        sleep(1)