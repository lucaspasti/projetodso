from entidade.amigo import Amigo
from limite.telaAmigo import TelaAmigo

class ControladorAmigo:
    def __init__(self, controlador_sistema):
        self.__controlador_sistema = controlador_sistema
        self.__amigos = []
        self.__tela_amigo = TelaAmigo()

    @property
    def tela_amigo(self):
        return self.__tela_amigo

    def pega_amigo(self, cpf):
        try:
            for a in range(len(self.__amigos)):
                if self.__amigos[a].amigo.cpf == cpf:
                    return a
            else:
                raise KeyError
        except KeyError:
            return None


    def inclui_amigo(self):
        while True:
            dados = self.__tela_amigo.pega_dados()
            amigo = Amigo(dados['nome'], dados['cpf'], dados['dinheiro'])
            try:
                for a in self.__amigos:
                    if a.cpf == amigo.cpf:
                        raise ValueError
            except ValueError:
                self.__tela_amigo.mensagem("CPF já existente, tente novamente.")
            try:
                if amigo.cpf < 0:
                    raise ValueError
            except ValueError:
                self.__tela_amigo.mensagem("CPF inválido, tente novamente.")

            else:
                self.__amigos.append(amigo)
                break

    def lista_amigos(self):
        for a in self.__amigos:
            self.__tela_amigo.mostra({'nome': a.nome, 'cpf': a.cpf, 'dinheiro': a.carteira.dinheiro})  #add parametros

    def altera_amigo(self):
        self.lista_amigos()
        cpf_amigo = self.__tela_amigo.seleciona()   #add parametros
        amigo = self.pega_amigo(cpf_amigo)

        novos_dados = self.__tela_amigo.pega_dados()    #add parametros
        amigo.nome = novos_dados['nome']
        amigo.cpf = novos_dados['cpf']      # verificar
        amigo.carteira.dinheiro = novos_dados['dinheiro']

    def excluir_amigo(self):
        self.lista_amigos()
        cpf_amigo = self.__tela_amigo.seleciona()   #add parametros
        amigo = self.pega_amigo(cpf_amigo)

        self.__amigos.remove(amigo)     # verificar

    def olha_carteira(self):
        self.lista_amigos()
        cpf_amigo = self.__tela_amigo.seleciona()   #add parametros
        amigo = self.pega_amigo(cpf_amigo)      # verificar

        self.__controlador_sistema.controlador_carteira.abre_tela(amigo)

    def retorna(self):
        self.__controlador_sistema.abre_tela()


    def abre_tela(self):
        lista_opcoes = {1: self.inclui_amigo, 2: self.altera_amigo, 3: self.excluir_amigo,
                        4: self.lista_amigos,5: self.olha_carteira, 0: self.retorna}

        while True:
            lista_opcoes[self.__tela_amigo.opcoes()]()

    # verificar divida
