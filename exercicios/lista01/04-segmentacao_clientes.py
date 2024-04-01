### Segmentação de clientes

### Segunda versão da segmentação de clientes

"""
Escreva um programa que segmenta clientes com base em suas compras totais.
O usuário deve digitar o nome do cliente e suas compras totais, e o programa
deve atribuir cada cliente a um segmento: 'Bronze' para compras de até R\\$ 1000,
'Prata' para compras de até R\\$ 5000 e 'Ouro' para compras acima de R\\$ 5000.

Estruture seu programa da seguinte forma:

1. Crie um dicionário vazio para armazenar os clientes e seus segmentos.
2. Crie um loop infinito que solicite ao usuário o nome do cliente e suas compras totais.
3. Dentro do loop, use uma declaração if para atribuir o segmento apropriado ao cliente.
4. Se o usuário digitar 'sair' para o nome do cliente, encerre o loop usando break.
5. Fora do loop, use um loop for para imprimir o nome e o segmento de cada cliente.

Exemplo de saída:
    
```
Digite o nome do cliente (ou 'sair' para sair): João
Digite o total de compras: 100
Digite o nome do cliente (ou 'sair' para sair): Maria
Digite o total de compras: 2000
Digite o nome do cliente (ou 'sair' para sair): José
Digite o total de compras: 6000
Digite o nome do cliente (ou 'sair' para sair): sair
João: Segmento do Cliente = Bronze
Maria: Segmento do Cliente = Prata
José: Segmento do Cliente = Ouro
```

Valida a entrada do usuário.
Se o usuário digitar um valor inválido para compras, mostre a mensagem
"Entrada inválida. Por favor, digite um número para compras." e peça para o usuário digitar
novamente. Tal validação deve ser feita usando try/except.

Além disso, ao invés de deixar os limites de compras fixos no programa, armazene-os em uma
lista de tuplas. Por exemplo:

```python
segmentos = [(1000, 'Bronze'), (5000, 'Prata'), (float('inf'), 'Ouro')]
``` 

Assim, outros segmentos podem ser adicionados facilmente. O primeiro elemento da tupla é o
limite de compras e o segundo é o nome do segmento. O último elemento da lista é uma tupla
com limite `float('inf')`, que representa o segmento Ouro. Isso significa que, se o valor de
compras for maior que todos os limites, o segmento será Ouro.

Depois, percorra essa lista e, para cada tupla, verifique se o valor de compras é menor ou igual
ao limite. Se for, armazene o segmento em um dicionário. Por exemplo, se o usuário digitar
"João" e "500" para compras, o dicionário deve ficar assim:
`{'João': 'Bronze'}`

"""

clientes = {}
segmentos = [(1000, 'Bronze'), (5000, 'Prata'), (float('inf'), 'Ouro')]

def isfloat(num):
    try:
        float(num)
        return True
    except ValueError:
        return False
    
def solicitar_nome_cliente() -> str:
    item = ''
    while(len(item) < 1):
        item = input("Digite o nome do cliente (ou 'fim' para finalizar): ")
        
    return item.casefold()

def solicitar_compras() -> float:
    while(True):
        compra = input("Digite o total de compras: ")
        if isfloat(compra):
            break
        else:
            print("Quantidade de compras inválida. Digite novamente.")
    
    return float(compra)
    
def atualizar_dados(cliente:str, compra:float):
    if cliente in clientes:
        print('Cliente já cadastrado! Nenhum valor atualizado')
        return
    
    for limite,segmento in segmentos:
        if compra <= limite:
            clientes[cliente] = segmento
            break


def print_dados():
    for item in clientes:
        segmento = clientes[item]
        print(f"{item}: Segmento do Cliente = {segmento}")


def main():
    while(True):
        item = solicitar_nome_cliente()

        if item == 'fim':
            break
        
        # pega valor das compras
        compra = solicitar_compras()

        atualizar_dados(item, compra)

    print_dados()


if __name__ == '__main__':
    main()