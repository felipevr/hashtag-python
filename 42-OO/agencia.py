

class Agencia:

    def __init__(self, numero, cnpj, telefone) -> None:
        self._numero = numero
        self.cnpj = cnpj
        self.telefone = telefone
        self.clientes = []
        self.caixa = 0
        self.emprestimos = []

    def verificar_caixa(self):
        if self.caixa < 1_000_000:
            print('Caixa abaixo do nivel recomendado. Caixa Atual: {}'.format(self.caixa))
        else:
            print('O valor do Caixa está OK. Caixa Atual: {}'.format(self.caixa))

    def emprestar_dinheiro(self, valor, cpf, juros):
        if self.caixa > valor:
            self.emprestimos.append((valor, cpf, juros))
        else:
            print('Não há dinheiro em caixa disponível para empréstimo.')

    def adicionar_cliente(self, nome, cpf, patrimonio):
        self.clientes.append((nome, cpf, patrimonio))

#programa
agencia2 = Agencia(2, '123123', '213432')

agencia2.caixa = 1_000_000

agencia2.verificar_caixa()

agencia2.emprestar_dinheiro(1500, '123412341234', 0.02)

print('Empréstimos:')
print(agencia2.emprestimos)


agencia2.adicionar_cliente('Rigo', '12341234', 1_000_000)

print('Clientes:')
print(agencia2.clientes)