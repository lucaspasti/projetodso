from telaCarteira import TelaCarteira

class ControladorCarteira:

    def __init__(self, controlador_amigo):
        self.__tela_carteira = TelaCarteira()
        self.__controlador_amigo = controlador_amigo

    def paga(self, amigo):
        valor = -(self.__tela_carteira.pega_valor())
        amigo.carteira.somar_dinheiro(valor)

    def recebe(self, amigo):
        valor = self.__tela_carteira.pega_valor()
        amigo.carteira.somar_dinheiro(valor)

    def retorna(self, _):
        self.__controlador_amigo.abre_tela()

    def abre_tela(self, amigo):
        lista_opcoes = {1: self.paga, 2: self.recebe, 0: self.retorna}

        while True:
            lista_opcoes[self.__tela_carteira.opcoes(amigo)](amigo)
