"""
Classes do banco
"""

class Conta:

    _ultimaConta = 0
    
    def __init__(self, agencia = 1) -> None:
        self.numero = Conta._ultimaConta + 1
        self.agencia = agencia
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

    def __str__(self) -> str:
        return f"Saldo: {self.saldo}"
    
class ContaCorrente(Conta):
    
    def __init__(self, nome, cpf, limite = 1000) -> None:
        super().__init__()
        self.nome = nome
        self.cpf = cpf
        self.limite = limite

    def sacar(self, valor):
        if valor < 0:
            raise Exception('Erro. Valor de saque inválido')
        if valor > self.saldo + self.limite:
            raise Exception('Erro. Valor de saque maior que o seu limite.')
        self.saldo -= valor

    def consultar_limite_chequeespecial(self):
        print(f"Seu limite do cheque especial é de R$ {self.limite:,.2f}.")
        if self.saldo < 0:
            print(f'Você já usou R$ {-self.saldo:,.2f} do seu limite.')
        else:
            print(f'Você não está usando seu limite no momento.')

    def __str__(self) -> str:
        #return f"ContaCorrente do {self.nome} ({self.cpf}) " + super().__str__()
        return f"ContaCorrente do {self.nome}, Número: {self.numero} (" + super().__str__() + ')'


class ContaPoupanca(Conta):
    
    def __init__(self) -> None:
        super().__init__()

    def __str__(self) -> str:
        return f"Conta Poupança Número: {self.numero} (" + super().__str__() + ')'


#programa
conta_Rigo = ContaCorrente("Felipe", '123.456.321-00')
conta_Ana = ContaPoupanca() #"Ana", "000,112,214-85")

print(conta_Rigo)
print(conta_Rigo.cpf)
print(conta_Rigo.numero)


print(conta_Ana)
print(conta_Ana.numero)


conta_Rigo.imprimir_saldo()

conta_Rigo.depositar(10000)

conta_Rigo.imprimir_saldo()

conta_Rigo.sacar(5000)
conta_Rigo.sacar(5000)
conta_Rigo.sacar(499.95)

conta_Rigo.imprimir_saldo()

conta_Rigo.consultar_limite_chequeespecial()
