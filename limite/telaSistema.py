from limite.telaAbstrata import TelaAbstrata

class TelaAmigo(TelaAbstrata):

    def opcoes(self):
        print("-----OPÇÕES-----")
        print("1 - Menu de Amigos")
        print("2 - Menu de Eventos")
        print("3 - Menu de Produtos")
        print("8 - Encerrar Sistema")

        return int(input("Escolha a opção: "))      # verificar

# UML: NAO HERDA DA TELA ABSTRATA