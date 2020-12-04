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
Lxx  
011   Lxx0 0110 0000
000  

0xxL
0110   0xxL 0110 0000
0000

0000
0110   0000 0110 0xxL
0xxL

0000
0110   0000 0110 Lxx0
LXX0
"""

def posicao_x(n_linhas, n_colunas, tabuleiro):
    d = 1
    ocorrencia = []
    dicionarioQuadradosLocal = listarQuadradosLocal(n_linhas, n_colunas, tabuleiro)
    dicionarioQuadradosValor = listarQuadradosValor(n_linhas, n_colunas, tabuleiro)
    while d < len(dicionarioQuadradosValor):
        if dicionarioQuadradosValor[d] == [1, 'A'] and dicionarioQuadradosValor[d + 1] == [1, 'A']:
                if (d - n_colunas - 1) >= 0 and \
                        dicionarioQuadradosValor[d - n_colunas - 1][1] == 'I' and \
                        (dicionarioQuadradosValor[d - n_colunas][1] == 'I' or dicionarioQuadradosValor[d - n_colunas + 1][1] == 'I'):
                    print("achei posição 1 da regra 1_1")
                    ocorrencia.append(dicionarioQuadradosLocal[d - n_colunas - 1])
                if (d - n_colunas + 2) > 0 and \
                        dicionarioQuadradosValor[d - n_colunas + 2][1] == 'I' and \
                        (dicionarioQuadradosValor[d - n_colunas][1] == 'I' or dicionarioQuadradosValor[d - n_colunas + 1][1] == 'I'):
                    print("achei posição 2 da regra 1_1")
                    ocorrencia.append(dicionarioQuadradosLocal[d - n_colunas + 2])
                if (d + n_colunas + 2) <= (n_linhas * n_colunas) and \
                        dicionarioQuadradosValor[d - n_colunas + 2][1] == 'I' and \
                        (dicionarioQuadradosValor[d + n_colunas][1] == 'I' or dicionarioQuadradosValor[d + n_colunas + 1][1] == 'I'):
                    print("achei posição 3 da regra 1_1")
                    ocorrencia.append(dicionarioQuadradosLocal[d + n_colunas + 2])
                if (d + n_colunas - 1) < (n_linhas * n_colunas) and \
                        dicionarioQuadradosValor[d + n_colunas - 1][1] == 'I' and \
                        (dicionarioQuadradosValor[d + n_colunas][1] == 'I' or dicionarioQuadradosValor[d + n_colunas + 1][1] == 'I'):
                    print("achei posição 4 da regra 1_1")
                    ocorrencia.append(dicionarioQuadradosLocal[d + n_colunas - 1])
        d = d + 1
    return ocorrencia


"""
Lxx0  
01103
   Lxx0 0110 0000
0000  
"""

def posicao_1(n_linhas, n_colunas, tabuleiro):
    d = 1
    ocorrencia = []
    dicionarioQuadradosLocal = listarQuadradosLocal(n_linhas, n_colunas, tabuleiro)
    dicionarioQuadradosValor = listarQuadradosValor(n_linhas, n_colunas, tabuleiro)
    while d < len(dicionarioQuadradosValor):
        if dicionarioQuadradosValor[d] == [1, 'A'] and dicionarioQuadradosValor[d + 1] == [1, 'A']:
                if (d - n_colunas - 1) >= 0 and \
                        dicionarioQuadradosValor[d - n_colunas - 1][1] == 'I' and \
                        (dicionarioQuadradosValor[d - n_colunas][1] == 'I' or dicionarioQuadradosValor[d - n_colunas + 1][1] == 'I'):
                    print("achei posição 1 da regra 1_1")
                    ocorrencia.append(dicionarioQuadradosLocal[d - n_colunas - 1])
        d = d + 1
    return ocorrencia
