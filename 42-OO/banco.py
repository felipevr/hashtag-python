"""
Classes do banco
"""

from datetime import datetime, timedelta
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
        ValueError: Valor de deposito inválido
        ValueError: Valor inválido
        ValueError: Valor de saque maior que o saldo.

    """

    _ultimaConta = 0

    @staticmethod
    def _data_hora():
        fuso_MS = pytz.timezone('Brazil/West')
        horario_CG = datetime.now(fuso_MS)
        return horario_CG.strftime('%d/%m/%Y %H:%M:%S')
    
    def __init__(self, agencia = 1) -> None:
        self._numero = Conta._ultimaConta + 1
        self._agencia = agencia
        Conta._ultimaConta = self._numero
        self._saldo = 0
        self._transacoes = []

    def imprimir_saldo(self):
        """Exibe o saldo atual da conta do cliente
        """
        print(f'Seu saldo é de R$ {self._saldo:,.2f}')

    def consultar_saldo(self):
        return self._saldo

    def depositar(self, valor):
        if valor < 0:
            raise ValueError('Erro. Valor de deposito inválido')
        self._saldo += valor
        movimentacao = (valor, self._saldo, Conta._data_hora())
        self._transacoes.append(movimentacao)

    def _verificaValorSaida(self, valor):
        if valor < 0:
            raise ValueError('Erro. Valor inválido')
        if valor > self._saldo:
            raise ValueError('Erro. Valor de saque maior que o saldo.')


    def sacar(self, valor):
        self._verificaValorSaida(valor)
        self._saldo -= valor
        movimentacao = (-valor, self._saldo, Conta._data_hora())
        self._transacoes.append(movimentacao)

    def consultar_extrato(self):
        print('Extrato da conta (Histórico de Transações)')
        print('Valor, Saldo, Data e Hora')
        for trans in self._transacoes:
            print(trans)

    def transferir(self, valor, conta_destino):
        self.sacar(valor)
        conta_destino.depositar(valor)


    def __str__(self) -> str:
        return f"Saldo: {self._saldo}"
    
class ContaCorrente(Conta):
    """
    ContaCorrente é Especialização da classe Conta
    """
    
    def __init__(self, nome, cpf, limite = 1000) -> None:
        super().__init__()
        self._nome = nome
        self._cpf = cpf
        self._limite = limite

    def _verificaValorSaida(self, valor):
        if valor < 0:
            raise ValueError('Erro. Valor inválido')
        if valor > self._saldo + self._limite:
            raise ValueError('Erro. Valor de saque maior que o saldo.')
    

    def consultar_limite_chequeespecial(self):
        print(f"Seu limite do cheque especial é de R$ {self._limite:,.2f}.")
        if self._saldo < 0:
            print(f'Você já usou R$ {-self._saldo:,.2f} do seu limite.')
        else:
            print(f'Você não está usando seu limite no momento.')

    def __str__(self) -> str:
        return f"ContaCorrente do {self._nome}, Número: {self._numero} (" + super().__str__() + ')'


class ContaPoupanca(Conta):
    """
    Poupança é Especialização da classe Conta
    
    """

    _rendimentoPorMes = 0.01
    _depositos = []
    
    def __init__(self, taxa_rendimento = 0.01) -> None:
        """
        Inicializa a classe Poupanca com uma lista vazia de depósitos e uma taxa de rendimento.
        
        Args:
            taxa_rendimento (float, opcional): A taxa de rendimento a ser aplicada nos depósitos. 
                                      Padrão é 1% (0.01) ao mês.
        """
        super().__init__()
        self._rendimentoPorMes = taxa_rendimento

    def __str__(self) -> str:
        return f"Conta Poupança Número: {self._numero} (" + super().__str__() + ')'
    
    def rendeConta(self):
        """Implementa o rendimento da conta no mês
        """
        data_atual = datetime.now()
        for deposito in self._depositos:
            # Verifica se o depósito foi feito há mais de 30 dias
            if data_atual - deposito['data'] > timedelta(days=30):
                # Aplica o rendimento ao valor do depósito
                deposito['valor'] *= (1 + self._rendimentoPorMes)

        novo_saldo = self.calcular_saldo()
        #print(novo_saldo, self._saldo, novo_saldo > self._saldo)
        if novo_saldo > self._saldo:
            self._transacoes.append((novo_saldo-self._saldo, novo_saldo, Conta._data_hora()))
        self._saldo = novo_saldo
    
    def depositar(self, valor, data_deposito=None):
        """
        Adiciona um depósito à lista de depósitos.
        
        Args:
            valor (float): O valor do depósito.
            data_deposito (datetime): A data em que o depósito foi feito. Se não for fornecida, 
                                      a data atual será usada.
        """
        #atualiza o saldo
        super().depositar(valor)
        
        if data_deposito is None:
            data_deposito = datetime.now()
        
        self._depositos.append({'valor': valor, 'data': data_deposito})

    def _verificaValorSaida(self, valor):
        if valor < 0:
            raise ValueError('Erro. Valor inválido')
        if valor > self._saldo:
            raise ValueError('Erro. Valor de saque maior que o saldo.')


    def sacar(self, valor):
        """
        Realiza um saque na conta poupanca.
        
        Args:
            valor (float): O valor a ser sacado.
            
        Raises:
            ValueError: Se o valor a ser sacado for maior do que o saldo disponível.
        """
        super().sacar(valor)

        # Remover valor dos depósitos
        for deposito in self._depositos:
            if deposito['valor'] >= valor:
                deposito['valor'] -= valor
                valor = 0
            else:
                valor -= deposito['valor']
                deposito['valor'] = 0
            
            # Remover depósitos zerados
            if deposito['valor'] == 0:
                self._depositos.remove(deposito)
            
            if valor == 0:
                break
        
    def calcular_saldo(self):
        """
        Calcula o saldo atual da conta poupança somando todos os depósitos.
        
        Returns:
            float: O saldo total da conta poupança.
        """
        return sum(deposito['valor'] for deposito in self._depositos if deposito['valor'] > 0)




#programa
conta_Rigo = ContaCorrente("Felipe", '123.456.321-00')
conta_Ana = ContaPoupanca() #"Ana", "000,112,214-85")

#help(str)

print(conta_Rigo)
print(conta_Rigo._cpf)
print(conta_Rigo._numero)


print(conta_Ana)
print(conta_Ana._numero)
data_passada = datetime.now() - timedelta(days=35)
conta_Ana.depositar(1100, data_passada)
conta_Ana.depositar(500)   # Depósito de 500 reais


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


#help(Conta)


# Aplicar rendimento nos depósitos
conta_Ana.rendeConta()

# Sacar 300 reais
conta_Ana.sacar(300)
conta_Ana.consultar_extrato()

# Calcular saldo atual
saldo_atual = conta_Ana.calcular_saldo()
print(f"Saldo após aplicar rendimento: {saldo_atual:.2f} reais")
print(f"Saldo atual: {conta_Ana._saldo} reais")





