

class Compra:
    def __init__(self, codigo, evento, pagante):
        self.__codigo = codigo
        self.__evento = evento  #verificar
        self.__pagante = pagante    #verificar
        self.__produtos = []
        self.__quitada = False

    @property
    def codigo(self):
        return self.__codigo

    @codigo.setter
    def codigo(self, codigo):
        self.__codigo = codigo

    @property
    def evento(self):
        return self.__evento

    @evento.setter
    def evento(self, evento):
        self.__evento = evento

    @property
    def pagante(self):
        return self.__pagante

    @pagante.setter
    def pagante(self, pagante):
        self.__pagante = pagante

    @property
    def quitada(self):
        return self.__quitada

    @quitada.setter
    def quitada(self, valor):
        self.__quitada = valor

    @property
    def produtos(self):
        return self.__produtos

    def add_produto(self, produto):
        self.__produtos.append(produto)     # verificar

    def exc_produto(self, codigo):
        for p in self.__produtos:
            if p.codigo == codigo:
                self.__produtos.remove(p)   # verificar

    def valor_total(self):
        valor = 0
        for p in self.__produtos:
            valor += p.preco
        return valor