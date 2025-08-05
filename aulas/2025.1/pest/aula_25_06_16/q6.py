# Crie um dicionário com o nome e a pontuação de cinco jogadores diferentes. Em seguida, use um loop para calcular a média das pontuações e imprimir o resultado na tela.

ranking = {
    "Jogador 1" : 55,
    "Jogador 2" : 37,
    "Jogador 3" : 73,
    "Jogador 4" : 88,
    "Jogador 5" : 99
}

soma = 0
for v in ranking.values():
    soma += v

media = soma/len(ranking)

print(f"A pontuação média é de {media}")