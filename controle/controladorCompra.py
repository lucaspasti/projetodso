from entidade.compra import Compra
from limite.telaCompra import TelaCompra

class ControladorCompra:

    def __init__(self, controlador_sistema):
        self.__controlador_sistema = controlador_sistema
        self.__compras = []
        self.__tela_compra = TelaCompra()

    @property
    def tela_compra(self):
        return self.__tela_compra

    @property
    def compras(self):
        return self.__compras

    def pega_compra(self, codigo):
        for c in self.__compras:
            if c.codigo == codigo:
                return c
        return None

    def inclui_compra(self, evento):
        dados = self.__tela_compra.pega_dados()  #add parametros
        compra = Compra(dados['codigo'], evento,
                        self.__controlador_sistema.controlador_amigo.pega_amigo(dados['cpf']))  # verificar
        while True:
            codigo_produto = self.__controlador_sistema.controlador_produto.tela_produto.seleciona()
            if codigo_produto == 0:
                break
            compra.add_produto(self.__controlador_sistema.controlador_produto.pega_produto(codigo_produto))

        self.__controlador_sistema.controlador_carteira.recebe_valor(compra.pagante, -compra.valor_total())
        self.__compras.append(compra)       # Pegar produtos
        return compra

    def lista_compras(self, evento):
        for c in self.__compras:
            if c.evento == evento:
                self.__tela_compra.mostra({'codigo': c.nome, 'pagante': c.pagante,
                                           'quitada': c.quitada})  #add parametros


    def exclui_compra(self, evento):
        self.lista_compras(evento)
        codigo_compra = self.__tela_compra.seleciona()   #add parametros
        compra = self.pega_compra(codigo_compra)

        self.__compras.remove(compra)
        return compra


    def quita_compra(self, compra):

        valor_parcial = compra.valor_parcial()
        for a in compra.evento.amigos:
            self.__controlador_sistema.controlador_carteira.recebe_valor(
                a, -(valor_parcial)
            )

        self.__controlador_sistema.controlador_carteira.recebe_valor(
            compra.pagante, compra.valor_total()
        )
        compra.quitada = True
