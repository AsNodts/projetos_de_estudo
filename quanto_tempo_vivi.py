from datetime import datetime
from time import sleep

data_atual = datetime.now()


while True:
    #loop geral
    print('Vamos descobrir quanto tempo você já viveu!!')
    while True:
        #loop para o dia apenas
        dia = input('vamos começar pelo seu dia de nascimento, digite ele: ').strip()
        try:
            dia = int(dia)
            if dia > 31:
                print('Digite um numero até 31')
            else:
                break
        except  ValueError:
            print('apenas numeros por favor')
    
    while True:
        #loop para saber o mês
        mes = input('digite o mes agr: ').strip()
        try:
            mes = int(mes)
            if mes > 12:
                print('Digite um numero até 12')
            else:
                break
        except ValueError:
            print('apenas numeros por favor')
    
    while True:
        #loop ano
        ano = input('digite o ano: ').strip()
        try:
            if len(ano) > 4 and ano > str(datetime.today().year):
                print('ano invalido, tente novamente.')
            else:
                ano = int(ano)
                break
        except ValueError:
            print('apenas numeros por favor!')
    
    print('processando...')
    sleep(2)
    data_usuario = datetime(ano, mes, dia)
    tempo = data_atual - data_usuario
    while True:
        print("""escolha 1 a 3 saber quanto tempo viveu em:
    1 -> segundos
    2 -> minutos
    3 -> dias""")
        try:
            resp = int(input())
            match resp:
                case 1:
                    print(f'Você viveu {int(tempo.total_seconds())} segundos!!')

                case 2:
                    print(f'Você viveu {int(tempo.total_seconds() // 60)} minutos!!')
                case 3:
                    print(f'Você viveu {tempo.days} dias!!')
        except ValueError:
            print('digite algo valido por favor')

        fim = input('quer continuar [S]im / [Não]: ').strip().upper()[0]
        if fim == 'N':
            break
    recomeco = input('Quer recomeçar [S]im / [Não]:').strip()[0]
    if recomeco in 'Nn':
        break
print('Obrigado por testar! <3')