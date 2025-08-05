# Escreva um programa que conte o número de ocorrências de cada palavra em uma frase. O programa deve ler uma frase do usuário, separar as palavras, armazená-las em um dicionário e imprimir o número de ocorrências para cada palavra.

meu_dicionario = {}
frase = input("Digite uma frase: ")

lista_de_palavras = frase.split()

for palavra in lista_de_palavras:
    if palavra in meu_dicionario.keys():
        meu_dicionario[palavra] += 1
    else:
        meu_dicionario[palavra] = 1

print(meu_dicionario)