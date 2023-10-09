from controladorAmigo import ControladorAmigo
from controladorEvento import ControladorEvento
from controladorProduto import ControladorProduto
from telaSistema import TelaSistema

class ControladorSistema:
    def __init__(self):
        self.__controlador_evento = ControladorEvento(self)
        self.__controlador_amigo = ControladorAmigo(self)
        self.__controlador_produto = ControladorProduto(self)
        self.__tela_sistema = TelaSistema()

    def inicializa_sistema(self):
        self.abre_tela()

    def menu_amigos(self):
        self.__controlador_amigo.abre_tela()

    def menu_eventos(self):
        self.__controlador_evento.abre_tela()

    def menu_produtos(self):
        self.__controlador_produto.abre_tela()

    def encerra_sistema(self):
        exit(0)

    def abre_tela(self):
        lista_opcoes = {1: self.menu_amigos, 2: self.menu_eventos, 3: self.menu_produtos, \
                        8: self.encerra_sistema}
        while True:
            lista_opcoes[self.__tela_sistema.opcoes()]()