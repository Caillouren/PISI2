# Import
import random
from itertools import permutations

# Leitura e mapeamento, dos pontos, da Matriz
matriz = []
with open('/Users/Caio_/Documents/GitHub/PISI2/Projeto\matriz.txt', 'r') as MatrizE:
    qtdLinhas = int(MatrizE.readline(1))
    qtdColunas = int(MatrizE.readline())
    for i in MatrizE:
        if i != '':
            matriz.append(i.split())
pontos = {}
locais = []
for l in range(len(matriz)):
    for c in range(len(matriz[0])):
        if matriz[l][c] == 'R':
            pontos['RF'] = [l, c]
            locais.append('RF')
        if matriz[l][c] != '0':
            pontos[matriz[l][c]] = [l, c]
            locais.append(matriz[l][c])
# print(locais)
print(pontos)
# Gerando a população, indivíduos e parâmetros
tam_população = 24
população = []
permutação = permutations(locais)
pop = [None] * tam_população
for i in list(permutação):
    if i[0] == 'R' and i[len(i) - 1] == 'RF' and len(população) < tam_população:
        população.append(i)
for item in range(len(população)):
    pop[item] = list(população[item])
print(pop)
print(len(pop))


# Função de distância
def distancias(cidade_x, cidade_y):
    return abs(((int(cidade_x[0]) - int(cidade_y[0])))) + abs(((int(cidade_x[1]) - int(cidade_y[1]))))