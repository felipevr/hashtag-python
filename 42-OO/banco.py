"""
Classes do banco
"""

from datetime import datetime
import pytz
import time


class Conta:
    """
    Classe Conta base para outros tipos de conta

    Attributes:
        numero: número da conta (automático)
        agencia: número da agencia da conta
        saldo: inteiro com valor atual do saldo
        transacoes: lista com histórico de movimentações da conta

    Raises:
        Exception: Valor de deposito inválido
        Exception: Valor inválido
        Exception: Valor de saque maior que o saldo.

    """

    _ultimaConta = 0

    @staticmethod
    def _data_hora():
        fuso_MS = pytz.timezone('Brazil/West')
        horario_CG = datetime.now(fuso_MS)
        return horario_CG.strftime('%d/%m/%Y %H:%M:%S')
    
    def __init__(self, agencia = 1) -> None:
        self.numero = Conta._ultimaConta + 1
        self.agencia = agencia
        Conta._ultimaConta = self.numero
        self.saldo = 0
        self.transacoes = []

    def imprimir_saldo(self):
        """Exibe o saldo atual da conta do cliente
        """
        print(f'Seu saldo é de R$ {self.saldo:,.2f}')

    def consultar_saldo(self):
        return self.saldo

    def depositar(self, valor):
        if valor < 0:
            raise Exception('Erro. Valor de deposito inválido')
        self.saldo += valor
        movimentacao = (valor, self.saldo, Conta._data_hora())
        self.transacoes.append(movimentacao)

    def _verificaValorSaida(self, valor):
        if valor < 0:
            raise Exception('Erro. Valor inválido')
        if valor > self.saldo:
            raise Exception('Erro. Valor de saque maior que o saldo.')


    def sacar(self, valor):
        self._verificaValorSaida(valor)
        self.saldo -= valor
        movimentacao = (-valor, self.saldo, Conta._data_hora())
        self.transacoes.append(movimentacao)

    def consultar_extrato(self):
        print('Extrato da conta (Histórico de Transações)')
        print('Valor, Saldo, Data e Hora')
        for trans in self.transacoes:
            print(trans)

    def transferir(self, valor, conta_destino):
        self._verificaValorSaida(valor)
        self.saldo -= valor
        self.transacoes.append( (-valor, self.saldo, Conta._data_hora()) )

        conta_destino.saldo += valor
        conta_destino.transacoes.append( (valor, conta_destino.saldo, Conta._data_hora()) )


    def __str__(self) -> str:
        return f"Saldo: {self.saldo}"
    
class ContaCorrente(Conta):
    
    def __init__(self, nome, cpf, limite = 1000) -> None:
        super().__init__()
        self.nome = nome
        self.cpf = cpf
        self.limite = limite

    # def sacar(self, valor):
    #     if valor < 0:
    #         raise Exception('Erro. Valor de saque inválido')
    #     if valor > self.saldo + self.limite:
    #         raise Exception('Erro. Valor de saque maior que o seu limite.')
    #     self.saldo -= valor
    #     movimentacao = (-valor, self.saldo, Conta._data_hora())
    #     self.transacoes.append(movimentacao)

    def _verificaValorSaida(self, valor):
        if valor < 0:
            raise Exception('Erro. Valor inválido')
        if valor > self.saldo + self.limite:
            raise Exception('Erro. Valor de saque maior que o saldo.')
    

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

#help(str)

print(conta_Rigo)
print(conta_Rigo.cpf)
print(conta_Rigo.numero)


print(conta_Ana)
print(conta_Ana.numero)
conta_Ana.depositar(1100)


time.sleep(1)
conta_Rigo.imprimir_saldo()

conta_Rigo.depositar(10000)

conta_Rigo.imprimir_saldo()
time.sleep(1)
conta_Rigo.sacar(5000)
time.sleep(1)
conta_Rigo.sacar(5000)
time.sleep(1)
conta_Rigo.sacar(499.95)

conta_Rigo.imprimir_saldo()

conta_Rigo.consultar_limite_chequeespecial()

conta_Rigo.transferir(250, conta_Ana)


print('-' * 20)
#print(conta_Rigo.transacoes)
conta_Rigo.consultar_extrato()
conta_Ana.consultar_extrato()


help(Conta)
