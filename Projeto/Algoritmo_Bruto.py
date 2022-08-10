# Import "permutations"
from itertools import permutations

# Abertura do txt e mapeamento da matriz
matriz = []
with open('/Users/Caio_/Documents/GitHub/PISI2/Projeto\matriz.txt', 'r') as matriz_entrada:
    for i in matriz_entrada:
        # print(i)
        matriz.append(i.split())
    matriz.remove(matriz[0]) # Remoção da linha informativa sobre a Qtd de linhas e colunas

# Localizando os pontos e suas coordenadas na matriz
pontos = {}
for l in range(len(matriz)): # Número de linhas dentro da matriz
    for c in range(len(matriz[0])): # Número de elementos dentro das linhas
        if matriz[l][c] == 'R':
            pontos['RF'] = [l, c]
        if matriz[l][c] != '0':
            pontos[matriz[l][c]] = [l, c]
# print(pontos)


# Função de calculo de distância entre os pontos
def distancias(Coord1, Coord2):
    return abs( (Coord1[0]) - (Coord2[0]) ) + abs( (Coord1[1]) - int(Coord2[1]) )

# Permutando as rotas
recebidos = permutations(pontos)

# Calculando a distância das rotas e encontrando a menor delas
distancia = []
rotas = {100: ('R','D')}
for i in list(recebidos):
    if i[0] == 'R' and i[len(i) - 1] == 'RF':
        for coordenada in range(len(i) - 1):
            distancia.append(distancias(pontos[i[coordenada]], pontos[i[coordenada + 1]]))
            # print(i)
        # print(distancia)

        # Transformando a key de rotas em um inteiro para seleção da menor rota
        menor_rota_anterior = list(rotas.keys())
        if sum(distancia) < int(menor_rota_anterior[0]):
            rotas.clear()
            rotas[sum(distancia)] = i
        distancia = []
        # print(rotas.keys())
# print(rotas.values())

# Menor rota
print(rotas)

# Removendo o ponto 'R' da menor rota e a transformando em uma string
menor_rota = list(rotas[int(menor_rota_anterior[0])])
if 'R' or 'RF' in menor_rota:
    menor_rota.remove('R') or menor_rota.remove('RF')
print(' '.join(menor_rota))
