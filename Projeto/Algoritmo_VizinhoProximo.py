# Import do integer de controle de limite
from sys import maxsize

# Abertura do txt e mapeamento da matriz
with open('Projeto/matriz.txt', 'r') as matriz_entrada:
    matriz = []
    
    # Dicionário para armazenar os pontos e suas coordenadas
    pontos = {}
    for i in matriz_entrada:
        matriz.append(i.split())
    matriz.remove(matriz[0]) # Remoção da linha informativa sobre a Qtd de linhas e colunas

    # Localizando os pontos e suas coordenadas na matriz
    for l in range(len(matriz)): # Número de linhas dentro da matriz
        for c in range(len(matriz[0])): # Número de elementos dentro das linhas
            if matriz[l][c] != '0':
                pontos[matriz[l][c]] = [l, c]

print(pontos)

matriz = list(pontos.keys())

# Função de cálculo de distância entre os pontos
def distancias(Coord1, Coord2):
    return abs( (Coord1[0]) - (Coord2[0]) ) + abs( (Coord1[1]) - (Coord2[1]) )

# Função de associação entre os valores e as chaves do dicionário
def encontrar_chave(valor_chave):
    for chave, valor in pontos.items():
         if valor_chave == valor:
             return chave

# Parâmetro de definição do ponto de começo
coordenada = 'R'

# Remoção do ponto de início da lista de trabalho
matriz.remove('R')

while len(matriz) != 0:
    # Lista de controle das distâncias de todos os vizinhos
    distancia = []

    # Lista de controle da posição do vizinho mais próximo
    coordenadas = []

    # Teto de controle de menor distância
    controller = maxsize

    # Main do algoritmo
    for ponto in range(len(matriz)):
        distancia.append(distancias(pontos[f'{coordenada}'], pontos[matriz[ponto]]))

        # Controle do menor percurso para o vizinho mais próximo
        if (distancias(pontos[f'{coordenada}'], pontos[matriz[ponto]])) < controller:
            coordenadas.append(pontos[matriz[ponto]])
            controller = (distancias(pontos[f'{coordenada}'], pontos[matriz[ponto]]))

            # Controle da lista mantendo a coordenada do vizinho mais próximo
            if len(coordenadas) >= 2:
                coordenadas.remove(coordenadas[0])
    
    # Limpeza de variáveis para re-operação, cálculo dos próximos pontos
    coordenada = encontrar_chave(coordenadas[0])
    matriz.remove(f'{coordenada}')
    distancia.clear()
    # break

print(coordenada)
# print(min(distancia))
print(distancia)
print(matriz)

"""
    Salvar a rota
    Salvar a distância total da rota
    Retornar para R e somar retorno
    Print da rota e custo total associado a ela
"""