def validador_cpf(usuario_digitou):
    #criação da lista para calculo de 10 até 2.
    lista0_a_10 = range(10, 1, -1)
    lista0_a_10 = list(lista0_a_10)
    lista11_a_0 = range(11, 1, -1)
    lista11_a_0 = list(lista11_a_0)

    #cpf para o exemplo
    cpf_exemplo = usuario_digitou
    if cpf_exemplo.isdigit():
        cpf_exemplo= f"{cpf_exemplo[:3]}.{cpf_exemplo[3:6]}.{cpf_exemplo[6:9]}-{cpf_exemplo[9:]}"
    #deixa cpf apenas com numeros
    cpf_exemplo_limpo = ''.join(filter(str.isdigit, cpf_exemplo))

    #converte cpf para string
    cpf_exemplo_str = str(cpf_exemplo_limpo)

    #lista para armazenar o resultados e multiplicação
    lista_digito1 = []
    for k, num in enumerate(lista0_a_10):
        lista_digito1.append(num * int(cpf_exemplo_str[k]))
    digito1 = (sum(lista_digito1) * 10) % 11
    digito1 = digito1 if digito1 <= 9 else 0

    #para achar o segundo digito
    lista_digito2 = []
    for k, num in enumerate(lista11_a_0):
        lista_digito2.append(num * int(cpf_exemplo_str[k]))
    digito2 = (sum(lista_digito2) * 10) % 11
    digito2 = digito2 if digito2 <= 9 else 0

    cpf_validado = f'{cpf_exemplo[:12]}{digito1}{digito2}'
    if cpf_validado == cpf_exemplo:
        return '\033[32mSeu cpf está correto!\033[m'
    else:
        return '\033[31mCPF invalido\033[m'


# Lista de CPFs inválidos conhecidos
invalidos = ['00000000000', '11111111111', '99999999999', '000.000.000-00', '111.111.111-11', '999.999.999-99']

while True:
    try:
        cpf = input('Digite o CPF para ser validado: ').strip()
        if cpf in invalidos or len(cpf) < 11 or len(cpf) > 14:
            print('CPF INVALIDO')
            continue
        else:
            print(validador_cpf(cpf))
        
    except IndexError:
        print('Digite apenas numeros ou como no exemplo: xxx.xxx.xxx-xx')
