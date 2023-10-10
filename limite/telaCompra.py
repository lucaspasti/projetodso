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
        nome = input("Código: ")
        cpf_pagante = input("CPF do amigo pagante: ")          # verificar

        return {'nome': nome, 'cpf': cpf_pagante}

    def mostra(self, dados):
        print("Código: ", dados['codigo'])
        print("Pagante: ", dados['pagante'])
        print("Quitada: ", dados['quitada'])
        print("\n")

    def seleciona(self):
        return input("Código da compra a selecionar: ")     # verificar

    def mensagem(self, msg):
        print(msg)