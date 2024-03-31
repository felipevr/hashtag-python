# ## Lista de compras

# ### Primeira versão da lista de compras

# Escreva um programa que permita que um usuário crie uma lista de compras.
# O usuário deve ser capaz de adicionar itens, remover itens e visualizar a lista.
# 
# Estruture seu programa da seguinte forma:
# 
# 1. Crie uma lista vazia para armazenar os itens da lista de compras.
# 2. Crie um loop infinito que imprima um menu de opções ao usuário e permita que ele escolha uma opção.
# 3. Dentro do loop, use uma declaração if para executar a tarefa apropriada de acordo com a escolha do usuário.
# 4. Se o usuário escolher adicionar um item, solicite que ele digite o nome do item e adicione-o à lista.
# 5. Se o usuário escolher remover um item, solicite que ele digite o nome do item e remova-o da lista.
# 6. Se o usuário escolher ver a lista, mostre cada item da lista em sua própria linha.
# 7. Se o usuário escolher sair, encerre o loop usando break.
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
# 
# 1 Adicionar item
# 2 Remover item
# 3 Ver lista
# 4 Sair
# Escolha uma opção: 1
# Digite um item: maçã
# 
# 1 Adicionar item
# 2 Remover item
# 3 Ver lista
# 4 Sair
# Escolha uma opção: 3
# ['banana', 'maçã']
# 
# 1 Adicionar item
# 2 Remover item
# 3 Ver lista
# 4 Sair
# Escolha uma opção: 2
# Digite um item: banana
# 
# 1 Adicionar item
# 2 Remover item
# 3 Ver lista
# 4 Sair
# Escolha uma opção: 3
# ['maçã']
# 
# 1 Adicionar item
# 2 Remover item
# 3 Ver lista
# 4 Sair
# Escolha uma opção: 4
# ```


lista_compras = []

def imprime_menu():
    print("1 Adicionar item")
    print("2 Remover item")
    print("3 Ver lista")
    print("4 Sair")
    return input("Escolha uma opção: ")

continua = True

while(continua):
    escolha = imprime_menu()

    if escolha == '4':
        print('Até mais!')
        break
    elif escolha == '3':
        print(lista_compras)
    elif escolha == '1':
        item = input("Digite um item: ")
        lista_compras.append(item)
    elif escolha == '2':
        item = input("Digite um item: ")
        if item in lista_compras:
            lista_compras.remove(item)
        else:
            print('Item não encontrado!')
    else:
        print('Opção inválida')