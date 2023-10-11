from entidade.evento import Evento
from limite.telaEvento import TelaEvento

class ControladorEvento:
    def __init__(self, controlador_sistema):
        self.__controlador_sistema = controlador_sistema
        self.__tela_evento = TelaEvento()
        self.__eventos = []


    def pega_evento(self, codigo):
        for e in self.__eventos:
            if e.codigo == codigo:
                return e
        return None

    def inclui_evento(self):
        dados = self.__tela_evento.pega_dados()  #add parametros
        evento = Evento(dados['nome'], dados['data'], dados['codigo'])  # verificar
        self.__eventos.append(evento)

    def lista_eventos(self):
        for e in self.__eventos:
            self.__tela_evento.mostra({'nome': e.nome, 'data': e.data, 'codigo': e.codigo})  #add parametros

    def altera_evento(self):
        self.lista_eventos()
        codigo_evento = self.__tela_evento.seleciona()   #add parametros
        evento = self.pega_evento(codigo_evento)

        novos_dados = self.__tela_evento.pega_dados()    #add parametros
        evento.nome = novos_dados['nome']
        evento.data = novos_dados['data']
        evento.codigo = novos_dados['codigo']       # verificar

    def exclui_evento(self):
        self.lista_eventos()
        codigo_evento = self.__tela_evento.seleciona()   #add parametros
        evento = self.pega_evento(codigo_evento)

        self.__eventos.remove(evento)

    def olha_evento(self):
        codigo = self.__tela_evento.seleciona()
        evento = self.pega_evento(codigo)       # verificar

        self.__tela_evento.mostra_um_evento(evento)

        lista_opcoes = {1: self.add_amigo, 2: self.add_compra, 3: self.remove_amigo,
                        4: self.remove_compra, 5: self.quita_compra, 6: self.quita_evento,
                        0: self.abre_tela}

        while True:
            lista_opcoes[self.__tela_evento.opcoes_um_evento()](evento)

    def add_amigo(self, evento):
        cpf = self.__controlador_sistema.controlador_amigo.tela_amigo().seleciona()
        amigo = self.__controlador_sistema.controlador_amigo.pega_amigo(cpf)
        evento.add_amigo(amigo)         # verificar


    def add_compra(self, evento):
        compra = self.__controlador_sistema.controlador_compra.inclui_compra(evento)
        evento.add_compra(compra)

    def remove_amigo(self, evento):
        cpf = self.__controlador_sistema.controlador_amigo.tela_amigo.seleciona()
        evento.exc_amigo(cpf)           # verificar

    def remove_compra(self, evento):
        compra = self.__controlador_sistema.controlador_compra.exclui_compra(evento)
        evento.exc_compra(compra.codigo)

    def quita_compra(self, evento):
        codigo_compra = self.__controlador_sistema.controlador_compra.tela_compra.seleciona()
        compra = self.__controlador_sistema.controlador_compra.pega_compra(codigo_compra)           # verificar

        self.__controlador_sistema.controlador_compra.quita_compra(compra)

    def quita_evento(self, evento):
        for c in self.__controlador_sistema.controlador_compra.compras:
            if c.evento == evento:
                self.__controlador_sistema.controlador_compra.quita_compra(c)


    def retorna(self):
        self.__controlador_sistema.abre_tela()

    def abre_tela(self, evento=''):     # param opcional para poder retornar do "olha evento"
        lista_opcoes = {1: self.inclui_evento, 2: self.altera_evento, 3: self.exclui_evento,
                        4: self.lista_eventos,5: self.olha_evento, 0: self.retorna}

        while True:
            lista_opcoes[self.__tela_evento.opcoes()]()