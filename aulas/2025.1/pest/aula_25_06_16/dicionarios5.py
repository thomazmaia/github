# SALVANDO DICIONÁRIOS VIA JSON

import json

livros = {
    "livro1" : {"Autor" : "Alguem",
                "Titulo" : "A volta dos que não foram",
                "Ano" : 2025},
    "livro2" : {"Autor" : "Ninguém",
                "Titulo" : "Poeira em alto mar",
                "Ano" : 2000}
}

# Como salvar:
with open("arquivo.json", "w") as f:
    json.dump(livros, f)

# Como carregar (ler):
with open("teste.json", "r") as f:
    dicio = json.load(f)

print(dicio)