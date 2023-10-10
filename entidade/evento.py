from entidade.compra import Compra
from entidade.amigo import Amigo

class Evento:
    def _init_(self, nome, data, codigo):
        self.__nome = nome
        self.__data = data
        self.__codigo = codigo
        self.__amigos = []
        self.__compras = []

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, nome):
        self.__nome = nome

    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self, data):
        self.__data = data

    @property
    def codigo(self):
        return self.__codigo

    @codigo.setter
    def codigo(self, codigo):
        self.__codigo = codigo

    @property
    def amigos(self):
        return self.__amigos

    def add_amigo(self, amigo):
        self.__amigos.append(amigo)     # verificar

    def exc_amigo(self, cpf):
        for amigo in self.__amigos:
            if amigo.cpf == cpf:
                self.__amigos.remove(amigo)     # verificar

    @property
    def compras(self):
        return self.__compras

    def add_compra(self, compra):
        self.__compras.append(compra)   # verificar

    def exc_compra(self, codigo):
        for compra in self.__compras:
            if compra.codigo == codigo:
                self.__compras.remove(compra)   # verificar