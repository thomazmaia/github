# Suponha que você esteja trabalhando com um sistema de votação e precisa contar a quantidade de votos de cada candidato. Você tem uma lista com os números correspondentes aos candidatos votados. Crie um programa que calcule a quantidade de votos para cada candidato e armazene essa informação em um dicionário. Ao final, imprima o dicionário contendo cada candidato como chave e a quantidade de votos como valor.

urna = ["João", 
         "Maria", 
         "José",
         "João",
         "João",
         "Maria",
         "José",
         "Maria",
         "Maria",
         "José",
         "João"]

resultado = {"João" : 0, "Maria" : 0, "José" : 0}

for item in urna:
    resultado[item] += 1

print(resultado)