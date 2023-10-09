from telaCarteira import TelaCarteira

class ControladorCarteira:

    def __init__(self, controlador_sistema):
        self.__tela_carteira = TelaCarteira()
        self.__controlador_sistema = controlador_sistema

    def paga(self, amigo):
        valor = -(int(input("Valor a pagar: ")))
        amigo.carteira.somar_dinheiro(valor)

    def recebe(self, amigo):
        valor = int(input("Valor a receber: "))
        amigo.carteira.somar_dinheiro(valor)


    def abre_tela(self, amigo):
        lista_opcoes = {1: self.paga, 2: self.recebe, 0: self.retorna}

        while True:
            lista_opcoes[self.__tela_carteira.opcoes(amigo)](amigo)
