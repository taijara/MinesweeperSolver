
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


def posicao1234(n_linhas, n_colunas, tabuleiro):
    dicionarioQuadradosLocal = listarQuadradosLocal(n_linhas, n_colunas, tabuleiro)
    dicionarioQuadradosValor = listarQuadradosValor(n_linhas, n_colunas, tabuleiro)
    ocorrencia = []
    d = 1
    A = []
    B = []
    C = []
    D = []
    E = []
    F = []
    G = []
    H = []
    I = []
    J = []
    while d < len(dicionarioQuadradosValor):
        if dicionarioQuadradosLocal[d][0] >= 0 and dicionarioQuadradosLocal[d][0] < n_linhas and \
                dicionarioQuadradosLocal[d][1] >= 0 and dicionarioQuadradosLocal[d][1] < (n_colunas - 1):
            if dicionarioQuadradosValor[d] == [1, 'I'] and dicionarioQuadradosValor[d + 1] == [1, 'I']:
                if (dicionarioQuadradosLocal[d][1] - 1) >= 0:
                    A = dicionarioQuadradosValor[d - 1]
                if (dicionarioQuadradosLocal[d][0] - 1) >= 0 and (dicionarioQuadradosLocal[d][1] - 1) >= 0:
                    B = dicionarioQuadradosValor[d - n_colunas - 1]
                if (dicionarioQuadradosLocal[d][0] - 1) >= 0:
                    C = dicionarioQuadradosValor[d - n_colunas]
                    D = dicionarioQuadradosValor[d - n_colunas + 1]
                if (dicionarioQuadradosLocal[d][0] - 1) >= 0 and (dicionarioQuadradosLocal[d][1] + 2) <= (
                        n_colunas - 1):
                    E = dicionarioQuadradosValor[d - n_colunas + 2]
                if (dicionarioQuadradosLocal[d][1] + 2) <= (n_colunas - 1):
                    F = dicionarioQuadradosValor[d + 2]
                if (dicionarioQuadradosLocal[d][0] + 1) <= (n_linhas - 1) and (dicionarioQuadradosLocal[d][1] + 2) <= (
                        n_colunas - 1):
                    G = dicionarioQuadradosValor[d + n_colunas + 2]
                if (dicionarioQuadradosLocal[d][0] + 1) <= (n_linhas - 1):
                    H = dicionarioQuadradosValor[d + n_colunas + 1]
                    I = dicionarioQuadradosValor[d + n_colunas]
                if (dicionarioQuadradosLocal[d][0] + 1) <= (n_linhas - 1) and (dicionarioQuadradosLocal[d][1] - 1) >= 0:
                    J = dicionarioQuadradosValor[d + n_colunas - 1]
                print(d)
                print("vizinhos :", A, B, C, D, E, F, G, H, I, J)

                if (B != [] and B[1] == 'I') and (C != [] and C[1] == 'I') and (D != [] and D[1] == 'I'):
                    if (E == [] or E[1] == 'A') and (F == [] or F[1] == 'A') and \
                            (G == [] or G[1] == 'A') and (H == [] or H[1] == 'A') and \
                            (I == [] or I[1] == 'A') and (J == [] or J[1] == 'A') and \
                            (A == [] or A[1] == 'A'):
                        print("encontrei a posição 1 da regra 1_1")
                        ocorrencia.append(dicionarioQuadradosLocal[d - n_colunas - 1])

                if (C != [] and C[1] == 'I') and (D != [] and D[1] == 'I') and (E != [] and E[1] == 'I'):
                    if (F == [] or F[1] == 'A') and (G == [] or G[1] == 'A') and \
                            (H == [] or H[1] == 'A') and (I == [] or I[1] == 'A') and \
                            (J == [] or J[1] == 'A') and (A == [] or A[1] == 'A') and \
                            (B == [] or B[1] == 'A'):
                        print("encontrei a posição 2 da regra 1_1")
                        ocorrencia.append(dicionarioQuadradosLocal[d - n_colunas + 2])

                if (J != [] and J[1] == 'I') and (I != [] and I[1] == 'I') and (H != [] and H[1] == 'I'):
                    if (F == [] or F[1] == 'A') and (G == [] or G[1] == 'A') and \
                            (D == [] or D[1] == 'A') and (C == [] or C[1] == 'A') and \
                            (B == [] or B[1] == 'A') and (A == [] or A[1] == 'A') and \
                            (E == [] or E[1] == 'A'):
                        print("encontrei a posição 3 da regra 1_1")
                        ocorrencia.append(dicionarioQuadradosLocal[d + n_colunas - 1])

                if (G != [] and G[1] == 'I') and (I != [] and I[1] == 'I') and (H != [] and H[1] == 'I'):
                    if (F == [] or F[1] == 'A') and (J == [] or J[1] == 'A') and \
                            (D == [] or D[1] == 'A') and (C == [] or C[1] == 'A') and \
                            (B == [] or B[1] == 'A') and (A == [] or A[1] == 'A') and \
                            (E == [] or E[1] == 'A'):
                        print("encontrei a posição 4 da regra 1_1")
                        ocorrencia.append(dicionarioQuadradosLocal[d + n_colunas + 2])
        d = d + 1
    return ocorrencia


def posicao5678(n_linhas, n_colunas, tabuleiro):
    dicionarioQuadradosLocal = listarQuadradosLocal(n_linhas, n_colunas, tabuleiro)
    dicionarioQuadradosValor = listarQuadradosValor(n_linhas, n_colunas, tabuleiro)
    ocorrencia = []
    d = 1
    while d < len(dicionarioQuadradosValor):
        A = []
        B = []
        C = []
        D = []
        E = []
        F = []
        G = []
        H = []
        I = []
        J = []
        if dicionarioQuadradosLocal[d][0] >= 0 and dicionarioQuadradosLocal[d][0] < (n_linhas - 1) and \
                dicionarioQuadradosLocal[d][1] >= 0 and dicionarioQuadradosLocal[d][1] < n_colunas:
            if dicionarioQuadradosValor[d] == [1, 'I'] and dicionarioQuadradosValor[d + n_colunas] == [1, 'I']:
                if (dicionarioQuadradosLocal[d][1] - 1) >= 0:
                    A = dicionarioQuadradosValor[d - 1]
                if (dicionarioQuadradosLocal[d][0] - 1) >= 0 and (dicionarioQuadradosLocal[d][1] - 1) >= 0:
                    B = dicionarioQuadradosValor[d - n_colunas - 1]
                if (dicionarioQuadradosLocal[d][0] - 1) >= 0:
                    C = dicionarioQuadradosValor[d - n_colunas]
                if (dicionarioQuadradosLocal[d][0] - 1) >= 0 and (dicionarioQuadradosLocal[d][1] + 1) <= (n_colunas - 1):
                    D = dicionarioQuadradosValor[d - n_colunas + 1]
                if (dicionarioQuadradosLocal[d][1] + 1) <= (n_colunas - 1):
                    E = dicionarioQuadradosValor[d + 1]
                if (dicionarioQuadradosLocal[d][0] + 1) <= (n_linhas - 1) and (dicionarioQuadradosLocal[d][1] + 1) <= (n_colunas - 1):
                    F = dicionarioQuadradosValor[d + n_colunas + 1]

                if (dicionarioQuadradosLocal[d][0] + 2) <= (n_linhas - 1) and (dicionarioQuadradosLocal[d][1] + 1) <= (n_colunas - 1):
                    G = dicionarioQuadradosValor[d + (2 * n_colunas) + 1]
                if (dicionarioQuadradosLocal[d][0] + 2) <= (n_linhas - 1):
                    H = dicionarioQuadradosValor[d + (2 * n_colunas)]
                if (dicionarioQuadradosLocal[d][0] + 2) <= (n_linhas - 1) and (dicionarioQuadradosLocal[d][1] - 1) >= 0:
                    I = dicionarioQuadradosValor[d + (2 * n_colunas) - 1]

                if (dicionarioQuadradosLocal[d][0] + 1) <= (n_linhas - 1) and (dicionarioQuadradosLocal[d][1] - 1) >= 0:
                    J = dicionarioQuadradosValor[d + n_colunas - 1]
                print(d)
                print("vizinhos :", A, B, C, D, E, F, G, H, I, J)

                if (B != [] and B[1] == 'I') and (A != [] and A[1] == 'I') and (J != [] and J[1] == 'I'):
                    if (E == [] or E[1] == 'A') and (F == [] or F[1] == 'A') and \
                            (G == [] or G[1] == 'A') and (H == [] or H[1] == 'A') and \
                            (I == [] or I[1] == 'A') and (D == [] or D[1] == 'A') and \
                            (C == [] or C[1] == 'A'):
                        print("encontrei a posição 1 da regra 1_1")
                        ocorrencia.append(dicionarioQuadradosLocal[d - n_colunas - 1])

                if (F != [] and F[1] == 'I') and (D != [] and D[1] == 'I') and (E != [] and E[1] == 'I'):
                    if (C == [] or C[1] == 'A') and (G == [] or G[1] == 'A') and \
                            (H == [] or H[1] == 'A') and (I == [] or I[1] == 'A') and \
                            (J == [] or J[1] == 'A') and (A == [] or A[1] == 'A') and \
                            (B == [] or B[1] == 'A'):
                        print("encontrei a posição 2 da regra 1_1")
                        ocorrencia.append(dicionarioQuadradosLocal[d - n_colunas + 1])

                if (E != [] and E[1] == 'I') and (F != [] and F[1] == 'I') and (G != [] and G[1] == 'I'):
                    if (I == [] or I[1] == 'A') and (H == [] or H[1] == 'A') and \
                            (D == [] or D[1] == 'A') and (C == [] or C[1] == 'A') and \
                            (B == [] or B[1] == 'A') and (A == [] or A[1] == 'A') and \
                            (J == [] or J[1] == 'A'):
                        print("encontrei a posição 3 da regra 1_1")
                        ocorrencia.append(dicionarioQuadradosLocal[d + (2 * n_colunas) + 1])

                if (J != [] and J[1] == 'I') and (I != [] and I[1] == 'I') and (A != [] and A[1] == 'I'):
                    if (F == [] or F[1] == 'A') and (G == [] or G[1] == 'A') and \
                            (D == [] or D[1] == 'A') and (C == [] or C[1] == 'A') and \
                            (B == [] or B[1] == 'A') and (H == [] or H[1] == 'A') and \
                            (E == [] or E[1] == 'A'):
                        print("encontrei a posição 4 da regra 1_1")
                        ocorrencia.append(dicionarioQuadradosLocal[d + (2 * n_colunas) - 1])
        d = d + 1
    return ocorrencia


def regra_1_1(n_linhas, n_colunas, tabuleiro):
    ocorrencias = []
    pos1234 = posicao1234(n_linhas, n_colunas, tabuleiro)
    if len(pos1234) != 0:
        ocorrencias = ocorrencias + pos1234
    pos5678 = posicao5678(n_linhas, n_colunas, tabuleiro)
    if len(pos5678) != 0:
        ocorrencias = ocorrencias + pos5678
    print("ocorrencias ------------------------------------------------------------------------------------------------------------->", ocorrencias)
    return ocorrencias


def verificarPosicoes(n_linhas, n_colunas, tabuleiro):
    ocorrencias = regra_1_1(n_linhas, n_colunas, tabuleiro)
    return ocorrencias


"""
# TESTES
tab = Tabuleiro.montarTabuleiroCompleto(5, 5, 5)
dicionarioQuadradosLocal = listarQuadradosLocal(5, 5, tab)
dicionarioQuadradosValor = listarQuadradosValor(5, 5, tab)
print(dicionarioQuadradosLocal)
print(dicionarioQuadradosValor)
Tabuleiro.imprimirTabuleiro(5, tab)
n_colunas = 5
n_linhas = 5
teste(n_colunas, n_linhas, tab)
"""