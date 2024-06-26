# Exercícios

## 1. Tirando informações de listas e dicionários

"""
Digamos que você está analisando as vendas de produtos de uma empresa de varejo.

Essa lista tem: (produto, vendas de 2019, vendas de 2020) para cada produto.
"""

vendas_produtos = [('iphone', 558147, 951642), ('galaxy', 712350, 244295), ('ipad', 573823, 26964), ('tv', 405252, 787604), ('máquina de café', 718654, 867660), ('kindle', 531580, 78830), ('geladeira', 973139, 710331), ('adega', 892292, 646016), ('notebook dell', 422760, 694913), ('notebook hp', 154753, 539704), ('notebook asus', 887061, 324831), ('microsoft surface', 438508, 667179), ('webcam', 237467, 295633), ('caixa de som', 489705, 725316), ('microfone', 328311, 644622), ('câmera canon', 591120, 994303)]


# Crie uma lista com as vendas de 2019.

vendas_2019 = [v19 for produto, v19, v20 in vendas_produtos]

print(vendas_2019)


# - Agora, qual o maior valor de vendas de 2019?
maior = max(vendas_2019)
print('Maior valor de vendas em 2019: ', maior)


# - E se eu quisesse descobrir o produto que mais vendeu em 2019?
# Temos 2 formas de fazer, refazendo o list comprehension ou consultando a lista original

vendas_2019_2 = [(v19, produto) for produto, v19, v20 in vendas_produtos]
print(vendas_2019_2)

vendas_2019_2.sort(reverse=True)

print(vendas_2019_2)

mais_vendido = max(vendas_2019_2)

produto_mais_vendido = vendas_2019_2[0]
print('produto que mais vendeu em 2019: ', mais_vendido[1])