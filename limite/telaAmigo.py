from limite.telaAbstrata import TelaAbstrata

class TelaAmigo(TelaAbstrata):

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
        nome = input("Nome: ")
        cpf = input("CPF: ")
        dinheiro = input("Dinheiro: ")          # verificar
        print("\n")

        return {'nome': nome, 'cpf': cpf, 'dinheiro': dinheiro}

    def mostra(self, dados):
        print("\n")
        print("Nome: ", dados['nome'])
        print("CPF: ", dados['cpf'])
        print("Dinheiro: ", dados['dinheiro'])
        print("\n")

    def seleciona(self):
        return input("CPF do amigo a selecionar: ")     # verificar

    def mensagem(self, msg):
        print(msg)