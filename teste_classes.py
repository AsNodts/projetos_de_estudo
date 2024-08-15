class Animal():
    def __init__(self, nome, cor_pelo):
        self.cor_pelo = cor_pelo
        self._nome = nome
        
    @property
    #privando o nome para testes
    def nome(self):
        return self._nome

    @nome.setter
    #setter para ser alterado depois como ex: cachorro1.nome = mario
    def nome(self, novo_nome):
        if isinstance(novo_nome, str):
            self._nome = novo_nome
        else:
            raise ValueError("O nome deve ser uma string")


    #caso algum animal for registrado usando apenas animal, ele só vai ter essa função padrão som "Grunindo"
    def som(self):
        return f'grunindo'
    

#classe Especie ficaria melhor mas apenas para um teste isso serve.
class Gato(Animal):
    def __init__(self, nome, cor_pelo):
        super().__init__(nome, cor_pelo)
    
    def som(self):
        return 'Miau. Miau'
    
    def brincar(self):
        return 'Brincando com laser!'
    

#Criando uma classe para cachorros herdando a classe Animal
class Cachorro(Animal):
    def __init__(self, nome, cor_pelo):
        super().__init__(nome, cor_pelo) #usnado o super para utilizar o __init__ da classe principal Animal

    def som(self):
        return 'Au! Au!'
    
    def brincar(self):
        return 'Brincando de pegar a Bolinha'



#codigo extrair e apresentar dados
gato_nome = str(input('Digite o Nome do seu gatinho: ')).strip().title()
gato_cor = str(input('Qual a cor do seu gato? ')).strip().title()
gato1 = Gato(gato_nome, gato_cor)
print(f'Seu gato se chama {gato1.nome} e a sua cor é {gato1.cor_pelo} e pode miar -{gato1.som()}')

#testando função brincar com gato
brincar = str(input('Quer Brincar com seu gato? ')).strip()[0]
if brincar in 'Ss':
    print(gato1.brincar())

#trabalhando com a entrada de dados para teste da class Cachorro
cachorro_nome = str(input('Agora vamos falar de cachorros, Digite o nome dele: ')).strip().title()
cachorro_cor = str(input('Que nome legal! Qual a cor dele: ')).strip().title()
cachorro1 = Cachorro(cachorro_nome, cachorro_cor)
print(f'Nome do cachorro: {cachorro1.nome}, da cor {cachorro1.cor_pelo}, cuidado que ele é bravo! {cachorro1.som()} ')
brincar = str(input('Quer Brincar com seu cachorro? ')).strip()[0]
if brincar in 'Ss':
    print(cachorro1.brincar())

print('Obrigado por testar nosso sistema!')
cachorro1.nome = 'Fabinho'
print(f'mudando nome do cachorro agora para.... {cachorro1.nome} ')

