
class TelaCarteira():

    def opcoes(self, amigo):
        print(f"-----Carteira De {amigo.nome}-----")
        print(f"Dinheiro: {amigo.carteira.dinheiro}")
        print("1 - Pagar")
        print("2 - Receber")
        print("0 - Retornar")
        return int(input("Escolha uma opção: "))

    def pega_valor(self):
        return int((input("Digite o valor: ")))