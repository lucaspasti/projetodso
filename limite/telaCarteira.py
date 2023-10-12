
class TelaCarteira():

    def opcoes(self, amigo):
        print(f"-----Carteira De {amigo.nome}-----")
        print(f"Dinheiro: {amigo.carteira.dinheiro}")
        print("1 - Pagar")
        print("2 - Receber")
        print("3 - Verificar dívidas")
        print("0 - Retornar")
        return int(input("Escolha uma opção: "))

    def pega_valor(self):
        return int(input("Digite o valor: "))

    def pega_cpf_credor(self):
        return input("CPF do credor (Para verificar dívida total, deixe vazio): ")

    def mensagem(self, msg):
        print(msg)