### Analisador de Texto

"""
Crie um programa que analise um texto fornecido pelo usuário. O programa deve contar o número de palavras (independentemente se há repetição ou não), 
a quantidade de cada palavra e a quantidade de cada letra. 
Ignore maiúsculas e minúsculas ao contar letras (ou seja, transforme tudo para minúsculas). 
Faça o devido tratamento para pontuação e espaços ao contar palavras.

O programa deve conter uma função chamada `analisar_texto` que recebe o texto como parâmetro e retorna a contagem de palavras, 
a frequência de palavras e a frequência de letras. A função deve ser devidamente documentada.

Para o texto "Olá mundo! Este é um teste. Olá novamente." o programa deve imprimir:

```
Contagem de palavras: 8
Frequência de palavras: Counter({'Olá': 2, 'mundo': 1, 'Este': 1, 'é': 1, 'um': 1, 'teste': 1, 'novamente': 1})
Frequência de letras: Counter({' ': 7, 'e': 6, 'o': 4, 't': 4, 'm': 3, 'n': 3, 'l': 2, 'á': 2, 'u': 2, 's': 2, 'd': 1, 'é': 1, 'v': 1, 'a': 1})
```

Dica: use o módulo `string` para obter uma lista de caracteres de pontuação. Exemplo:

```python
import string
print(string.punctuation)
```

Dica: use o módulo `collections` para obter um contador de palavras e letras. Exemplo:

```python
from collections import Counter
print(Counter(['a', 'b', 'a', 'c', 'b', 'a']))
print(Counter('abacba'))
``` 
"""

import string
from collections import Counter


def solicitar_texto() -> str:
    return input("Digite um texto: ")

def analisar_texto(texto):
    for ponto in string.punctuation:
        texto = texto.replace(ponto, '')
    palavras = texto.split()
    qtd = len(palavras)
    
    freq_letras = Counter(texto.casefold())

    freq_palavras = dict(Counter(palavras))
        
    freq_letras = dict(freq_letras)

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