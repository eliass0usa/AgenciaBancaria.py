class Cliente:
    def __init__(self, nome, telefone):
        self._nome = nome
        self._telefone = telefone

    # métodos GET
    def get_nome(self):
        return self._nome

    def get_telefone(self):
        return self._telefone

    # métodos SET
    def set_nome(self, nome):
        self._nome = nome

    def set_telefone(self, telefone):
        self._telefone = telefone