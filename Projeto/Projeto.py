# Importe da função permutations
from itertools import permutations

# Criação da Matriz e leitura do .txt contendo a matriz
Matriz = []
Matriz_Entrada = open('/Users/Caio_/Documents/GitHub/PISI2/Projeto\MatrizEntrada.txt', 'r')

# Quantidade de linhas e colunas da matriz
QtdLinhas = int(Matriz_Entrada.readline(1))
QtdColunas = int(Matriz_Entrada.readline())

# Mapeando a Matriz
for i in Matriz_Entrada:
    Matriz_Entrada
    if i != "":
        Matriz.append(i.split())

# Criando o Print da Matriz e o realizando
linhas = len(Matriz)
colunas = len(Matriz[0])
def PrintMatriz(Matriz):
    for l in range(linhas):
        linha = ""
        for c in range(colunas):
            linha = linha + " " + str(Matriz[l][c])
        print(linha)

PrintMatriz(Matriz)

# Localizando os pontos da Matriz
pontos = {}
for l in range(linhas):
    for c in range(colunas):
        if Matriz[l][c] == 'R':
            pontos['RFinal'] = [l, c]
        if Matriz[l][c] != '0':
            pontos[Matriz[l][c]] = [l, c]

# Calculando a distância entre os pontos
def distancias(Coord1, Coord2):
    return abs((int(Coord1[0]) - int(Coord2[0]))) + ((int(Coord1[1]) - int(Coord2[1])))

Recebidos = permutations(pontos)
print(Recebidos)