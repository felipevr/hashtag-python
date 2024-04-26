"""
Classes do banco
"""

class Conta:

    _ultimaConta = 0
    
    def __init__(self) -> None:
        self.numero = Conta._ultimaConta + 1
        Conta._ultimaConta = self.numero
        self.saldo = 0

    def imprimir_saldo(self):
        print(f'Seu saldo é de R$ {self.saldo:,.2f}')

    def consultar_saldo(self):
        return self.saldo

    def depositar(self, valor):
        if valor < 0:
            raise Exception('Erro. Valor de deposito inválido')
        self.saldo += valor

    def sacar(self, valor):
        if valor < 0:
            raise Exception('Erro. Valor de saque inválido')
        if valor > self.saldo:
            raise Exception('Erro. Valor de saque maior que o saldo.')
        self.saldo -= valor

class ContaCorrente(Conta):
    
    def __init__(self, nome, cpf) -> None:
        super().__init__()
        self.nome = nome
        self.cpf = cpf



class ContaPoupanca(Conta):
    
    def __init__(self) -> None:
        pass



#programa
conta_Rigo = ContaCorrente("Felipe", '123.456.321-00')

print(conta_Rigo)
print(conta_Rigo.cpf)

conta_Rigo.imprimir_saldo()

conta_Rigo.depositar(10000)

conta_Rigo.imprimir_saldo()

conta_Rigo.sacar(5000)
conta_Rigo.sacar(5000)
conta_Rigo.sacar(0)

conta_Rigo.imprimir_saldo()