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
mes = ''

def formata_para_reais(numero:float) -> str:
    return 'R$ {:_.2f}'.format(numero).replace('.', ',').replace('_', '.')

def converte_de_reais(valor_str:str) -> float:
    """
    converte a string formatada em reais para formato numerico python
    """
    return float(valor_str.strip('R$ ').replace('.', '').replace(',', '.'))

def calcular_imposto_mensal(valor, verbose = True):
    """
    - 5% sobre faturamento de ISS (mensal)
    - 0,65% de PIS sobre faturamento, (mensal)
    - 3% de COFINS sobre faturmaneto, (mensal)
    """
    iss = valor * 0.05 # 5%
    pis = valor * 0.0065 # 0,65%
    cofins = valor * 0.03 # 3%

    if (verbose):
        print(f'ISS: R$ {iss:.2f}')
        print(f'PIS: R$ {pis:.2f}')
        print(f'COFINS: R$ {cofins:.2f}')

    impostos_mensais = iss + pis + cofins
    
    if (verbose):
        print(f'Total impostos mensais {mes}: R$ {impostos_mensais:.2f}')

    return impostos_mensais

def calcular_imposto_trimestral(valor, verbose = True):
    #Impostos trimestrais

    csll = valor * 0.0288 #2,88%
    ir_base = valor * 0.048 # 4,8%
    ir_adicional = 0.0
    if valor > 20000:
        tmp = valor - 20000
        ir_adicional = tmp * 0.1 # 10%

    if (verbose):
        print(f'IR base: R$ {ir_base:.2f}')
        print(f'IR Adicional: R$ {ir_adicional:.2f}')
        print(f'CSLL: R$ {csll:.2f}')

    impostos_trimestrais = ir_base + ir_adicional + csll
    
    if (verbose):
        print(f'Total impostos trimestrais {mes}: R$ {impostos_trimestrais:.2f}')

    return impostos_trimestrais

def main():
    global mes

    for mes in faturamento:
        valor = faturamento[mes]
        
        valor = converte_de_reais(valor)
        print(f'Faturamento {mes}: ', formata_para_reais(valor))
        
        #impostos mensais
        impostos_mensais = calcular_imposto_mensal(valor)

        impostos_trimestrais = 0.0

        #Impostos trimestrais
        impostos_trimestrais = calcular_imposto_trimestral(valor)

        resultado[mes] = (formata_para_reais(valor), formata_para_reais(impostos_mensais), formata_para_reais(impostos_trimestrais))


    #SAÍDA
    print(resultado)


if __name__ == '__main__':
    main()