string = "Parabens pra voce".lower()
meu_dicionario = dict()

for caractere in string:
    if caractere in meu_dicionario.keys():
        meu_dicionario[caractere] += 1
    else:
        meu_dicionario[caractere] = 1

print(meu_dicionario)