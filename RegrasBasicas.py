# ************
# ---------------------------------------------------------------------------------------------------
# -------------------------------- IMPLEMENTAÇÃO DE REGRAS (INICIO) ---------------------------------
# ---------------------------------------------------------------------------------------------------
"""
0000 | x000 | xxxx | 000x | condição 1 - existir quadrado Q1 aberto(A) e com valor 1
0000 | x100 | 0120 | 001x | condição 2 - Q1 ter um vizinho Q2, tambem aberto(A) com valor 2
0120 | x200 | 0000 | 002x | condição 3 - existir 6 vizinhos consecutivos de Q1Q2 aberto(A) e com valor 0 
xxxx | x000 | 0000 | 000x | condição 4 - existir 3 vizinhos consecutivos de Q1Q2 fechado(I)
"""


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


def regra_1_2(n_linhas, n_colunas, tabuleiro):
    d = 1
    ocorrencia = "SO"
    dicionarioQuadradosLocal = listarQuadradosLocal(n_linhas, n_colunas, tabuleiro)
    dicionarioQuadradosValor = listarQuadradosValor(n_linhas, n_colunas, tabuleiro)
    while d < len(dicionarioQuadradosValor):
        if dicionarioQuadradosLocal[d][0] > 0 and dicionarioQuadradosLocal[d][0] < (n_linhas - 1) and \
                dicionarioQuadradosLocal[d][1] > 0 and dicionarioQuadradosLocal[d][1] < (n_colunas - 2):
            if dicionarioQuadradosValor[d] == [1, 'A'] and dicionarioQuadradosValor[d + 1] == [2, 'A'] and \
                    dicionarioQuadradosValor[d - 1][0] == 'A' and \
                    dicionarioQuadradosValor[d + 2][0] == 'A' and \
                    dicionarioQuadradosValor[d - n_linhas][0] == 'A' and \
                    dicionarioQuadradosValor[d - n_linhas + 1][0] == 'A' and \
                    dicionarioQuadradosValor[d - n_linhas + 2][0] == 'A' and \
                    dicionarioQuadradosValor[d - n_linhas - 1][0] == 'A' and \
                    dicionarioQuadradosValor[d + n_linhas][1] == 'I' and \
                    dicionarioQuadradosValor[d + n_linhas + 1][1] == 'I' and \
                    dicionarioQuadradosValor[d + n_linhas + 2][1] == 'I' and \
                    dicionarioQuadradosValor[d + n_linhas - 1][1] == 'I':
                print("achei regra 1_2")
                tabuleiro[dicionarioQuadradosLocal[d][0] + 1, dicionarioQuadradosLocal[d][1] + 2][1] = 'F'
                ocorrencia = dicionarioQuadradosLocal[d]
        d = d + 1
    return ocorrencia


def regra_1_1(n_linhas, n_colunas, tabuleiro):
    d = 1
    ocorrencia = "SO"
    dicionarioQuadradosLocal = listarQuadradosLocal(n_linhas, n_colunas, tabuleiro)
    dicionarioQuadradosValor = listarQuadradosValor(n_linhas, n_colunas, tabuleiro)
    while d < len(dicionarioQuadradosValor):
        if dicionarioQuadradosLocal[d][0] > 0 and dicionarioQuadradosLocal[d][0] < (n_linhas - 1) and \
                dicionarioQuadradosLocal[d][1] >= 0 and dicionarioQuadradosLocal[d][1] < (n_colunas - 2):
            if dicionarioQuadradosValor[d] == [1, 'A'] and dicionarioQuadradosValor[d + 1] == [1, 'A'] and \
                    dicionarioQuadradosValor[d - 1][0] == 'A' and \
                    dicionarioQuadradosValor[d + 2][0] == 'A' and \
                    dicionarioQuadradosValor[d - n_linhas][0] == 'A' and \
                    dicionarioQuadradosValor[d - n_linhas + 1][0] == 'A' and \
                    dicionarioQuadradosValor[d - n_linhas + 2][0] == 'A' and \
                    dicionarioQuadradosValor[d - n_linhas - 1][0] == 'A' and \
                    dicionarioQuadradosValor[d + n_linhas][1] == 'I' and \
                    dicionarioQuadradosValor[d + n_linhas + 1][1] == 'I' and \
                    dicionarioQuadradosValor[d + n_linhas + 2][1] == 'I' and \
                    dicionarioQuadradosValor[d + n_linhas - 1][1] == 'I':
                print("achei regra 1_1")
                tabuleiro[dicionarioQuadradosLocal[d][0] + 1, dicionarioQuadradosLocal[d][1] + 2][1] = 'F'
                ocorrencia = dicionarioQuadradosLocal[d]
        d = d + 1
    return ocorrencia


def regra_1_2_2_1(n_linhas, n_colunas, tabuleiro):
    d = 1
    ocorrencias = []
    dicionarioQuadradosLocal = listarQuadradosLocal(n_linhas, n_colunas, tabuleiro)
    dicionarioQuadradosValor = listarQuadradosValor(n_linhas, n_colunas, tabuleiro)
    while d < len(dicionarioQuadradosValor):
        if dicionarioQuadradosLocal[d][0] > 0 and dicionarioQuadradosLocal[d][0] < (n_linhas - 1) and \
                dicionarioQuadradosLocal[d][1] > 0 and dicionarioQuadradosLocal[d][1] < (n_colunas - 4):
            if dicionarioQuadradosValor[d] == [1, 'A'] and dicionarioQuadradosValor[d + 1] == [2, 'A'] and \
                    dicionarioQuadradosValor[d + 2] == [2, 'A'] and dicionarioQuadradosValor[d + 3] == [1, 'A'] and \
                    dicionarioQuadradosValor[d - 1][0] == 'A' and \
                    dicionarioQuadradosValor[d + 4][0] == 'A' and \
                    dicionarioQuadradosValor[d - n_linhas][0] == 'A' and \
                    dicionarioQuadradosValor[d - n_linhas + 1][0] == 'A' and \
                    dicionarioQuadradosValor[d - n_linhas + 2][0] == 'A' and \
                    dicionarioQuadradosValor[d - n_linhas + 3][0] == 'A' and \
                    dicionarioQuadradosValor[d - n_linhas + 4][0] == 'A' and \
                    dicionarioQuadradosValor[d - n_linhas - 1][0] == 'A' and \
                    dicionarioQuadradosValor[d + n_linhas][1] == 'I' and \
                    dicionarioQuadradosValor[d + n_linhas + 1][1] == 'I' and \
                    dicionarioQuadradosValor[d + n_linhas + 2][1] == 'I' and \
                    dicionarioQuadradosValor[d + n_linhas + 3][1] == 'I' and \
                    dicionarioQuadradosValor[d + n_linhas + 4][1] == 'I' and \
                    dicionarioQuadradosValor[d + n_linhas - 1][1] == 'I':
                print("achei regra 1_2_2_1")
                tabuleiro[dicionarioQuadradosLocal[d][0] + 1, dicionarioQuadradosLocal[d][1] + 1][1] = 'F'
                tabuleiro[dicionarioQuadradosLocal[d][0] + 1, dicionarioQuadradosLocal[d][1] + 2][1] = 'F'
                ocorrencias.append(dicionarioQuadradosLocal[d + n_linhas])
                ocorrencias.append(dicionarioQuadradosLocal[d + n_linhas - 1])
                ocorrencias.append(dicionarioQuadradosLocal[d + n_linhas + 3])
                ocorrencias.append(dicionarioQuadradosLocal[d + n_linhas + 4])
        d = d + 1
    return ocorrencias


def regra_1_2_1(n_linhas, n_colunas, tabuleiro):
    d = 1
    ocorrencias = []
    dicionarioQuadradosLocal = listarQuadradosLocal(n_linhas, n_colunas, tabuleiro)
    dicionarioQuadradosValor = listarQuadradosValor(n_linhas, n_colunas, tabuleiro)
    while d < len(dicionarioQuadradosValor):
        if dicionarioQuadradosLocal[d][0] > 0 and dicionarioQuadradosLocal[d][0] < (n_linhas - 1) and \
                dicionarioQuadradosLocal[d][1] > 0 and dicionarioQuadradosLocal[d][1] < (n_colunas - 3):
            if dicionarioQuadradosValor[d] == [1, 'A'] and dicionarioQuadradosValor[d + 1] == [2, 'A'] and \
                    dicionarioQuadradosValor[d + 2] == [1, 'A'] and \
                    dicionarioQuadradosValor[d - 1][0] == 'A' and \
                    dicionarioQuadradosValor[d + 3][0] == 'A' and \
                    dicionarioQuadradosValor[d - n_linhas][0] == 'A' and \
                    dicionarioQuadradosValor[d - n_linhas + 1][0] == 'A' and \
                    dicionarioQuadradosValor[d - n_linhas + 2][0] == 'A' and \
                    dicionarioQuadradosValor[d - n_linhas + 3][0] == 'A' and \
                    dicionarioQuadradosValor[d - n_linhas - 1][0] == 'A' and \
                    dicionarioQuadradosValor[d + n_linhas][1] == 'I' and \
                    dicionarioQuadradosValor[d + n_linhas + 1][1] == 'I' and \
                    dicionarioQuadradosValor[d + n_linhas + 2][1] == 'I' and \
                    dicionarioQuadradosValor[d + n_linhas + 3][1] == 'I' and \
                    dicionarioQuadradosValor[d + n_linhas - 1][1] == 'I':
                print("achei regra 1_2_1")
                tabuleiro[dicionarioQuadradosLocal[d][0] + 1, dicionarioQuadradosLocal[d][1] + 2][1] = 'F'
                tabuleiro[dicionarioQuadradosLocal[d][0] + 1, dicionarioQuadradosLocal[d][1]][1] = 'F'
                ocorrencias.append(dicionarioQuadradosLocal[d + n_linhas - 1])
                ocorrencias.append(dicionarioQuadradosLocal[d + n_linhas + 1])
                ocorrencias.append(dicionarioQuadradosLocal[d + n_linhas + 3])
        d = d + 1
    return ocorrencias


def regra_1_3_1(n_linhas, n_colunas, tabuleiro):
    d = 1
    ocorrencias = []
    dicionarioQuadradosLocal = listarQuadradosLocal(n_linhas, n_colunas, tabuleiro)
    dicionarioQuadradosValor = listarQuadradosValor(n_linhas, n_colunas, tabuleiro)
    while d < len(dicionarioQuadradosValor):
        if dicionarioQuadradosLocal[d][0] > 1 and dicionarioQuadradosLocal[d][0] < (n_linhas - 1) and \
                dicionarioQuadradosLocal[d][1] > 1 and dicionarioQuadradosLocal[d][1] < (n_colunas - 1):
            if dicionarioQuadradosValor[d] == [3, 'A'] and dicionarioQuadradosValor[d - 1] == [1, 'A'] and \
                    dicionarioQuadradosValor[d - n_linhas] == [1, 'A'] and \
                    dicionarioQuadradosValor[d - 2][0] == 'A' and \
                    dicionarioQuadradosValor[d - n_linhas-1][0] == 'A' and \
                    dicionarioQuadradosValor[d - n_linhas-2][0] == 'A' and \
                    dicionarioQuadradosValor[d - (2 * n_linhas)][0] == 'A' and \
                    dicionarioQuadradosValor[d - (2 * n_linhas)-1][0] == 'A' and \
                    dicionarioQuadradosValor[d + n_linhas][1] == 'I' and \
                    dicionarioQuadradosValor[d + n_linhas + 1][1] == 'I' and \
                    dicionarioQuadradosValor[d + 1][1] == 'I' and \
                    dicionarioQuadradosValor[d - n_linhas + 1][1] == 'I' and \
                    dicionarioQuadradosValor[d - (2 * n_linhas) + 1][0] == 'A' and \
                    dicionarioQuadradosValor[d + n_linhas - 1][1] == 'I' and\
                    dicionarioQuadradosValor[d + n_linhas - 2][1] == 'I':
                print("achei regra 1_2_1")
                tabuleiro[dicionarioQuadradosLocal[d][0] + 1, dicionarioQuadradosLocal[d][1] + 1][1] = 'F'
                ocorrencias.append(dicionarioQuadradosLocal[d + n_linhas - 2])
                ocorrencias.append(dicionarioQuadradosLocal[d - (2 * n_linhas) + 1])
        d = d + 1
    return ocorrencias


""" TESTES
tab = Tabuleiro.montarTabuleiroCompleto(5, 5, 5)
dicionarioQuadradosLocal = listarQuadradosLocal(5, 5, tab)
dicionarioQuadradosValor = listarQuadradosValor(5, 5, tab)
Tabuleiro.imprimirTabuleiro(5, tab)
regra_1_2(5, 5, tab)
"""
