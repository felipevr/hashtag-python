### 1- Imposto a pagar no Lucro Presumido

"""
- 5% sobre faturamento de ISS (mensal)
- 0,65% de PIS sobre faturamento, (mensal)
- 3% de COFINS sobre faturmaneto, (mensal)
- 4.8% de IR (trimestral)
- 10% de IR Adicional sobre o que ultrapassar 20mil do faturamento (trimestral)
- CSLL: 2,88% sobre faturamento (trimestral)
"""

# ENTRADA
faturamento = {
    'jan': 'R$ 95.141,98',
    'fev': 'R$ 95.425,16',
    'mar': 'R$ 89.716,31',
    'abr': 'R$ 78.459,99',
    'mai': 'R$ 71.087,28',
    'jun': 'R$ 83.911,06',
    'jul': 'R$ 56.467,26',
    'ago': 'R$ 88.513,58',
    'set': 'R$ 66.552,49',
    'out': 'R$ 80.164,07',
    'nov': 'R$ 66.964,33',
    'dez': 'R$ 71.525,25',
}

# você precisa inserir no sistema um dicionário no formato:

# resultado = {
#     'mes': (faturamento, imposto_mensal, imposto_trimestral),
# }

resultado = {}

def formata_para_reais(numero:float) -> str:
    return 'R$ {:_.2f}'.format(numero).replace('.', ',').replace('_', '.')

def converte_de_reais(valor_str:str) -> float:
    """
    converte a string formatada em reais para formato numerico python
    """
    return float(valor_str.strip('R$ ').replace('.', '').replace(',', '.'))

contames = 0
valor_trimestral = 0
for mes in faturamento:
    contames += 1
    valor = faturamento[mes]
    
    valor = converte_de_reais(valor)
    print(f'Faturamento {mes}: ', formata_para_reais(valor))

    valor_trimestral += valor
    
    #impostos mensais
    iss = valor * 0.05 # 5%
    pis = valor * 0.0065 # 0,65%
    cofins = valor * 0.03 # 3%
    print(f'ISS: R$ {iss:.2f}')
    print(f'PIS: R$ {pis:.2f}')
    print(f'COFINS: R$ {cofins:.2f}')

    impostos_mensais = iss + pis + cofins
    print(f'Total impostos mês {mes}: R$ {impostos_mensais:.2f}')

    impostos_trimestrais = 0.0

    #Impostos trimestrais
    if contames % 3 == 0:
        print(f'Faturamento trimestre: ', formata_para_reais(valor_trimestral))
        csll = valor_trimestral * 0.0288 #2,88%
        ir_base = valor_trimestral * 0.048 # 4,8%
        ir_adicional = 0.0
        if valor_trimestral > 20000:
            tmp = valor_trimestral - 20000
            ir_adicional = tmp * 0.1 # 10%

        print(f'IR base: R$ {ir_base:.2f}')
        print(f'IR Adicional: R$ {ir_adicional:.2f}')
        print(f'CSLL: R$ {csll:.2f}')

        impostos_trimestrais = ir_base + ir_adicional + csll
        print(f'Total impostos trimestre: R$ {impostos_trimestrais:.2f}')

        valor_trimestral = 0

    resultado[mes] = (formata_para_reais(valor), formata_para_reais(impostos_mensais), formata_para_reais(impostos_trimestrais))


#SAÍDA
print(resultado)
