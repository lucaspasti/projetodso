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

    @abstractmethod
    def verifica(self,  ints_validos = []):
        while True:
            valor_lido = input("Insira a opção desejada: ")
            try:
                valor_int = int(valor_lido) #tenta transformar o valor lido em inteiro.
                if ints_validos and valor_int not in ints_validos:
                    raise ValueError
                return valor_int
            except ValueError: #aqui cai se não for int ou se não for valido
                print("A opção selecionada não existe. Tente novamente")