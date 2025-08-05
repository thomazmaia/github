# COMO ITERAR EM DICIONÁRIOS
# 1) Pelas chaves (keys)
# 2) Pelos valores (values)
# 3) Pelas chaves e pelos valores (keys e values)

lista_de_compras = {
    'arroz': 2, 
    'feijão': 1, 
    'óleo': 5, 
    'açúcar': 3, 
    'sal': 1
    }

# 1) Iterando pelas chaves
for chave in lista_de_compras.keys():
    print(chave)

# 2) Iterando pelos valores 
for valor in lista_de_compras.values():
    print(valor)

# 3) Iterando pelas chaves e pelos valores
for chave, valor in lista_de_compras.items():
    print(f"{chave} --> {valor}")