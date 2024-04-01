### Relatório de vendas

### Terceira versão do relatório de vendas

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

Valida a entrada do usuário.
Se o usuário digitar um valor inválido para vendas, mostre a mensagem
"Entrada inválida. Por favor, digite um número para vendas." e peça para o usuário digitar
novamente. Tal validação deve ser feita usando try/except.

Além disso, ao invés de armazenar cada venda em uma lista para cada vendedor, armazene
o total de vendas e a quantidade de vendas em um dicionário. Por exemplo, se o usuário
digitar "João" e "1000" para vendas, o dicionário deve ficar assim:

```python
{'João': {'total_vendas': 1000, 'quantidade_vendas': 1}}
```

Se, após, o usuário digitar "João" e "2000" para vendas, o dicionário deve ficar assim:

```python
{'João': {'total_vendas': 3000, 'quantidade_vendas': 2}}
```

Perceba como o total de vendas de João aumentou em 2000, assim como a quantidade aumentou em uma unidade.

Ao final, mostre o total de vendas e a média de vendas de cada vendedor.

Use funções para organizar o código. 
Crie funções para cada uma das operações: 
`solicitar_nome_vendedor`, `solicitar_vendas` e `atualizar_dados` e `print_dados`.
O programa deve continuar funcionando da mesma forma, mas agora o código deve estar organizado em funções.

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
    
def solicitar_nome_vendedor() -> str:
    item = input("Digite o nome do vendedor (ou 'fim' para finalizar): ")
    return item.casefold()

def solicitar_vendas() -> float:
    while(True):
        venda = input("Digite as vendas: ")
        if isfloat(venda):
            break
        else:
            print("Quantidade de vendas inválida. Digite novamente.")
    
    return float(venda)
    
def atualizar_dados(vendedor:str, venda:float):

    if not vendedor in dados_vendas:
        dados_vendas[vendedor] = {'total_vendas': venda, 'quantidade_vendas': 1}
    else:
        dados_vendas[vendedor]['total_vendas'] += venda
        dados_vendas[vendedor]['quantidade_vendas'] += 1


def print_dados():
    for item in dados_vendas:
        total_vendas = dados_vendas[item]['total_vendas']
        quantidade_vendas = dados_vendas[item]['quantidade_vendas']
        media = total_vendas / quantidade_vendas
        print(f"{item}: Total de vendas = R$ {total_vendas:.2f}, Média de vendas = R$ {media:.2f}")

def main():
    while(True):
        item = solicitar_nome_vendedor()

        if item == 'fim':
            break
        
        # pega valor das vendas
        venda = solicitar_vendas()

        atualizar_dados(item, venda)

    print_dados()


if __name__ == '__main__':
    main()