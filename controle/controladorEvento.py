from evento import Evento
from telaEvento import TelaEvento

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

        lista_opcoes = {1: self.inclui_evento, 2: self.altera_evento, 3: self.exclui_evento, \
                        4: self.lista_eventos, 5: self.olha_evento, 0: self.retorna}

        while True:
            lista_opcoes[self.__tela_evento.opcoes_um_evento()]()

    # add amigo no evento

    # add compra no evento

    # quitar evento


    def retorna(self):
        self.__controlador_sistema.abre_tela()

    def abre_tela(self):
        lista_opcoes = {1: self.inclui_evento, 2: self.altera_evento, 3: self.exclui_evento, \
                        4: self.lista_eventos,5: self.olha_evento, 0: self.retorna}

        while True:
            lista_opcoes[self.__tela_evento.opcoes()]()