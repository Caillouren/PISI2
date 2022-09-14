# Import "permutations", MaxSize
from itertools import permutations

# Dicionário para armazenar os pontos e suas coordenadas
pontos = {}

# Abertura do txt e mapeamento da matriz
with open('Projeto/matriz.txt', 'r') as matriz_entrada:
    matriz = []
    for i in matriz_entrada:
        matriz.append(i.split())
    matriz.remove(matriz[0]) # Remoção da linha informativa sobre a Qtd de linhas e colunas

    # Localizando os pontos e suas coordenadas na matriz
    for l in range(len(matriz)): # Número de linhas dentro da matriz
        for c in range(len(matriz[0])): # Número de elementos dentro das linhas
            if matriz[l][c] != '0':
                pontos[matriz[l][c]] = [l, c]

print(pontos)

# Função de calculo de distância entre os pontos
def distancias(Coord1, Coord2):
    return abs( (Coord1[0]) - (Coord2[0]) ) + abs( (Coord1[1]) - (Coord2[1]) )