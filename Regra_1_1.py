# --------- Função para Listar Quadrados virados --------------
def listarQuadradosLocal(n_linhas, n_colunas, tabuleiro):
    contador = 0
    listaQuadardos = {}
    for i in range(n_linhas):
        for j in range(n_colunas):
            contador = contador + 1
            # if tabuleiro[i][j][1] == 'I':
            listaQuadardos.update({contador: (i, j)})
    return listaQuadardos


def listarQuadradosValor(n_linhas, n_colunas, tabuleiro):
    contador = 0
    listaQuadardos = {}
    for i in range(n_linhas):
        for j in range(n_colunas):
            contador = contador + 1
            # if tabuleiro[i][j][1] == 'I':
            listaQuadardos.update({contador: tabuleiro[i][j]})
    return listaQuadardos


"""
0xx0  
x11x  
0xx0  
"""

def posicao_1(n_linhas, n_colunas, tabuleiro):
    d = 1
    ocorrencia = []
    dicionarioQuadradosLocal = listarQuadradosLocal(n_linhas, n_colunas, tabuleiro)
    dicionarioQuadradosValor = listarQuadradosValor(n_linhas, n_colunas, tabuleiro)
    while d < len(dicionarioQuadradosValor):
        if dicionarioQuadradosLocal[d][0] >= 0 and dicionarioQuadradosLocal[d][0] < (n_linhas - 1) and \
                dicionarioQuadradosLocal[d][1] >= 0 and dicionarioQuadradosLocal[d][1] < (n_colunas - 2):
            if dicionarioQuadradosValor[d] == [1, 'A'] and dicionarioQuadradosValor[d + 1] == [1, 'A'] and \
                    dicionarioQuadradosValor[d + n_linhas - 1][1] == 'A' and \
                    dicionarioQuadradosValor[d - 1][1] == 'A' and \
                    dicionarioQuadradosValor[d - n_linhas - 1][1] == 'A' and\
                    dicionarioQuadradosValor[d - n_linhas][1] == 'A' and \
                    dicionarioQuadradosValor[d - n_linhas + 1][1] == 'A' and \
                    dicionarioQuadradosValor[d - n_linhas + 2][1] == 'A' and \
                    dicionarioQuadradosValor[d + 2][1] == 'A':
                print("achei posição 1 da regra 1_2")
                ocorrencia.append(dicionarioQuadradosLocal[d + n_linhas - 2])
        d = d + 1
    return ocorrencia


"""
0000
1100
xxx0
"""


def posicao_2(n_linhas, n_colunas, tabuleiro):
    d = 1
    ocorrencia = []
    dicionarioQuadradosLocal = listarQuadradosLocal(n_linhas, n_colunas, tabuleiro)
    dicionarioQuadradosValor = listarQuadradosValor(n_linhas, n_colunas, tabuleiro)
    while d < len(dicionarioQuadradosValor):
        if dicionarioQuadradosLocal[d][0] > 0 and dicionarioQuadradosLocal[d][0] < (n_linhas - 1) and \
                dicionarioQuadradosLocal[d][1] >= 0 and dicionarioQuadradosLocal[d][1] < (n_colunas - 2):
            if dicionarioQuadradosValor[d] == [1, 'A'] and dicionarioQuadradosValor[d + 1] == [1, 'A'] and \
                    dicionarioQuadradosValor[d + n_linhas - 1][1] == 'A' and \
                    dicionarioQuadradosValor[d - 1][1] == 'A' and \
                    dicionarioQuadradosValor[d - n_linhas - 1][1] == 'A' and\
                    dicionarioQuadradosValor[d - n_linhas][1] == 'A' and \
                    dicionarioQuadradosValor[d - n_linhas + 1][1] == 'A' and \
                    dicionarioQuadradosValor[d - n_linhas + 2][1] == 'A' and \
                    dicionarioQuadradosValor[d + 2][1] == 'A':
                print("achei posição 1 da regra 1_2")
                ocorrencia.append(dicionarioQuadradosLocal[d + n_linhas - 2])
        d = d + 1
    return ocorrencia