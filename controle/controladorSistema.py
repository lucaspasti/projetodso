from limite.telaSistema import TelaSistema
from controle.controladorEvento import ControladorEvento
#from controladorProduto import ControladorProduto
from controle.controladorAmigo import ControladorAmigo

class ControladorSistema:
    def __init__(self):
        self.__controlador_evento = ControladorEvento(self)
        self.__controlador_amigo = ControladorAmigo(self)
#       self.__controlador_produto = ControladorProduto(self)
        self.__tela_sistema = TelaSistema()

    @property
    def controlador_amigo(self):
        return self.__controlador_amigo

    def inicializa_sistema(self):
        self.abre_tela()

    def menu_amigos(self):
        self.__controlador_amigo.abre_tela()

    def menu_eventos(self):
        self.__controlador_evento.abre_tela()

#    def menu_produtos(self):
 #       self.__controlador_produto.abre_tela()

    def encerra_sistema(self):
        exit(0)

    def abre_tela(self):
        lista_opcoes = {1: self.menu_amigos, 2: self.menu_eventos, 3: self.menu_produtos,
                        8: self.encerra_sistema}
        while True:
            lista_opcoes[self.__tela_sistema.opcoes()]()

sis = ControladorSistema()

sis.inicializa_sistema()