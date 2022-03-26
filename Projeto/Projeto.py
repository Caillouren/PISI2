def PrintMatriz(matriz):
    linhas = len(matriz)
    colunas = len(matriz[0])
    for l in range(linhas):
        linha = ""
        for c in range(colunas):
            linha = linha + " " + str(matriz[l][c])
        print(linha)

matriz = [[1,2,3],[4,5,6]]
PrintMatriz(matriz)
