class TelaCarteira:

    def opcoes(self, amigo):
        print(f"-----Carteira De {amigo.nome}-----")
        print("1 - Pagar")
        print("2 - Receber")
        print("0 - Retornar")
        return input("Escolha uma opção: ")