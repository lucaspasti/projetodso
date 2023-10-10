from abc import ABC, abstractmethod

class TelaAbstrata(ABC):

    @abstractmethod
    def opcoes(self):
        pass

    @abstractmethod
    def pega_dados(self):
        pass

    @abstractmethod
    def mostra(self):
        pass

    @abstractmethod
    def seleciona(self):
        pass

    @abstractmethod
    def mensagem(self):
        pass