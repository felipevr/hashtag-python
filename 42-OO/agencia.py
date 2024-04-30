
from random import randint

class Agencia:

    def __init__(self, numero, cnpj, telefone) -> None:
        print('Criado objeto da AgenciaBase')
        self._numero = numero
        self.cnpj = cnpj
        self.telefone = telefone
        self.clientes = []
        self.caixa = 0
        self.emprestimos = []

    def verificar_caixa(self):
        if self.caixa < 1_000_000:
            print('Caixa abaixo do nivel recomendado. Caixa Atual: {:,.2f}'.format(self.caixa))
        else:
            print('O valor do Caixa está OK. Caixa Atual: {:,.2f}'.format(self.caixa))

    def emprestar_dinheiro(self, valor, cpf, juros):
        if self.caixa > valor:
            self.emprestimos.append((valor, cpf, juros))
        else:
            print('Não há dinheiro em caixa disponível para empréstimo.')

    def adicionar_cliente(self, nome, cpf, patrimonio):
        self.clientes.append((nome, cpf, patrimonio))




#AgenciaVirtual
class AgenciaVirtual(Agencia):
    
    def __init__(self, numero, site, email, agencia_associada = None) -> None:
        super().__init__(numero, agencia_associada.cnpj, agencia_associada.telefone)
        print('Criado objeto da AgenciaVirtual')
        self.site = site
        self.email = email
        self._agencia_associada = agencia_associada
        self.caixa_criptomoedas = 0

    def depositar_criptomoeda(self, valor):
        self.caixa -= valor
        self.caixa_criptomoedas += valor

    def sacar_criptomoeda(self, valor):
        self.caixa += valor
        self.caixa_criptomoedas -= valor
    
    def verificar_caixa(self):
        if self.caixa < 100_000:
            print('Caixa abaixo do nivel recomendado. Caixa Atual: R$ {:,.2f}'.format(self.caixa))
        else:
            print('O valor do Caixa está OK. Caixa Atual: R$ {:,.2f}'.format(self.caixa))
        print(f'Caixa em criptomoedas de R$ {self.caixa_criptomoedas:,.2f}')

#AgenciaComum
class AgenciaComum(Agencia):
    
    def __init__(self, numero, cnpj, telefone, endereco) -> None:
        Agencia.__init__(self, numero, cnpj, telefone)
        print('Criado objeto da AgenciaComum')
        self.endereco = endereco

#AgenciaPremium
class AgenciaPremium(AgenciaComum, AgenciaVirtual):
    """
    Agencia TOP das Galaxias que engloba as funcionalidades de todas as outras
    """
    
    def __init__(self, cnpj, telefone, endereco = None, site = None, email = None, numero = None) -> None:
        super().__init__(numero, cnpj, telefone, endereco)
        print('Criado objeto da AgenciaPremium')
        self.endereco = endereco
        self.site = site
        self.email = email
        self.caixa = 10_000_000
        if numero is None:
            self._numero = randint(1001, 9999)
        else:
            self._numero = numero

    
    def adicionar_cliente(self, nome, cpf, patrimonio):
        if patrimonio < 1_000_000:
            print('Patrimonio muito baixo para Agencia Premium')
        else:
            super().adicionar_cliente(nome, cpf, patrimonio)

    
    def verificar_caixa(self):
        if self.caixa < 10_000_000:
            print('Caixa abaixo do nivel recomendado. Caixa Atual: {:,.2f}'.format(self.caixa))
        else:
            print('O valor do Caixa está OK. Caixa Atual: {:,.2f}'.format(self.caixa))
