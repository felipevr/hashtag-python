# ## Lista de compras

# ### Segunda versão da lista de compras
# 

# Mude o programa de lista de compras para usar um dicionário ao invés de uma lista.
# O programa deve ter as mesmas funcionalidades, mas agora deve ser possível
# adicionar mais de uma unidade de um item na lista de compras. Ou seja, o dicionário
# deve armazenar o nome do item e a quantidade desejada pelo usuário. Por exemplo,
# se o usuário digitar "banana" e "2", o dicionário deve armazenar "banana" como chave
# e 2 como valor. A estrutura do dicionário ficaria assim: `{"banana": 2}`.
# 
# O programa deve permitir que o usuário adicione, remova e visualize o dicionário de compras.
# 
# Além disso, o programa deve mostrar uma mensagem de erro se o usuário tentar
# usar uma opção inválida do menu. Por exemplo, se o usuário digitar 5, o programa
# deve mostrar a mensagem "Opção inválida. Por favor, escolha uma opção válida." e
# mostrar o menu novamente. Além disso, o programa deve ser *case insensitive*, ou seja,
# "Maçã" e "maçã" devem ser considerados o mesmo item.
# 
# Exemplo de saída:
# 
# ```
# 1 Adicionar item
# 2 Remover item
# 3 Ver lista
# 4 Sair
# Escolha uma opção: 1
# Digite um item: banana
# Digite a quantidade: 2
# 
# 1 Adicionar item
# 2 Remover item
# 3 Ver lista
# 4 Sair
# Escolha uma opção: 1
# Digite um item: maçã
# Digite a quantidade: 3
# 
# 1 Adicionar item
# 2 Remover item
# 3 Ver lista
# 4 Sair
# Escolha uma opção: 3
# {'banana': 2, 'maçã': 3}
# 
# 1 Adicionar item
# 2 Remover item
# 3 Ver lista
# 4 Sair
# Escolha uma opção: 2
# Digite um item: banana
# Digite a quantidade: 1
# 
# 1 Adicionar item
# 2 Remover item
# 3 Ver lista
# 4 Sair
# Escolha uma opção: 3
# {'banana': 1, 'maçã': 3}
# 
# 1 Adicionar item
# 2 Remover item
# 3 Ver lista
# 4 Sair
# Escolha uma opção: 4
# ```
# 


lista_compras = {}

def imprime_menu():
    print("1 Adicionar item")
    print("2 Remover item")
    print("3 Ver lista")
    print("4 Sair")
    return input("Escolha uma opção: ")

def inclui_novo_item():
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

continua = True

while(continua):
    escolha = imprime_menu()

    if escolha == '4':
        print('Até mais!')
        break
    elif escolha == '3':
        print(lista_compras)
    elif escolha == '1':
        inclui_novo_item()
    elif escolha == '2':
        item = input("Digite um item: ")
        item = item.casefold()
        if item in lista_compras:
            lista_compras.pop(item)
        else:
            print('Item não encontrado!')
    else:
        print('Opção inválida. Por favor, escolha uma opção válida.')