### Lista de compras

### Terceira versão da lista de compras

"""
O programa de lista de compras usa um dicionário.
Agora é possível adicionar mais de uma unidade de um item na lista de compras. 
Ou seja, o dicionário deve armazenar o nome do item e a quantidade desejada pelo usuário. 
Por exemplo, se o usuário digitar "banana" e "2", o dicionário deve armazenar "banana" como 
chave e 2 como valor. A estrutura do dicionário ficaria assim: `{"banana": 2}`.

O programa deve permitir que o usuário adicione, remova e visualize o dicionário de compras.

Além disso, o programa deve mostrar uma mensagem de erro se o usuário tentar
usar uma opção inválida do menu. Por exemplo, se o usuário digitar 5, o programa
deve mostrar a mensagem "Opção inválida. Por favor, escolha uma opção válida." e
mostrar o menu novamente. Além disso, o programa deve ser *case insensitive*, ou seja,
"Maçã" e "maçã" devem ser considerados o mesmo item.

Agora usa funções para organizar o código. 
Crie funções para cada uma das opções do menu: `adicionar_item`, `remover_item` e `ver_lista`. 
Crie também uma função para mostrar o menu. 
O programa deve continuar funcionando da mesma forma, mas agora o código deve estar organizado em funções.

"""


lista_compras = {}

def imprime_menu():
    print("1 Adicionar item")
    print("2 Remover item")
    print("3 Ver lista")
    print("4 Sair")
    return input("Escolha uma opção: ")

def adicionar_item():
    item = input("Digite um item: ")
    while(True):
        qtd = input("Digite a quantidade: ")
        if qtd.isdecimal():
            break
        else:
            print("Quantidade inválida. Tente novamente.")
    item = item.casefold()
    qtd = int(qtd)
    if item in lista_compras:
        lista_compras[item] += qtd
    else:
        lista_compras[item] = qtd

def remover_item():
    item = input("Digite um item: ")
    item = item.casefold()
    if item in lista_compras:
        lista_compras.pop(item)
    else:
        print('Item não encontrado!')

def ver_lista():
    print(lista_compras)

def main():
    continua = True

    while(continua):
        escolha = imprime_menu()

        if escolha == '4':
            print('Até mais!')
            break
        elif escolha == '3':
            ver_lista()
        elif escolha == '1':
            adicionar_item()
        elif escolha == '2':
            remover_item()
        else:
            print('Opção inválida. Por favor, escolha uma opção válida.')


if __name__ == '__main__':
    main()