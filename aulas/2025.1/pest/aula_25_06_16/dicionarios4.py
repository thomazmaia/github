# DICIONÁRIOS ANINHADOS

livros = {
    "livro1" : {"Autor" : "Alguem",
                "Titulo" : "A volta dos que não foram",
                "Ano" : 2025},
    "livro2" : {"Autor" : "Ninguém",
                "Titulo" : "Poeira em alto mar",
                "Ano" : 2000}
}

# Acessando informações da primeira camada:
print(livros["livro1"])

# Acessando informações da segunda camada:
print(livros["livro2"]["Titulo"])