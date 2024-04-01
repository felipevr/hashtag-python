### Analisador de texto

"""
Crie um programa que analise um texto fornecido pelo usuário.
O programa deve contar o número de palavras (independentemente se há repetição ou não),
a quantidade de cada palavra e a quantidade de cada letra. 
Ignore maiúsculas e minúsculas ao contar letras.
Não se preocupe com pontuação e espaços ao contar palavras.

O programa deve conter uma função chamada `analisar_texto` que recebe o texto
como parâmetro e retorna a contagem de palavras, a frequência de palavras e a
frequência de letras.

Para o texto "Olá mundo! Este é um teste. Olá novamente." o programa deve
imprimir:
    
```
Contagem de palavras: 8
Frequência de palavras: {'Olá': 2, 'mundo!': 1, 'Este': 1, 'é': 1, 'um': 1, 'teste.': 1, 'novamente.': 1}
Frequência de letras: {'o': 4, 'l': 2, 'á': 2, 'm': 3, 'u': 2, 'n': 3, 'd': 1, '!': 1, 'e': 6, 's': 2, 't': 4, 'é': 1, '.': 2, 'v': 1, 'a': 1}
```

"""

def solicitar_texto() -> str:
    return input("Digite um texto: ")

def analisar_texto(texto):
    palavras = texto.split()
    qtd = len(palavras)
    freq_palavras = {}
    freq_letras = {}

    for palavra in palavras:
        if palavra in freq_palavras:
            freq_palavras[palavra] += 1
        else:
            freq_palavras[palavra] = 1

        for letra in palavra:
            letra = letra.casefold()
            if letra in freq_letras:
                freq_letras[letra] += 1
            else:
                freq_letras[letra] = 1


    #freq_pal = {'Olá': 2, 'mundo!': 1, 'Este': 1, 'é': 1, 'um': 1, 'teste.': 1, 'novamente.': 1}
    #freq_l = {'o': 4, 'l': 2, 'á': 2, 'm': 3, 'u': 2, 'n': 3, 'd': 1, '!': 1, 'e': 6, 's': 2, 't': 4, 'é': 1, '.': 2, 'v': 1, 'a': 1}

    imprime_resultado(qtd, freq_palavras, freq_letras)

def imprime_resultado(qtd, freq_pal, freq_l):
    print('Contagem de palavras:', qtd)
    print('Frequência de palavras: ', freq_pal)
    print('Frequência de letras: ', freq_l)

def main():
    
    texto = solicitar_texto()

    if len(texto) > 0:
        analisar_texto(texto)


if __name__ == '__main__':
    main()