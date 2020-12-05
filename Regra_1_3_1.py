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
000x
001x
013x
xxxx
"""

def posicao_1(n_linhas, n_colunas, tabuleiro):
    d = 1
    ocorrencia = []
    dicionarioQuadradosLocal = listarQuadradosLocal(n_linhas, n_colunas, tabuleiro)
    dicionarioQuadradosValor = listarQuadradosValor(n_linhas, n_colunas, tabuleiro)
    while d < len(dicionarioQuadradosValor):
        if dicionarioQuadradosLocal[d][0] > 1 and dicionarioQuadradosLocal[d][0] < (n_linhas - 1) and \
                dicionarioQuadradosLocal[d][1] > 1 and dicionarioQuadradosLocal[d][1] < (n_colunas - 1):
            if dicionarioQuadradosValor[d] == [3, 'A'] and dicionarioQuadradosValor[d - n_colunas] == [1, 'A'] and dicionarioQuadradosValor[d - 1] == [1, 'A'] and \
                    dicionarioQuadradosValor[d - (2 * n_colunas)][1] == 'A' and \
                    dicionarioQuadradosValor[d - (2 * n_colunas) - 1][1] == 'A' and \
                    dicionarioQuadradosValor[d - n_colunas - 1][1] == 'A' and \
                    dicionarioQuadradosValor[d - n_colunas - 2][1] == 'A' and \
                    dicionarioQuadradosValor[d - 2][1] == 'A' and \
                    dicionarioQuadradosValor[d + n_colunas + 1][1] == 'I':
                print("achei posição 1 da regra 1_3_1")
                tabuleiro[dicionarioQuadradosLocal[d - (2 * n_colunas)][0]][dicionarioQuadradosLocal[d + 1][1]][1] = 'F'
                tabuleiro[dicionarioQuadradosLocal[d + n_colunas][0]][dicionarioQuadradosLocal[d - 2][1]][1] = 'F'
                ocorrencia.append(dicionarioQuadradosLocal[d + n_colunas + 1])
        d = d + 1
    return ocorrencia


"""
x000
x100
x310
xxxx
"""

# espelhamento da posição 1
def posicao_2(n_linhas, n_colunas, tabuleiro):
    d = 1
    ocorrencia = []
    dicionarioQuadradosLocal = listarQuadradosLocal(n_linhas, n_colunas, tabuleiro)
    dicionarioQuadradosValor = listarQuadradosValor(n_linhas, n_colunas, tabuleiro)
    while d < len(dicionarioQuadradosValor):
        if dicionarioQuadradosLocal[d][0] > 1 and dicionarioQuadradosLocal[d][0] < (n_linhas - 1) and \
                dicionarioQuadradosLocal[d][1] > 0 and dicionarioQuadradosLocal[d][1] < (n_colunas - 1):
            if dicionarioQuadradosValor[d] == [3, 'A'] and dicionarioQuadradosValor[d - n_colunas] == [1, 'A'] and dicionarioQuadradosValor[d + 1] == [1, 'A'] and \
                    dicionarioQuadradosValor[d - (2 * n_colunas)][1] == 'A' and \
                    dicionarioQuadradosValor[d - (2 * n_colunas) + 1][1] == 'A' and \
                    dicionarioQuadradosValor[d - n_colunas + 1][1] == 'A' and \
                    dicionarioQuadradosValor[d - n_colunas + 2][1] == 'A' and \
                    dicionarioQuadradosValor[d + 2][1] == 'A' and \
                    dicionarioQuadradosValor[d + n_colunas - 1][1] == 'I':
                print("achei posição 2 da regra 1_3_1")
                tabuleiro[dicionarioQuadradosLocal[d - (2 * n_colunas)][0]][dicionarioQuadradosLocal[d - 1][1]][1] = 'F'
                tabuleiro[dicionarioQuadradosLocal[d + n_colunas][0]][dicionarioQuadradosLocal[d + 2][1]][1] = 'F'
                ocorrencia.append(dicionarioQuadradosLocal[d + n_colunas - 1])
        d = d + 1
    return ocorrencia


"""
xxxx
013x
001x
000x
"""

# rotacao 90 posicao 1
def posicao_3(n_linhas, n_colunas, tabuleiro):
    d = 1
    ocorrencia = []
    dicionarioQuadradosLocal = listarQuadradosLocal(n_linhas, n_colunas, tabuleiro)
    dicionarioQuadradosValor = listarQuadradosValor(n_linhas, n_colunas, tabuleiro)
    while d < len(dicionarioQuadradosValor):
        if dicionarioQuadradosLocal[d][0] > 0 and dicionarioQuadradosLocal[d][0] < (n_linhas - 2) and \
                dicionarioQuadradosLocal[d][1] > 1 and dicionarioQuadradosLocal[d][1] < (n_colunas - 1):
            if dicionarioQuadradosValor[d] == [3, 'A'] and dicionarioQuadradosValor[d + n_colunas] == [1, 'A'] and dicionarioQuadradosValor[d - 1] == [1, 'A'] and \
                    dicionarioQuadradosValor[d - 2][1] == 'A' and \
                    dicionarioQuadradosValor[d + n_colunas - 2][1] == 'A' and \
                    dicionarioQuadradosValor[d + n_colunas - 1][1] == 'A' and \
                    dicionarioQuadradosValor[d + (2 * n_colunas) - 1][1] == 'A' and \
                    dicionarioQuadradosValor[d + (2 * n_colunas)][1] == 'A' and \
                    dicionarioQuadradosValor[d - n_colunas + 1][1] == 'I':
                print("achei posição 3 da regra 1_3_1")
                tabuleiro[dicionarioQuadradosLocal[d + (2 * n_colunas)][0]][dicionarioQuadradosLocal[d + 1][1]][1] = 'F'
                tabuleiro[dicionarioQuadradosLocal[d - n_colunas][0]][dicionarioQuadradosLocal[d - 2][1]][1] = 'F'
                ocorrencia.append(dicionarioQuadradosLocal[d - n_colunas + 1])
        d = d + 1
    return ocorrencia


"""
xxxx
x310
x100
x000
"""

def posicao_4(n_linhas, n_colunas, tabuleiro):
    d = 1
    ocorrencia = []
    dicionarioQuadradosLocal = listarQuadradosLocal(n_linhas, n_colunas, tabuleiro)
    dicionarioQuadradosValor = listarQuadradosValor(n_linhas, n_colunas, tabuleiro)
    while d < len(dicionarioQuadradosValor):
        if dicionarioQuadradosLocal[d][0] > 0 and dicionarioQuadradosLocal[d][0] < (n_linhas - 2) and \
                dicionarioQuadradosLocal[d][1] > 0 and dicionarioQuadradosLocal[d][1] < (n_colunas - 2):
            if dicionarioQuadradosValor[d] == [3, 'A'] and dicionarioQuadradosValor[d + n_colunas] == [1, 'A'] and dicionarioQuadradosValor[d + 1] == [1, 'A'] and \
                    dicionarioQuadradosValor[d + 2][1] == 'A' and \
                    dicionarioQuadradosValor[d + n_colunas + 2][1] == 'A' and \
                    dicionarioQuadradosValor[d + n_colunas + 1][1] == 'A' and \
                    dicionarioQuadradosValor[d + (2 * n_colunas) + 1][1] == 'A' and \
                    dicionarioQuadradosValor[d + (2 * n_colunas)][1] == 'A' and \
                    dicionarioQuadradosValor[d - n_colunas - 1][1] == 'I':
                print("achei posição 4 da regra 1_3_1")
                tabuleiro[dicionarioQuadradosLocal[d + (2 * n_colunas)][0]][dicionarioQuadradosLocal[d - 1][1]][1] = 'F'
                tabuleiro[dicionarioQuadradosLocal[d - n_colunas][0]][dicionarioQuadradosLocal[d + 2][1]][1] = 'F'
                ocorrencia.append(dicionarioQuadradosLocal[d - n_colunas - 1])
        d = d + 1
    return ocorrencia


def regra_1_3_1(n_linhas, n_colunas, tabuleiro):
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
    ocorrencias = regra_1_3_1(n_linhas, n_colunas, tabuleiro)
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