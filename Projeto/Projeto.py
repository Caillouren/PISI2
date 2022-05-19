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
    if i != "":
        Matriz.append(i.split())

Matriz_Entrada.close()

# Criando o Print da Matriz e o realizando
def PrintMatriz(Matriz):
    for l in range(len(Matriz)):
        linha = ""
        for c in range(len(Matriz[0])):
            linha = linha + " " + str(Matriz[l][c])
        print(linha)

#PrintMatriz(Matriz)

# Localizando os pontos da Matriz
pontos = {}
for l in range(len(Matriz)):
    for c in range(len(Matriz[0])):
        if Matriz[l][c] == 'R':
            pontos['RF'] = [l, c]
        if Matriz[l][c] != '0':
            pontos[Matriz[l][c]] = [l, c]

#print(pontos)

# Calculando a distância entre os pontos
def distancias(Coord1, Coord2):
    return abs(((int(Coord1[0]) - int(Coord2[0])))) + abs(((int(Coord1[1]) - int(Coord2[1]))))

# Gerando as permutações e obtendo as rotas
Recebidos = permutations(pontos)
Distancia = []
Rotas = {}
for i in list(Recebidos):
    if i[0] == 'R' and i[len(i) - 1] == 'RF':
        for coordenada in range(len(i) - 1):
            Distancia.append(distancias(pontos[i[coordenada]], pontos[i[coordenada + 1]]))
            #print(i)
        #print(Distancia)
        Rotas[sum(Distancia)] = i
        Distancia = []

# print(Rotas)

# Selecionando a rota com menor percurso
Valores = []
for i in Rotas:
    Valores.append(i)
print(min(Valores))

# Removendo o ponto 'R' da menor rota
MenorRota = list(Rotas[min(Valores)])
if 'R' or 'RF' in MenorRota:
    MenorRota.remove('R') or MenorRota.remove('RF')
print(MenorRota)