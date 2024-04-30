"""
Classes do banco
"""

from datetime import datetime, timedelta
import pytz
import random


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
        self._cartoes = []

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

    def adicionaCartaCredito(self, cartaoCredito):
        self._cartoes.append(cartaoCredito)

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


class CartaoCredito:
    """Classe de Cartão de Crédito
    associada com a Classe ContaCorrente

    """
    
    @staticmethod
    def _data_hora():
        fuso_MS = pytz.timezone('Brazil/West')
        horario_CG = datetime.now(fuso_MS)
        return horario_CG        

    def __init__(self, titular:str, conta_corrente:ContaCorrente) -> None:
        self._numero = CartaoCredito._geraNumeroCartao()
        self._nome_titular = titular
        self._validade = '{:02d}/{}'.format(CartaoCredito._data_hora().month, CartaoCredito._data_hora().year + 4)
        self.__codigo_seguranca = CartaoCredito._gerar_cvv()
        self._limite = 50
        self._senha = None
        self._conta_corrente = conta_corrente
        conta_corrente.adicionaCartaCredito(self)

    @property
    def senha(self):
        return self._senha
    
    @senha.setter
    def senha(self, nova):
        if len(nova) == 4 and nova.isnumeric():
            self._senha = nova
        else:
            print("Nova Senha Inválida! Digite 4 números.")


    def ajustarLimite(self, novo_limite):
        self._limite = novo_limite

    @staticmethod
    def _geraNumeroCartao(bandeira = 'Mastercard'):
        """
        Gera um número de cartão de crédito com base na bandeira do cartão.

        Args:
            bandeira (str): A bandeira do cartão (por exemplo, 'Visa', 'Mastercard', 'American Express'). Padrão: 'Mastercard'

        Returns:
            str: O número do cartão de crédito gerado com base na bandeira.
        """
        # Definir prefixos com base na bandeira
        prefixos = {
            'Visa': '4',
            'Mastercard': '5',
            'American Express': '3',
            'Elo': '5'
        }
        
        if bandeira not in prefixos:
            raise ValueError(f"Bandeira {bandeira} não suportada.")

        # Obtém o prefixo da bandeira
        prefixo = prefixos[bandeira]

        # Gera os próximos dígitos do cartão
        instituicao_financeira = random.randint(10000, 99999)  # Gera um número de 2º a 6º dígito

        # Gera dígitos únicos para o cliente
        digitos_unicos = random.randint(10000000, 999999999)  # Gera dígitos do 7º ao 15º dígito

        # Concatenar prefixo, instituição financeira e dígitos únicos
        numero_cartao = f"{prefixo}{instituicao_financeira:05d}{digitos_unicos:09d}"

        # Calcular o dígito verificador usando o algoritmo de Luhn
        numero_cartao_completo = CartaoCredito._adicionar_digito_verificador(numero_cartao)

        return numero_cartao_completo
    
    @staticmethod
    def _adicionar_digito_verificador(numero):
        """
        Calcula e adiciona o dígito verificador a um número de cartão de crédito usando o algoritmo de Luhn.

        Args:
            numero (str): O número de cartão de crédito sem o dígito verificador.

        Returns:
            str: O número de cartão de crédito com o dígito verificador.
        """
        total = 0
        # Reverte o número para facilitar o cálculo
        reversed_number = numero[::-1]

        for i, char in enumerate(reversed_number):
            digit = int(char)
            # Dobra os dígitos nos índices ímpares (considerando índice 0 como par)
            if i % 2 == 1:
                digit *= 2
                # Se o resultado é maior que 9, subtrai 9
                if digit > 9:
                    digit -= 9
            total += digit

        # O dígito verificador é o número necessário para tornar o total divisível por 10
        digito_verificador = (10 - total % 10) % 10

        # Concatenar o dígito verificador ao número original
        numero_com_digito_verificador = f"{numero}{digito_verificador}"

        return numero_com_digito_verificador

    @staticmethod
    def _gerar_cvv():
        """
        Gera um código de verificação de cartão (CVV) com 3 dígitos.

        Returns:
            str: O código de verificação como uma string de 3 dígitos.
        """
        cvv = ""
        for _ in range(3):
            # Gera um número inteiro aleatório entre 0 e 9
            digito = random.randint(0, 9)
            # Concatena o dígito ao CVV
            cvv += str(digito)
        return cvv
    
    @staticmethod
    def _formatar_numero_cartao(numero_cartao):
        """
        Formata um número de cartão de crédito em grupos de 4 dígitos.

        Args:
            numero_cartao (str): O número de cartão de crédito.

        Returns:
            str: O número de cartão de crédito formatado em grupos de 4 dígitos.
        """
        # Formatar o número de cartão em grupos de 4 dígitos separados por espaço
        grupos = [numero_cartao[i:i+4] for i in range(0, len(numero_cartao), 4)]
        return ' '.join(grupos)

    def __str__(self) -> str:
        return f"Cartão Crédito Número {self._numero}, Titular {self._nome_titular}"
    


