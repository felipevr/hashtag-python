### Gerador de Senhas

"""
    Escreva um programa que gere uma senha aleatória com um determinado comprimento. A senha deve conter uma mistura de letras, números e caracteres especiais. O comprimento da senha deve ser fornecido pelo usuário. Se o comprimento for menor que 4, imprima uma mensagem de erro e peça ao usuário para fornecer um novo comprimento.

A senha deve ser aleatória, então cada vez que o usuário executar o programa, uma nova senha deve ser gerada. Obrigatoriamente, a senha deve conter pelo menos uma letra, um número e um caractere especial. A senha não pode conter espaços em branco.

O programa deve conter uma função chamada `gerar_senha` que recebe o comprimento da senha como parâmetro e retorna a senha gerada. Se o comprimento for inválido, a função deve retornar None.

Exemplo de saída:

```
Digite o comprimento da senha: 10
8Zn$*2q9X
```

- Dica: use a biblioteca random e a função shuffle para embaralhar os caracteres da senha.
- Dica: use a função choice, dessa mesma biblioteca, para escolher um caractere aleatório de uma string.
- Dica: use a biblioteca string para obter uma lista de caracteres válidos para a senha.
"""



import string
import random


def solicitar_tamanho() -> str:
    """
    Solicita o tamanho da senha ao usuário

    Returns:
        str: o tamanho informado
    """
    while(True):
        tamanho = input("Digite o comprimento da senha: ")
        if str.isdigit(tamanho):
            break
        else:
            print("Comprimento inválido. Digite novamente.")
    
    return int(tamanho)

def gerar_senha(tamanho):
    """
    Gera senha com tamanho informado

    Parameters:
        texto -> str : Tamanho da senha a ser gerada

    Returns:
        str : senha gerada
    """

    string.digits, string.ascii_letters, string.punctuation

    senha = ''
    
    letras = random.choice(string.ascii_letters)

    numeros = random.choice(string.digits)
        
    pontuacoes = random.choice(string.punctuation)

    tudao = string.ascii_letters + string.digits + string.punctuation + string.ascii_letters

    senha = letras+numeros+pontuacoes

    while(len(senha) < tamanho):
        senha += random.choice(tudao)

    senha = senha.split(sep=None, maxsplit=-1)

    random.shuffle(senha)

    return ''.join(senha)


def main():
    
    tamanho = solicitar_tamanho()

    if tamanho < 4:
        print('Tamanho informado muito pequeno.')

    senha = gerar_senha(tamanho)

    print(senha)


if __name__ == '__main__':
    main()