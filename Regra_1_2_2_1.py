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
000000
012210
xxxxxx
"""

def posicao_1(n_linhas, n_colunas, tabuleiro):
    d = 1
    ocorrencia = []
    dicionarioQuadradosLocal = listarQuadradosLocal(n_linhas, n_colunas, tabuleiro)
    dicionarioQuadradosValor = listarQuadradosValor(n_linhas, n_colunas, tabuleiro)
    while d < len(dicionarioQuadradosValor):
        if dicionarioQuadradosLocal[d][0] > 0 and dicionarioQuadradosLocal[d][0] < (n_linhas - 1) and \
                dicionarioQuadradosLocal[d][1] > 0 and dicionarioQuadradosLocal[d][1] < (n_colunas - 4):
            if dicionarioQuadradosValor[d] == [1, 'A'] and dicionarioQuadradosValor[d + 1] == [2, 'A'] and dicionarioQuadradosValor[d + 2] == [2, 'A'] and dicionarioQuadradosValor[d + 3] == [1, 'A'] and \
                    dicionarioQuadradosValor[d - 1][1] == 'A' and \
                    dicionarioQuadradosValor[d + 4][1] == 'A' and \
                    dicionarioQuadradosValor[d - n_colunas][1] == 'A' and \
                    dicionarioQuadradosValor[d - n_colunas + 1][1] == 'A' and \
                    dicionarioQuadradosValor[d - n_colunas + 2][1] == 'A' and \
                    dicionarioQuadradosValor[d - n_colunas + 3][1] == 'A' and \
                    dicionarioQuadradosValor[d - n_colunas + 4][1] == 'A' and \
                    dicionarioQuadradosValor[d - n_colunas - 1][1] == 'A' and \
                    dicionarioQuadradosValor[d + n_colunas + 1][1] == 'I' and\
                    dicionarioQuadradosValor[d + n_colunas + 2][1] == 'I':
                print("achei posição 1 da regra 1_2_1")
                tabuleiro[dicionarioQuadradosLocal[d + n_colunas][0]][dicionarioQuadradosLocal[d + 1][1]][1] = 'F'
                tabuleiro[dicionarioQuadradosLocal[d + n_colunas][0]][dicionarioQuadradosLocal[d + 2][1]][1] = 'F'
                ocorrencia.append(dicionarioQuadradosLocal[d + n_colunas - 1])
                ocorrencia.append(dicionarioQuadradosLocal[d + n_colunas])
                ocorrencia.append(dicionarioQuadradosLocal[d + n_colunas + 3])
                ocorrencia.append(dicionarioQuadradosLocal[d + n_colunas + 4])
        d = d + 1
    return ocorrencia


"""
xxxxxx
012210
000000
"""

# espelhamento da posição 1
def posicao_2(n_linhas, n_colunas, tabuleiro):
    d = 1
    ocorrencia = []
    dicionarioQuadradosLocal = listarQuadradosLocal(n_linhas, n_colunas, tabuleiro)
    dicionarioQuadradosValor = listarQuadradosValor(n_linhas, n_colunas, tabuleiro)
    while d < len(dicionarioQuadradosValor):
        if dicionarioQuadradosLocal[d][0] > 0 and dicionarioQuadradosLocal[d][0] < (n_linhas - 1) and \
                dicionarioQuadradosLocal[d][1] > 0 and dicionarioQuadradosLocal[d][1] < (n_colunas - 4):
            if dicionarioQuadradosValor[d] == [1, 'A'] and dicionarioQuadradosValor[d + 1] == [2, 'A'] and dicionarioQuadradosValor[d + 2] == [2, 'A']  and dicionarioQuadradosValor[d + 3] == [1, 'A'] and \
                    dicionarioQuadradosValor[d - 1][1] == 'A' and \
                    dicionarioQuadradosValor[d + 4][1] == 'A' and \
                    dicionarioQuadradosValor[d + n_colunas - 1][1] == 'A' and \
                    dicionarioQuadradosValor[d + n_colunas][1] == 'A' and \
                    dicionarioQuadradosValor[d + n_colunas + 1][1] == 'A' and \
                    dicionarioQuadradosValor[d + n_colunas + 2][1] == 'A' and \
                    dicionarioQuadradosValor[d + n_colunas + 3][1] == 'A' and \
                    dicionarioQuadradosValor[d + n_colunas + 4][1] == 'A' and \
                    dicionarioQuadradosValor[d - n_colunas + 1][1] == 'I' and \
                    dicionarioQuadradosValor[d - n_colunas + 2][1] == 'I':
                print("achei posição 2 da regra 1_2_1")
                tabuleiro[dicionarioQuadradosLocal[d - n_colunas][0]][dicionarioQuadradosLocal[d + 1][1]][1] = 'F'
                tabuleiro[dicionarioQuadradosLocal[d - n_colunas][0]][dicionarioQuadradosLocal[d + 2][1]][1] = 'F'
                ocorrencia.append(dicionarioQuadradosLocal[d - n_colunas - 1])
                ocorrencia.append(dicionarioQuadradosLocal[d - n_colunas])
                ocorrencia.append(dicionarioQuadradosLocal[d - n_colunas + 3])
                ocorrencia.append(dicionarioQuadradosLocal[d - n_colunas + 4])
        d = d + 1
    return ocorrencia


"""
x000  ooo0
x100  o1o0
x200  o0o0
x200
x100  0000
x000
"""

# rotacao 90 posicao 1
def posicao_3(n_linhas, n_colunas, tabuleiro):
    d = 1
    ocorrencia = []
    dicionarioQuadradosLocal = listarQuadradosLocal(n_linhas, n_colunas, tabuleiro)
    dicionarioQuadradosValor = listarQuadradosValor(n_linhas, n_colunas, tabuleiro)
    while d < len(dicionarioQuadradosValor):
        if dicionarioQuadradosLocal[d][0] > 0 and dicionarioQuadradosLocal[d][0] < (n_linhas - 4) and \
                dicionarioQuadradosLocal[d][1] > 0 and dicionarioQuadradosLocal[d][1] < (n_colunas - 1):
            if dicionarioQuadradosValor[d] == [1, 'A'] and dicionarioQuadradosValor[d + n_colunas] == [2, 'A'] and dicionarioQuadradosValor[d + (2 * n_colunas)] == [2, 'A'] and dicionarioQuadradosValor[d + (3 * n_colunas)] == [1, 'A'] and \
                    dicionarioQuadradosValor[d - n_colunas][1] == 'A' and \
                    dicionarioQuadradosValor[d - n_colunas + 1][1] == 'A' and \
                    dicionarioQuadradosValor[d + 1][1] == 'A' and \
                    dicionarioQuadradosValor[d + n_colunas + 1][1] == 'A' and \
                    dicionarioQuadradosValor[d + (2 * n_colunas) + 1][1] == 'A' and \
                    dicionarioQuadradosValor[d + (3 * n_colunas) + 1][1] == 'A' and \
                    dicionarioQuadradosValor[d + (4 * n_colunas) + 1][1] == 'A' and \
                    dicionarioQuadradosValor[d + (4 * n_colunas)][1] == 'A' and \
                    dicionarioQuadradosValor[d + n_colunas - 1][1] == 'I' and \
                    dicionarioQuadradosValor[d + (2 * n_colunas) - 1][1] == 'I':
                print("achei posição 3 da regra 1_2_1")
                tabuleiro[dicionarioQuadradosLocal[d + n_colunas][0]][dicionarioQuadradosLocal[d - 1][1]][1] = 'F'
                tabuleiro[dicionarioQuadradosLocal[d + (2 * n_colunas)][0]][dicionarioQuadradosLocal[d - 1][1]][1] = 'F'
                ocorrencia.append(dicionarioQuadradosLocal[d - n_colunas - 1])
                ocorrencia.append(dicionarioQuadradosLocal[d - 1])
                ocorrencia.append(dicionarioQuadradosLocal[d + (3 * n_colunas) - 1])
                ocorrencia.append(dicionarioQuadradosLocal[d + (4 * n_colunas) - 1])
        d = d + 1
    return ocorrencia


"""
000x  ooo0
001x  o1o0
002x  o0o0
002x
001x  0000
000x
"""

# espelhamento posicao 3
def posicao_4(n_linhas, n_colunas, tabuleiro):
    d = 1
    ocorrencia = []
    dicionarioQuadradosLocal = listarQuadradosLocal(n_linhas, n_colunas, tabuleiro)
    dicionarioQuadradosValor = listarQuadradosValor(n_linhas, n_colunas, tabuleiro)
    while d < len(dicionarioQuadradosValor):
        if dicionarioQuadradosLocal[d][0] > 0 and dicionarioQuadradosLocal[d][0] < (n_linhas - 4) and \
                dicionarioQuadradosLocal[d][1] > 0 and dicionarioQuadradosLocal[d][1] < (n_colunas - 1):
            if dicionarioQuadradosValor[d] == [1, 'A'] and dicionarioQuadradosValor[d + n_colunas] == [2, 'A'] and dicionarioQuadradosValor[d + (2 * n_colunas)] == [2, 'A'] and dicionarioQuadradosValor[d + (3 * n_colunas)] == [1, 'A'] and \
                    dicionarioQuadradosValor[d - n_colunas][1] == 'A' and \
                    dicionarioQuadradosValor[d - n_colunas - 1][1] == 'A' and \
                    dicionarioQuadradosValor[d - 1][1] == 'A' and \
                    dicionarioQuadradosValor[d + n_colunas - 1][1] == 'A' and \
                    dicionarioQuadradosValor[d + (2 * n_colunas) - 1][1] == 'A' and \
                    dicionarioQuadradosValor[d + (3 * n_colunas) - 1][1] == 'A' and \
                    dicionarioQuadradosValor[d + (4 * n_colunas) - 1][1] == 'A' and \
                    dicionarioQuadradosValor[d + (4 * n_colunas)][1] == 'A' and \
                    dicionarioQuadradosValor[d + n_colunas + 1][1] == 'I' and \
                    dicionarioQuadradosValor[d + (2 * n_colunas) + 1][1] == 'I':
                print("achei posição 4 da regra 1_2_1")
                tabuleiro[dicionarioQuadradosLocal[d + n_colunas][0]][dicionarioQuadradosLocal[d + 1][1]][1] = 'F'
                tabuleiro[dicionarioQuadradosLocal[d + (2 * n_colunas)][0]][dicionarioQuadradosLocal[d + 1][1]][1] = 'F'
                ocorrencia.append(dicionarioQuadradosLocal[d - n_colunas + 1])
                ocorrencia.append(dicionarioQuadradosLocal[d + 1])
                ocorrencia.append(dicionarioQuadradosLocal[d + (3 * n_colunas) + 1])
                ocorrencia.append(dicionarioQuadradosLocal[d + (4 * n_colunas) + 1])
        d = d + 1
    return ocorrencia


def regra_1_2_2_1(n_linhas, n_colunas, tabuleiro):
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
    print("ocorrencias ------------------------------------------------------------------------------------------------------------->", ocorrencias)
    return ocorrencias



def verificarPosicoes(n_linhas, n_colunas, tabuleiro):
    dicionarioQuadradosLocal = listarQuadradosLocal(n_linhas, n_colunas, tabuleiro)
    dicionarioQuadradosValor = listarQuadradosValor(n_linhas, n_colunas, tabuleiro)
    ocorrencias = regra_1_2_2_1(n_linhas, n_colunas, tabuleiro)
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