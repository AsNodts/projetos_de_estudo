import random
chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%&*()'
while True:
    senha = input('Quantas senhas você deseja gerar? ')
    if senha.isnumeric() :
        senha = int(senha)
        tamanho = input('Qual tamanho das senhas? ')
        if tamanho.isnumeric():
            tamanho = int(tamanho)
            break
        else:
            print('Apenas numeros')
    else:
        print('Apenas numeros')
print('Suas senhas são:')

for pwd in range(senha):
    senhas = ''
    for c in range(tamanho):
        senhas += random.choice(chars)
    print(senhas)