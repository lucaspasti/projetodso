from entidade.produto import Produto
from limite.telaProduto import TelaProduto

class ControladorProduto:

    def __init__(self, controlador_sistema):
        self.__controlador_sistema = controlador_sistema
        self.__produtos = []
        self.__tela_produto = TelaProduto()

    @property
    def tela_produto(self):
        return self.__tela_produto

    def pega_produto(self, codigo):
        for p in self.__produtos:
            if p.codigo == codigo:
                return p
        return None

    def inclui_produto(self):
        dados = self.__tela_produto.pega_dados()  #add parametros
        codigo = dados_produto('codigo')
        produto = self.pega_produto(codigo)
        try:
            if produto == None:
                self.__produtos.append(produto)
            else:
                raise ValueError
        except ValueError:
            self.__tela_produto.mensagem('Produto já existe')


    def lista_produtos(self):
        try:
            if lista:
                for p in self.__produtos:
                    self.__tela_produto.mostra({'nome': p.nome, 'codigo': p.codigo, 'preco': p.preco})
            else:
                raise KeyError
        except KeyError:
            self.__tela_produto.mensagem('Não há nenhum produto cadastrado.')

    def altera_produto(self):
        self.lista_produtos()
        codigo_produto = self.__tela_produto.seleciona()   #add parametros
        produto = self.pega_produto(codigo_produto)
        try:
            if produto:
                novos_dados = self.__tela_produto.pega_dados()    #add parametros
                produto.nome = novos_dados['nome']
                produto.preco = novos_dados['preco']
            else:
                raise KeyError
        except KeyError:
            self.tela_produto.mensagem('Produto não existente')

    def excluir_produto(self):
        self.lista_produtos()
        codigo_produto = self.__tela_produto.seleciona()  # add parametros
        produto = self.pega_produto(codigo_produto)
        try:
            if produto:
                self.__produtos.remove(produto)  # verificar
            else:
                raise KeyError
        except KeyError:
            self.__tela_produto.mensagem('Produto não existente. ')


    def retorna(self):
        self.__controlador_sistema.abre_tela()

    def abre_tela(self):
        lista_opcoes = {1: self.inclui_produto, 2: self.altera_produto, 3: self.excluir_produto,
                        4: self.lista_produtos, 0: self.retorna}

        while True:
            lista_opcoes[self.__tela_produto.opcoes()]()
