# Exercício - sistema de perguntas e respostas


perguntas = [
    {
        'Pergunta': 'Quanto é 2+2?',
        'Opções': ['1', '3', '4', '5'],
        'Resposta': '4',
    },
    {
        'Pergunta': 'Quanto é 5*5?',
        'Opções': ['25', '55', '10', '51'],
        'Resposta': '25',
    },
    {
        'Pergunta': 'Quanto é 10/2?',
        'Opções': ['4', '5', '2', '1'],
        'Resposta': '5',
    },
]
contador_acertos = 0
for indice, pergunta in enumerate(perguntas):
    print(f'{indice + 1}º pergunta:', end=' ')
    print(pergunta['Pergunta'])
    print()
    print('Opções:')
    for opcao, alternativa in enumerate(pergunta['Opções']):
        print(f'{opcao}) {alternativa}')
    resp = input('Escolha uma Opção: ')
    try:
        if pergunta['Opções'][int(resp)] == pergunta['Resposta']:
            print('ACERTOU 👍')
            contador_acertos += 1
        else:
            print('ERROU ❌')
        print()
    except ValueError:
        print('ERROR ❌')
        continue

print(f'Você acertou {contador_acertos} de {len(perguntas)}')