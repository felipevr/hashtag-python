### Previsão de vendas

### Primeira versão da previsão de vendas

"""
Escreva um programa que preveja as vendas totais para cada produto em uma empresa.
O usuário deve digitar o nome do produto, as vendas do mês atual e a taxa de crescimento,
e o programa deve calcular as vendas previstas para o próximo mês.

Estruture seu programa da seguinte forma:

1. Crie um dicionário vazio para armazenar as previsões de vendas.
2. Crie um loop infinito que solicite ao usuário o nome do produto, as vendas do mês atual e a taxa de crescimento.
3. Dentro do loop, use uma declaração if para verificar se o usuário digitou 'fim'.
4. Se o usuário digitar 'fim', encerre o loop usando break.
5. Se o usuário digitar qualquer outra coisa, use as entradas para calcular as vendas previstas e adicione-as ao dicionário.
6. Depois que o loop for encerrado, use um loop for para iterar sobre o dicionário e mostrar as previsões de vendas para cada produto.

Exemplo de saída:

```
Digite o nome do produto (ou 'fim' para finalizar): iphone
Digite as vendas do mês atual: 10000
Digite a taxa de crescimento (%): 10
Digite o nome do produto (ou 'fim' para finalizar): capinha para iphone
Digite as vendas do mês atual: 200
Digite a taxa de crescimento (%): 20
Digite o nome do produto (ou 'fim' para finalizar): fim
iphone: Previsão de vendas do próximo mês = R$ 11000.00
capinha para iphone: Previsão de vendas do próximo mês = R$ 240.00
```
"""


previsao_vendas = {}

def isfloat(num):
    try:
        float(num)
        return True
    except ValueError:
        return False
    
def adicionar_item():
    item = input("Digite o nome do produto (ou 'fim' para finalizar): ")
    item = item.casefold()

    if item == 'fim':
        return False
    
    # pega qtd de vendas
    while(True):
        qtd = input("Digite as vendas do mês atual: ")
        if isfloat(qtd):
            break
        else:
            print("Quantidade de vendas inválida. Digite novamente.")
            
    # pega taxa de crescimento
    while(True):
        taxa = input("Digite a taxa de crescimento (%): ")
        if isfloat(taxa):
            break
        else:
            print("Valor da taxa inválida. Digite novamente (somente números decimais).")
            
    qtd = float(qtd)
    taxa = float(taxa) / 100 + 1
    
    previsao_vendas[item] = qtd * taxa

    return True

def ver_resultado():
    for item in previsao_vendas:
        valor = previsao_vendas[item]
        print(f"{item}: Previsão de vendas do próximo mês = R$ {valor:.2f}")

def main():
    while(adicionar_item()):
        pass

    ver_resultado()


if __name__ == '__main__':
    main()