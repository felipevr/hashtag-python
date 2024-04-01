### Relatório de vendas

### Primeira versão do relatório de vendas

"""
Escreva um programa que calcula o total e a média de vendas para cada vendedor em uma empresa.
O usuário deve digitar o nome do vendedor e suas vendas, e o programa deve manter o controle
do total e da média de vendas para cada vendedor.

Estruture seu programa da seguinte forma:

1. Crie um dicionário vazio para armazenar os dados de vendas.
2. Crie um loop infinito que solicite ao usuário o nome do vendedor e suas vendas.
3. Dentro do loop, use uma declaração if para verificar se o usuário digitou 'sair'.
4. Se o usuário digitar 'sair', encerre o loop usando break.
5. Se o usuário digitar qualquer outra coisa, use as entradas para calcular o total e a média de vendas para o vendedor e adicione-os ao dicionário.
6. Depois que o loop for encerrado, use um loop for para iterar sobre o dicionário e mostrar o total e a média de vendas para cada vendedor.

Exemplo de saída:
    
```
Digite o nome do vendedor (ou 'sair' para sair): João
Digite as vendas: 100
Digite o nome do vendedor (ou 'sair' para sair): Maria
Digite as vendas: 200
Digite o nome do vendedor (ou 'sair' para sair): João
Digite as vendas: 300
Digite o nome do vendedor (ou 'sair' para sair): sair
João: Total de vendas = R$ 400.0, Média de vendas = R$ 200.0
Maria: Total de vendas = R$ 200.0, Média de vendas = R$ 200.0
```

Dica: use o método sum() para calcular o total de vendas e o método len() para calcular o número de vendas.
"""

dados_vendas = {}

def isfloat(num):
    try:
        float(num)
        return True
    except ValueError:
        return False
    
def adicionar_item():
    item = input("Digite o nome do vendedor (ou 'fim' para finalizar): ")
    item = item.casefold()

    if item == 'fim':
        return False
    
    # pega valor das vendas
    while(True):
        qtd = input("Digite as vendas: ")
        if isfloat(qtd):
            break
        else:
            print("Quantidade de vendas inválida. Digite novamente.")
                        
    qtd = float(qtd)

    if not item in dados_vendas:
        dados_vendas[item] = []
    
    dados_vendas[item].append(qtd)

    return True


def ver_resultado():
    for item in dados_vendas:
        lista = dados_vendas[item]
        media = sum(lista) / len(lista)
        print(f"{item}: Total de vendas = R$ {sum(lista):.2f}, Média de vendas = R$ {media:.2f}")

def main():
    while(adicionar_item()):
        pass

    ver_resultado()


if __name__ == '__main__':
    main()