from limite.telaAbstrata import TelaAbstrata

class TelaCompra(TelaAbstrata):

    def opcoes(self):
        print("-----AMIGOS-----")
        print("1 - Incluir Amigo")
        print("2 - Alterar Amigo")
        print("3 - Excluir Amigo")
        print("4 - Listar Amigos")
        print("5 - Olhar Carteira")
        print("0 - Retornar")

        return int(input("Escolha a opção: "))      # verificar

    def pega_dados(self):
        print("-----DADOS-----")
        codigo = input("Código: ")
        cpf_pagante = input("CPF do amigo pagante: ")          # verificar

        return {'codigo': codigo, 'cpf': cpf_pagante}       # Pegar produtos

    def mostra(self, dados):
        print("Código: ", dados['codigo'])
        print("Pagante: ", dados['pagante'])
        print("Produtos: ", dados['produtos'])
        print("Valor: ", dados['valor'])
        print("Quitada: ", dados['quitada'])
        print("\n")

    def seleciona(self):
        return input("Código da compra a selecionar: ")     # verificar

    def mensagem(self, msg):
        print(msg)