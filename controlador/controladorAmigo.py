class ControladorAmigo:
    def _init_(self, controlador_sistema):
        self.__amigos = []
        self.__tela_amigo = TelaAmigo()
        self.__controlador_sistema = controlador_sistema

    def pega_amigo(self, cpf):
        for a in self.__amigos:
            if a.cpf == cpf:
                return a
        return None

    def inclui_amigo(self):
        dados = self.__tela_amigo.pega_dados()  #add parametros
        amigo = Amigo(dados['nome'], dados['cpf'])  # verificar
        self.__amigos.append(amigo)

    def lista_amigos(self):
        for a in self.__amigos:
            self.__tela_amigo.mostra()  #add parametros

    def altera_amigo(self):
        self.lista_amigos()
        cpf_amigo = self.__tela_amigo.seleciona()   #add parametros
        amigo = self.__pega_amigo(cpf_amigo)

        novos_dados = self.__tela_amigo.pega_dados()    #add parametros
        amigo.nome = novos_dados['nome']
        amigo.cpf = novos_dados['cpf']      # verificar

    def excluir_amigo(self):
        self.lista_amigos()
        cpf_amigo = self.__tela_amigo.seleciona()   #add parametros
        amigo = self.pega_amigo(cpf_amigo)

        self.__amigos.remove(amigo)     # verificar

    def olhar_carteira(self):
        cpf_amigo = self.__tela_amigo.seleciona()   #add parametros
        amigo = self.pega_amigo(cpf_amigo)      # verificar

        amigo.carteira.abre_tela()

    #abre tela

    #retornar

    # verificar divida