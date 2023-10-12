from limite.telaCarteira import TelaCarteira
from entidade.carteira import Carteira

class ControladorCarteira:

    def __init__(self, controlador_sistema):
        self.__tela_carteira = TelaCarteira()
        self.__controlador_sistema = controlador_sistema

    def paga(self, amigo):
        valor = -(self.__tela_carteira.pega_valor())
        amigo.carteira.somar_dinheiro(valor)

    def recebe(self, amigo):
        valor = self.__tela_carteira.pega_valor()
        amigo.carteira.somar_dinheiro(valor)

    def recebe_valor(self, amigo, valor):
        amigo.carteira.somar_dinheiro(valor)

    def verifica_divida(self, amigo):
        credor = self.__controlador_sistema.controlador_amigo.pega_amigo(
            self.__tela_carteira.pega_cpf_credor()
        )
        divida = 0
        if not credor:
            for c in self.__controlador_sistema.controlador_compra.compras:
                if not c.quitada:
                    if c.pagante == amigo:
                        divida -= (c.valor_total() - c.valor_parcial())
                    elif amigo in c.evento.amigos:
                        divida += c.valor_parcial()
            self.__tela_carteira.mensagem(f"Dívida total: {divida}")
            return divida
        else:
            for c in self.__controlador_sistema.controlador_compra.compras:
                if not c.quitada:
                    if amigo == c.pagante and credor in c.evento.amigos:
                        divida -= c.valor_parcial()
                    elif amigo in c.evento.amigos and credor == c.pagante:
                        divida += c.valor_parcial()
            self.__tela_carteira.mensagem(f"Dívida parcial para {credor.nome}: {divida}")
            return divida


    def retorna(self, _):
        self.__controlador_sistema.controlador_amigo.abre_tela()

    def abre_tela(self, amigo):
        lista_opcoes = {1: self.paga, 2: self.recebe, 3:self.verifica_divida, 0: self.retorna}

        while True:
            lista_opcoes[self.__tela_carteira.opcoes(amigo)](amigo)
