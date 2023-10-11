from limite.telaAbstrata import TelaAbstrata


class TelaProduto (TelaAbstrata):


    def opcoes(self):
        print("-------- Opções Produto ----------")
        print("Escolha a opcao")
        print("1 - Incluir Produto")
        print("2 - Alterar Produto")
        print("3 - Exclui Produtos")
        print("4 - Mostra Produto por Codigo")
        print("5 - Lista Produtos")
        print("0 - Voltar")

        return int(input("Escolha a opção: "))

    def pega_dados(self):
        print("-----DADOS-----")
        nome = input("Nome do produto: ")
        codigo = int(input("Codigo do produto: "))
        preco = int(input('Preço do produto: '))           # verificar

        return {'nome': nome, 'codigo': codigo, 'preco': preco}

    def mostra(self, dados):
        print("Nome: ", dados['nome'])
        print("Codigo: ", dados['codigo'])
        print("Preço: ", dados['preco'])
        print("\n")

    def seleciona(self):
        return int(input("Codigo do produto selecionado: "))    # verificar

    def mensagem(self, msg):
        print(msg)