class Cliente:
    def __init__(self, nome, fone):
        self._nome = nome
        self._telefone = fone

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, nome):
        self._nome = nome

    @property
    def telefone(self):
        return self._telefone

    @telefone.setter
    def telefone(self, fone):
        self._telefone = fone