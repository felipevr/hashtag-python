
import time
from datetime import datetime, timedelta
from banco import ContaCorrente, ContaPoupanca, CartaoCredito
from agencia import Agencia, AgenciaVirtual, AgenciaComum, AgenciaPremium


def main_testes_agencias():
    print('Criar objeto AgenciaPremium')
    ap = AgenciaPremium('12343', '2342')


def main_testes_agencias4():
    agencia2 = Agencia(2, '123123', '213432')

    agencia2.caixa = 1_000_000

    print('Criar objeto AgenciaComum')
    agencia3 = AgenciaComum(43, '21341234', '12341234', 'Rua bla bla bla')
    print('Criar objeto AgenciaPremium')
    ap = AgenciaPremium('12343', '2342')
    print('Criar objeto AgenciaVirtual')
    av = AgenciaVirtual(3, 'http://1234', '1234@banco.com', agencia2)

    av.caixa = 150000

    print(ap.__module__)


    av.depositar_criptomoeda(2000)
    av.verificar_caixa()
    

    ap.caixa = 200_000
    ap.verificar_caixa()

    ap.adicionar_cliente('Fulano', '123', 1000)
    ap.adicionar_cliente('Fulano 2', '1323', 1000000)
    print(ap.clientes)

    agencia3.caixa = 100000
    agencia3.verificar_caixa()
    
    agencia3.adicionar_cliente('Fulano', '123', 1000)
    print(agencia3.clientes)

    print(ap, av)

def main_testes_agencias2():
    agencia2 = Agencia(2, '123123', '213432')

    agencia2.caixa = 1_000_000

    agencia2.verificar_caixa()

    agencia2.emprestar_dinheiro(1500, '123412341234', 0.02)

    print('Empréstimos:')
    print(agencia2.emprestimos)


    agencia2.adicionar_cliente('Rigo', '12341234', 1_000_000)

    print('Clientes:')
    print(agencia2.clientes)


def main():
    #main_testes_banco()

    main_testes_agencias()
    



def main_testes_banco():
            
    conta_Rigo = ContaCorrente("Felipe", '123.456.321-00')
    conta_Ana = ContaPoupanca() #"Ana", "000,112,214-85")

    cartao_Rigo = CartaoCredito('Rigo', conta_Rigo)
    print(cartao_Rigo._nome_titular)
    print(cartao_Rigo._conta_corrente._numero)
    print(conta_Rigo._cartoes[0]._numero)
    print(cartao_Rigo._validade)

    cartao_Rigo.senha = '1234'
    print('Senha: ', cartao_Rigo.senha)

    print(conta_Rigo.__dict__)
    print(cartao_Rigo.__dict__)

    main_testes_banco3(conta_Rigo, conta_Ana)


"""

def main_testes_banco2():
    numero_cartao_visa = CartaoCredito._geraNumeroCartao('Visa')
    numero_formatado = CartaoCredito._formatar_numero_cartao(numero_cartao_visa)
    print(f"Número do cartão Visa: {numero_cartao_visa}")
    print(f"Número do cartão Visa formatado: {numero_formatado}")

    numero_cartao_mastercard = CartaoCredito._formatar_numero_cartao(CartaoCredito._geraNumeroCartao('Mastercard'))
    print(f"Número do cartão Mastercard: {numero_cartao_mastercard}")

    numero_cartao_amex = CartaoCredito._formatar_numero_cartao(CartaoCredito._geraNumeroCartao('American Express'))
    print(f"Número do cartão American Express: {numero_cartao_amex}")
"""
#help(str)


def main_testes_banco3(conta_Rigo, conta_Ana):
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
    #time.sleep(1)
    conta_Rigo.sacar(5000)
    #time.sleep(1)
    conta_Rigo.sacar(499.95)

    conta_Rigo.imprimir_saldo()

    conta_Rigo.consultar_limite_chequeespecial()

    conta_Rigo.transferir(250, conta_Ana)


    print('-' * 20)
    #print(conta_Rigo.transacoes)
    #conta_Rigo.consultar_extrato()


    #help(Conta)


    # Aplicar rendimento nos depósitos
    conta_Ana.rendeConta()

    # Sacar 300 reais
    conta_Ana.sacar(300)
    #conta_Ana.consultar_extrato()

    # Calcular saldo atual
    # saldo_atual = conta_Ana.calcular_saldo()
    # print(f"Saldo após aplicar rendimento: {saldo_atual:.2f} reais")
    # print(f"Saldo atual: {conta_Ana._saldo} reais")







if __name__ == '__main__':
    main()