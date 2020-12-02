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

""" TESTES
tab = Tabuleiro.montarTabuleiroCompleto(5, 5, 5)
dicionarioQuadradosLocal = listarQuadradosLocal(5, 5, tab)
dicionarioQuadradosValor = listarQuadradosValor(5, 5, tab)
Tabuleiro.imprimirTabuleiro(5, tab)
regra_1_2(5, 5, tab)
"""
