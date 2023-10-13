from limite.telaAbstrata import TelaAbstrata


class TelaProduto (TelaAbstrata):

    def le_num_inteiro(self, msg='', inteiros_validos=[]):
        while True:
            entrada = input(msg)
            try:
                inteiro = int(entrada)
                if inteiros_validos and inteiro not in inteiros_validos:
                    raise ValueError
                return inteiro
            except ValueError:
                print("Valor inválido")
                print()

    def opcoes(self):
        print("\n")
        print("-------- Opções Produto ----------")
        print("1 - Incluir Produto")
        print("2 - Alterar Produto")
        print("3 - Exclui Produtos")
        print("4 - Lista Produtos")
        print("0 - Retornar")

        return self.le_num_inteiro("Escolha a opção: ", [1, 2, 3, 4, 0])

    def pega_dados(self):
        print("-----DADOS-----")
        nome = input("Nome do produto: ")
        codigo = int(input("Codigo do produto: "))
        preco = int(input('Preço do produto: '))           # verificar

        return {'nome': nome, 'codigo': codigo, 'preco': preco}

    def mostra(self, dados):
        print("\n")
        print("Nome: ", dados['nome'])
        print("Codigo: ", dados['codigo'])
        print("Preço: ", dados['preco'])
        print("\n")

    def seleciona(self):
        return int(input("Codigo do produto selecionado: "))    # verificar

    def mensagem(self, msg):
        print(msg)