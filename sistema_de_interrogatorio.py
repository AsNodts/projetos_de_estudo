from time import sleep


perguntas = [
    'Telefonou para a vitima? ',
    'Esteve no local do crime? ',
    'Mora perto da vitima? ',
    'Devia para a vitima? ',
    'Já trabalhou com a vitima? '
]
suspeita = [
    'Possui algum motivo para querer mal à vítima? ',
    'Já foi acusado de violência antes? ',
    'Você já teve algum desentendimento com a vitima? ',
    'Você possui alguma arma de fogo? '
]

print('SISTEMA DE INTERROGAÇÃO')
print('-' * 23)
contador = 0
for pergunta in perguntas:
    resposta = input(pergunta).strip()[0]
    print('Salvando resposta....')
    sleep(1)
    if resposta in 'Ss':
        contador += 1
print('Analisando dados....')
sleep(2)
if contador == 2:
    interrogada = 'Suspeita'
elif contador == 3 or contador == 4:
    interrogada = 'Cúmplice'
elif contador == 5:
    interrogada = 'Assassino(a)'
else:
    interrogada = 'Inocente'

print(f'A pessoa interrogada é {interrogada} até o momento.')

match interrogada:
    case 'Suspeita':
        contador = 0
        for pergunta in suspeita:
            resposta = input(pergunta).strip()[0]
            print('Salvando...')
            sleep(1)
            if resposta in 'Ss':
                contador += 1
            if contador >= 2:
                interrogada = 'Assassino(a)'
    case 'Cúmplice':
        contador = 0
        for pergunta in suspeita:
            resposta = input(pergunta).strip()[0]
            print('Salvando...')
            sleep(1)
            if resposta in 'Ss':
                contador += 1
            if contador < 2:
                interrogada = 'Inocente'
print()
print('VEREDITO!') 
print()
sleep(1)
print(f'Com todas as informações fornecidas, a pessoa interrogada é {interrogada}')