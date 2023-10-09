class Carteira:
    def _init_(self, dinheiro):
        self.__dinheiro = dinheiro

    @property
    def dinheiro(self):
        return self.__dinheiro

    @dinheiro.setter
    def dinheiro(self, dinheiro):
        self.__dinheiro = dinheiro

    # adicionar dinheiro?