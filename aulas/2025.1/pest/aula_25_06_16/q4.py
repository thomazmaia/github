# Crie um dicionário com o nome e a idade de três pessoas diferentes. Em seguida, use um loop para imprimir o nome e a idade de cada pessoa separadamente.

cadastro = {"Maria" : 15, "João" : 17, "Zé" : 16}

for k, v in cadastro.items():
    print(f"Nome: {k} - Idade: {v}")