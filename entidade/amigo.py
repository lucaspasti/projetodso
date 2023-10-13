class Amigo:
    def _init_(self, nome, cpf, dinheiro):
        self.__nome = nome
        self.__cpf = cpf
        self.__eventos = []
        self.__carteira = Carteira(dinheiro)

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, nome):
        self.__nome = nome

    @property
    def cpf(self):
        return self.__cpf

    @cpf.setter
    def cpf(self, cpf):
        self.__cpf = cpf

    @property
    def carteira(self):
        return self.__carteira

    @carteira.setter
    def carteira(self, carteira):
        self.__carteira = carteira

    @property
    def eventos(self):
        return self.__eventos

    def add_evento(self, evento):
        self.__eventos.append(evento)

    def exc_evento(self, codigo):
        for e in self.__eventos:
            if e.codigo == codigo:
                self.__eventos.remove(e)    # verificar