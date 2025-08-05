# Crie um dicionário com o nome e a idade de três pessoas diferentes. Em seguida, calcule a média de idade dessas pessoas.

cadastro = {"Maria" : 15, "João" : 17, "Zé" : 16}

soma = 0
for v in cadastro.values():
    soma += v

media = soma/len(cadastro)

print(f"A idade média é de {media}")