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


"""
0000
0120
xxxx
"""

def posicao_1(n_linhas, n_colunas, tabuleiro):
    d = 1
    ocorrencia = []
    dicionarioQuadradosLocal = listarQuadradosLocal(n_linhas, n_colunas, tabuleiro)
    dicionarioQuadradosValor = listarQuadradosValor(n_linhas, n_colunas, tabuleiro)
    while d < len(dicionarioQuadradosValor):
        if dicionarioQuadradosLocal[d][0] > 0 and dicionarioQuadradosLocal[d][0] < (n_linhas - 1) and \
                dicionarioQuadradosLocal[d][1] > 0 and dicionarioQuadradosLocal[d][1] < (n_colunas - 2):
            if dicionarioQuadradosValor[d] == [1, 'A'] and dicionarioQuadradosValor[d + 1] == [2, 'A'] and \
                    dicionarioQuadradosValor[d - 1][1] == 'A' and \
                    dicionarioQuadradosValor[d + 2][1] == 'A' and \
                    dicionarioQuadradosValor[d - n_colunas][1] == 'A' and \
                    dicionarioQuadradosValor[d - n_colunas + 1][1] == 'A' and \
                    dicionarioQuadradosValor[d - n_colunas + 2][1] == 'A' and \
                    dicionarioQuadradosValor[d - n_colunas - 1][1] == 'A' and \
                    dicionarioQuadradosValor[d + n_colunas + 2][1] == 'I':
                print("achei posição 1 da regra 1_2")
                tabuleiro[dicionarioQuadradosLocal[d + n_colunas][0]][dicionarioQuadradosLocal[d + 2][1]][1] = 'F'
                ocorrencia.append(dicionarioQuadradosLocal[d + n_colunas - 1])
        d = d + 1
    return ocorrencia


"""
xxxx
0120
0000
"""

# espelhamento da posição 1
def posicao_2(n_linhas, n_colunas, tabuleiro):
    d = 1
    ocorrencia = []
    dicionarioQuadradosLocal = listarQuadradosLocal(n_linhas, n_colunas, tabuleiro)
    dicionarioQuadradosValor = listarQuadradosValor(n_linhas, n_colunas, tabuleiro)
    while d < len(dicionarioQuadradosValor):
        if dicionarioQuadradosLocal[d][0] > 0 and dicionarioQuadradosLocal[d][0] < (n_linhas - 1) and \
                dicionarioQuadradosLocal[d][1] > 0 and dicionarioQuadradosLocal[d][1] < (n_colunas - 2):
            if dicionarioQuadradosValor[d] == [1, 'A'] and dicionarioQuadradosValor[d + 1] == [2, 'A'] and \
                    dicionarioQuadradosValor[d - 1][1] == 'A' and \
                    dicionarioQuadradosValor[d + 2][1] == 'A' and \
                    dicionarioQuadradosValor[d - n_colunas + 2][1] == 'I' and \
                    dicionarioQuadradosValor[d + n_colunas][1] == 'A' and \
                    dicionarioQuadradosValor[d + n_colunas + 1][1] == 'A' and \
                    dicionarioQuadradosValor[d + n_colunas + 2][1] == 'A' and \
                    dicionarioQuadradosValor[d + n_colunas - 1][1] == 'A':
                print("achei posição 2 da regra 1_2")
                tabuleiro[dicionarioQuadradosLocal[d - n_colunas][0]][dicionarioQuadradosLocal[d + 2][1]][1] = 'F'
                ocorrencia.append(dicionarioQuadradosLocal[d - n_colunas - 1])
        d = d + 1
    return ocorrencia


"""
x000  ooo0
x100  o1o0
x200  o0o0
x000  0000
"""

# rotacao 90 posicao 1
def posicao_3(n_linhas, n_colunas, tabuleiro):
    d = 1
    ocorrencia = []
    dicionarioQuadradosLocal = listarQuadradosLocal(n_linhas, n_colunas, tabuleiro)
    dicionarioQuadradosValor = listarQuadradosValor(n_linhas, n_colunas, tabuleiro)
    while d < len(dicionarioQuadradosValor):
        if dicionarioQuadradosLocal[d][0] > 0 and dicionarioQuadradosLocal[d][0] < (n_linhas - 2) and \
                dicionarioQuadradosLocal[d][1] > 0 and dicionarioQuadradosLocal[d][1] < (n_colunas - 1):
            if dicionarioQuadradosValor[d] == [1, 'A'] and dicionarioQuadradosValor[d + n_colunas] == [2, 'A'] and \
                    dicionarioQuadradosValor[d + 1][1] == 'A' and \
                    dicionarioQuadradosValor[d - n_colunas][1] == 'A' and \
                    dicionarioQuadradosValor[d - n_colunas + 1][1] == 'A' and \
                    dicionarioQuadradosValor[d + n_colunas + 1][1] == 'A' and \
                    dicionarioQuadradosValor[d + (2 * n_colunas)][1] == 'A' and \
                    dicionarioQuadradosValor[d + (2 * n_colunas) + 1][1] == 'A' and \
                    dicionarioQuadradosValor[d + (2 * n_colunas) - 1][1] == 'I':
                print("achei posição 3 da regra 1_2")
                tabuleiro[dicionarioQuadradosLocal[d + (2 * n_colunas)][0]][dicionarioQuadradosLocal[d - 1][1]][1] = 'F'
                ocorrencia.append(dicionarioQuadradosLocal[d - n_colunas - 1])
        d = d + 1
    return ocorrencia


"""
00x0  ooo0
01x0  o1o0
02x0  o0o0
00x0  0000
"""

# espelhamento posicao 3
def posicao_4(n_linhas, n_colunas, tabuleiro):
    d = 1
    ocorrencia = []
    dicionarioQuadradosLocal = listarQuadradosLocal(n_linhas, n_colunas, tabuleiro)
    dicionarioQuadradosValor = listarQuadradosValor(n_linhas, n_colunas, tabuleiro)
    while d < len(dicionarioQuadradosValor):
        if dicionarioQuadradosLocal[d][0] > 0 and dicionarioQuadradosLocal[d][0] < (n_linhas - 2) and \
                dicionarioQuadradosLocal[d][1] > 0 and dicionarioQuadradosLocal[d][1] < (n_colunas - 1):
            if dicionarioQuadradosValor[d] == [1, 'A'] and dicionarioQuadradosValor[d + n_colunas] == [2, 'A'] and \
                    dicionarioQuadradosValor[d - n_colunas][1] == 'A' and \
                    dicionarioQuadradosValor[d + (2 * n_colunas)][1] == 'A' and \
                    dicionarioQuadradosValor[d + (2 * n_colunas) + 1][1] == 'I' and \
                    dicionarioQuadradosValor[d - n_colunas - 1][1] == 'A' and \
                    dicionarioQuadradosValor[d - 1][1] == 'A' and \
                    dicionarioQuadradosValor[d + n_colunas - 1][1] == 'A' and\
                    dicionarioQuadradosValor[d + (2 * n_colunas) - 1][1] == 'A':
                print("achei posição 4 da regra 1_2")
                tabuleiro[dicionarioQuadradosLocal[d + (2 * n_colunas)][0]][dicionarioQuadradosLocal[d + 1][1]][1] = 'F'
                ocorrencia.append(dicionarioQuadradosLocal[d - n_colunas + 1])
        d = d + 1
    return ocorrencia


"""
0000
0210
xxxx
"""


def posicao_5(n_linhas, n_colunas, tabuleiro):
    d = 1
    ocorrencia = []
    dicionarioQuadradosLocal = listarQuadradosLocal(n_linhas, n_colunas, tabuleiro)
    dicionarioQuadradosValor = listarQuadradosValor(n_linhas, n_colunas, tabuleiro)
    while d < len(dicionarioQuadradosValor):
        if dicionarioQuadradosLocal[d][0] > 0 and dicionarioQuadradosLocal[d][0] < (n_linhas - 1) and \
                dicionarioQuadradosLocal[d][1] > 0 and dicionarioQuadradosLocal[d][1] < (n_colunas - 2):
            if dicionarioQuadradosValor[d] == [2, 'A'] and dicionarioQuadradosValor[d + 1] == [1, 'A'] and \
                    dicionarioQuadradosValor[d - 1][1] == 'A' and \
                    dicionarioQuadradosValor[d + 2][1] == 'A' and \
                    dicionarioQuadradosValor[d - n_colunas][1] == 'A' and \
                    dicionarioQuadradosValor[d - n_colunas + 1][1] == 'A' and \
                    dicionarioQuadradosValor[d - n_colunas + 2][1] == 'A' and \
                    dicionarioQuadradosValor[d - n_colunas - 1][1] == 'A' and \
                    dicionarioQuadradosValor[d + n_colunas - 1][1] == 'I':
                print("achei posição 5 da regra 1_2")
                tabuleiro[dicionarioQuadradosLocal[d + n_colunas][0]][dicionarioQuadradosLocal[d - 1][1]][1] = 'F'
                ocorrencia.append(dicionarioQuadradosLocal[d + n_colunas + 2])
        d = d + 1
    return ocorrencia


"""
xxxx
0210
0000
"""

# espelhamento da posição 1
def posicao_6(n_linhas, n_colunas, tabuleiro):
    d = 1
    ocorrencia = []
    dicionarioQuadradosLocal = listarQuadradosLocal(n_linhas, n_colunas, tabuleiro)
    dicionarioQuadradosValor = listarQuadradosValor(n_linhas, n_colunas, tabuleiro)
    while d < len(dicionarioQuadradosValor):
        if dicionarioQuadradosLocal[d][0] > 0 and dicionarioQuadradosLocal[d][0] < (n_linhas - 1) and \
                dicionarioQuadradosLocal[d][1] > 0 and dicionarioQuadradosLocal[d][1] < (n_colunas - 2):
            if dicionarioQuadradosValor[d] == [2, 'A'] and dicionarioQuadradosValor[d + 1] == [1, 'A'] and \
                    dicionarioQuadradosValor[d - 1][1] == 'A' and \
                    dicionarioQuadradosValor[d + 2][1] == 'A' and \
                    dicionarioQuadradosValor[d - n_colunas - 1][1] == 'I' and \
                    dicionarioQuadradosValor[d + n_colunas][1] == 'A' and \
                    dicionarioQuadradosValor[d + n_colunas + 1][1] == 'A' and \
                    dicionarioQuadradosValor[d + n_colunas + 2][1] == 'A' and \
                    dicionarioQuadradosValor[d + n_colunas - 1][1] == 'A':
                print("achei posição 2 da regra 1_2")
                tabuleiro[dicionarioQuadradosLocal[d - n_colunas][0]][dicionarioQuadradosLocal[d - 1][1]][1] = 'F'
                ocorrencia.append(dicionarioQuadradosLocal[d - n_colunas + 2])
        d = d + 1
    return ocorrencia


"""
x000  ooo0
x200  o1o0
x100  o0o0
x000  0000
"""

# rotacao 90 posicao 1
def posicao_7(n_linhas, n_colunas, tabuleiro):
    d = 1
    ocorrencia = []
    dicionarioQuadradosLocal = listarQuadradosLocal(n_linhas, n_colunas, tabuleiro)
    dicionarioQuadradosValor = listarQuadradosValor(n_linhas, n_colunas, tabuleiro)
    while d < len(dicionarioQuadradosValor):
        if dicionarioQuadradosLocal[d][0] > 0 and dicionarioQuadradosLocal[d][0] < (n_linhas - 2) and \
                dicionarioQuadradosLocal[d][1] > 0 and dicionarioQuadradosLocal[d][1] < (n_colunas - 1):
            if dicionarioQuadradosValor[d] == [2, 'A'] and dicionarioQuadradosValor[1 + n_colunas] == [2, 'A'] and \
                    dicionarioQuadradosValor[d + 1][1] == 'A' and \
                    dicionarioQuadradosValor[d - n_colunas][1] == 'A' and \
                    dicionarioQuadradosValor[d - n_colunas + 1][1] == 'A' and \
                    dicionarioQuadradosValor[d + n_colunas + 1][1] == 'A' and \
                    dicionarioQuadradosValor[d + (2 * n_colunas)][1] == 'A' and \
                    dicionarioQuadradosValor[d + (2 * n_colunas) + 1][1] == 'A' and \
                    dicionarioQuadradosValor[d - n_colunas - 1][1] == 'I':
                print("achei posição 7 da regra 1_2")
                tabuleiro[dicionarioQuadradosLocal[d - n_colunas][0]][dicionarioQuadradosLocal[d - 1][1]][1] = 'F'
                ocorrencia.append(dicionarioQuadradosLocal[d + (2 * n_colunas) - 1])
        d = d + 1
    return ocorrencia


"""
00x0  ooo0
02x0  o1o0
01x0  o0o0
00x0  0000
"""

# espelhamento posicao 3
def posicao_8(n_linhas, n_colunas, tabuleiro):
    d = 1
    ocorrencia = []
    dicionarioQuadradosLocal = listarQuadradosLocal(n_linhas, n_colunas, tabuleiro)
    dicionarioQuadradosValor = listarQuadradosValor(n_linhas, n_colunas, tabuleiro)
    while d < len(dicionarioQuadradosValor):
        if dicionarioQuadradosLocal[d][0] > 0 and dicionarioQuadradosLocal[d][0] < (n_linhas - 2) and \
                dicionarioQuadradosLocal[d][1] > 0 and dicionarioQuadradosLocal[d][1] < (n_colunas - 1):
            if dicionarioQuadradosValor[d] == [2, 'A'] and dicionarioQuadradosValor[d + n_colunas] == [1, 'A'] and \
                    dicionarioQuadradosValor[d - n_colunas][1] == 'A' and \
                    dicionarioQuadradosValor[d - n_colunas + 1][1] == 'I' and \
                    dicionarioQuadradosValor[d + (2 * n_colunas)][1] == 'A' and \
                    dicionarioQuadradosValor[d - n_colunas - 1][1] == 'A' and \
                    dicionarioQuadradosValor[d - 1][1] == 'A' and \
                    dicionarioQuadradosValor[d + n_colunas - 1][1] == 'A' and\
                    dicionarioQuadradosValor[d + (2 * n_colunas) - 1][1] == 'A':
                print("achei posição 8 da regra 1_2")
                tabuleiro[dicionarioQuadradosLocal[d - n_colunas][0]][dicionarioQuadradosLocal[d + 1][1]][1] = 'F'
                ocorrencia.append(dicionarioQuadradosLocal[d + (2 * n_colunas) + 1])
        d = d + 1
    return ocorrencia


def regra_1_2(n_linhas, n_colunas, tabuleiro):
    ocorrencias = []
    pos1 = posicao_1(n_linhas, n_colunas, tabuleiro)
    if len(pos1) != 0:
        ocorrencias = ocorrencias + pos1
    pos2 = posicao_2(n_linhas, n_colunas, tabuleiro)
    if len(pos2) != 0:
        ocorrencias = ocorrencias + pos2
    pos3 = posicao_3(n_linhas, n_colunas, tabuleiro)
    if len(pos3) != 0:
        ocorrencias = ocorrencias + pos3
    pos4 = posicao_4(n_linhas, n_colunas, tabuleiro)
    if len(pos4) != 0:
        ocorrencias = ocorrencias + pos4
    pos5 = posicao_5(n_linhas, n_colunas, tabuleiro)
    if len(pos5) != 0:
        ocorrencias = ocorrencias + pos5
    pos6 = posicao_6(n_linhas, n_colunas, tabuleiro)
    if len(pos6) != 0:
        ocorrencias = ocorrencias + pos6
    pos7 = posicao_7(n_linhas, n_colunas, tabuleiro)
    if len(pos7) != 0:
        ocorrencias = ocorrencias + pos7
    pos8 = posicao_8(n_linhas, n_colunas, tabuleiro)
    if len(pos8) != 0:
        ocorrencias = ocorrencias + pos8
    print("ocorrencias ------------------------------------------------------------------------------------------------------------->", ocorrencias)
    return ocorrencias



def verificarPosicoes(n_linhas, n_colunas, tabuleiro):
    dicionarioQuadradosLocal = listarQuadradosLocal(n_linhas, n_colunas, tabuleiro)
    dicionarioQuadradosValor = listarQuadradosValor(n_linhas, n_colunas, tabuleiro)
    ocorrencias = regra_1_2(n_linhas, n_colunas, tabuleiro)
    return ocorrencias

""" 
# TESTES
tab = Tabuleiro.montarTabuleiroCompleto(6, 6, 5)
dicionarioQuadradosLocal = listarQuadradosLocal(6, 6, tab)
dicionarioQuadradosValor = listarQuadradosValor(6, 6, tab)
Tabuleiro.imprimirTabuleiro(6, tab)
resultado = ""
while resultado != "Game Over":
    resultado = CampoMinado.simularClickAleatorio(6, 6, tab)
    regra_1_2(6, 6, tab)
    Tabuleiro.imprimirTabuleiro(6, tab)
print("FIM")
Tabuleiro.imprimirTabuleiro(6, tab)
"""