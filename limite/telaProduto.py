from limite.telaAbstrata import TelaAbstrata


class TelaProduto (TelaAbstrata):
    def __init__(self):
        super().__init__()

    def tela_opcoes(self):
        print("-------- Opções Produto ----------")
        print("Escolha a opcao")
        print("1 - Incluir Produto")
        print("2 - Alterar Produto")
        print("3 - Exclui Produtos")
        print("4 - Pega Produto por Codigo")
        print("5 - Lista Produtos")
        print("0 - Voltar")

        opcao = self.verifica((0, 1, 2, 3, 4, 5))
        print("\n"*3)
        return opcao