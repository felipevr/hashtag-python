"""
Classes do banco
"""

class Conta:

    _ultimaConta = 0
    
    def __init__(self) -> None:
        self.numero = Conta._ultimaConta + 1
        Conta._ultimaConta = self.numero
        self.saldo = 0

class ContaCorrente(Conta):
    
    def __init__(self, nome, cpf) -> None:
        super().init()
        self.nome = nome
        self.cpf = cpf



class ContaPoupança(Conta):
    
    def __init__(self) -> None:
        pass

