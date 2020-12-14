# ************
# ---------------------------------------------------------------------------------------------------
# --------------------------- MANIPULAÇÃO DO TABULERO (INICIO) --------------------------------------
# ---------------------------------------------------------------------------------------------------

# --------- Função para Virar o Quadrado --------------
def virarQuadrado(linha, coluna, tabuleiro):
    tabuleiro[linha][coluna][1] = 'A'


# -------------------------------------------------------

# --------- Função para Listar Quadrados Vizinhos --------------
def listarQuadradosVizinhos(linha, coluna, n_linhas, n_colunas):
    listaVizinhos = []
    if (coluna - 1) >= 0:
        listaVizinhos.append((linha, coluna - 1))
    if (coluna + 1) <= n_colunas - 1:
        listaVizinhos.append((linha, coluna + 1))
    if linha - 1 >= 0:
        listaVizinhos.append((linha - 1, coluna))
    if linha + 1 <= n_linhas - 1:
        listaVizinhos.append((linha + 1, coluna))
    if linha - 1 >= 0 and (coluna - 1) >= 0:
        listaVizinhos.append((linha - 1, coluna - 1))
    if linha + 1 <= n_linhas - 1 and (coluna + 1) <= n_colunas - 1:
        listaVizinhos.append((linha + 1, coluna + 1))
    if linha - 1 >= 0 and (coluna + 1) <= n_colunas - 1:
        listaVizinhos.append((linha - 1, coluna + 1))
    if linha + 1 <= n_linhas - 1 and (coluna - 1) >= 0:
        listaVizinhos.append((linha + 1, coluna - 1))
    return listaVizinhos


# --------------------------------------------------------------

# --------- Função para Virar Quadrados Vizinhos --------------
def virarQuadradosVizinhos(linha, coluna, tabuleiro, n_linhas, n_colunas):
    i = 0
    j = 0
    controle = True
    while controle:
        controle = False
        for i in range(n_linhas-1):
            for j in range(n_colunas-1):
                if tabuleiro[i][j][0] == 0 and tabuleiro[i][j][1] == 'A':
                    if j - 1 >= 0 and tabuleiro[i][j - 1][0] == 0 and tabuleiro[i][j - 1][1] == 'I':
                        tabuleiro[i][j - 1][1] = 'A'
                        controle = True
                        # print("teste 1")
                    if i - 1 >= 0 and j - 1 >= 0 and tabuleiro[i - 1][j - 1][0] == 0 and tabuleiro[i - 1][j - 1][1] == 'I':
                        tabuleiro[i - 1][j - 1][1] = 'A'
                        controle = True
                        # print("teste 2")
                    if i - 1 >= 0 and tabuleiro[i - 1][j][0] == 0 and tabuleiro[i - 1][j][1] == 'I':
                        tabuleiro[i - 1][j][1] = 'A'
                        controle = True
                        # print("teste 3")
                    if i - 1 >= 0 and j + 1 <= (n_colunas - 1) and tabuleiro[i - 1][j + 1][0] == 0 and tabuleiro[i - 1][j + 1][1] == 'I':
                        tabuleiro[i - 1][j + 1][1] = 'A'
                        controle = True
                        # print("teste 4")
                    if j + 1 <= (n_colunas - 1) and tabuleiro[i][j + 1][0] == 0 and tabuleiro[i][j + 1][1] == 'I':
                        tabuleiro[i][j + 1][1] = 'A'
                        controle = True
                        # print("teste 5")
                    if i + 1 <= (n_linhas - 1) and j + 1 <= (n_colunas - 1) and tabuleiro[i + 1][j + 1][0] == 0 and tabuleiro[i + 1][j + 1][1] == 'I':
                        tabuleiro[i + 1][j + 1][1] = 'A'
                        controle = True
                        # print("teste 6")
                    if i + 1 <= (n_linhas - 1) and tabuleiro[i + 1][j][0] == 0 and tabuleiro[i + 1][j][1] == 'I':
                        tabuleiro[i + 1][j][1] = 'A'
                        controle = True
                        # print("teste 7")
                    if i + 1 <= (n_linhas - 1) and j - 1 >= 0 and tabuleiro[i + 1][j - 1][0] == 0 and tabuleiro[i + 1][j - 1][1] == 'I':
                        tabuleiro[i + 1][j - 1][1] = 'A'
                        controle = True
                        # print("teste 8")
    """
    # print('teste inicio funcao -')
    qVizinhos = listarQuadradosVizinhos(linha, coluna, n_linhas, n_colunas)
    # print('quadrados vizinhos',qVizinhos)
    listaVirar = [(0, 0)]
    # print('lista aqui -',listaVirar)
    r = 0
    # for r in range(len(listaVirar)):
    while r < len(listaVirar):
        # print('teste loop')

        p = 0
        while p < len(qVizinhos):
            # print('p',p)
            # print('tamanho p',len(qVizinhos))
            # print('-----',qVizinhos[p][0],qVizinhos[p][1])
            # print('-----',tabuleiro[qVizinhos[p][0]][qVizinhos[p][1]][0],tabuleiro[qVizinhos[p][0]][qVizinhos[p][1]][1])
            if tabuleiro[qVizinhos[p][0]][qVizinhos[p][1]][0] == 0 and tabuleiro[qVizinhos[p][0]][qVizinhos[p][1]][1] == 'I':
                # print('estou no if')
                # print('r 1',r)
                if r == 0 and p == 0:
                    del listaVirar[r]
                if qVizinhos[p] not in listaVirar:
                    # print('------------->------------>--------->',qVizinhos[p])
                    listaVirar.append(qVizinhos[p])
                    # print(listaVirar)
            else:
                # print('estou no else')
                del qVizinhos[p]
                p = p - 1
            p = p + 1
        # print('r 2',r)
        qVizinhos = listarQuadradosVizinhos(listaVirar[r][0], listaVirar[r][1], n_linhas, n_colunas)
        # print('quadrados vizinhos',qVizinhos)
        r = r + 1

    # print('lista para virar -',listaVirar)

    q = 0
    for cont in range(len(listaVirar)):
        i = listaVirar[q][0]
        j = listaVirar[q][1]
        x = 1
        while 0 <= (i - x) < n_linhas and 0 <= (j - x) < n_colunas and tabuleiro[i - x][j - x][0] == 0:
            tabuleiro[i - x][j - x][1] = 'A'
            x = x + 1

        x = 1
        while 0 <= (i - x) < n_linhas and 0 <= (j) < n_colunas and tabuleiro[i - x][j][0] == 0:
            tabuleiro[i - x][j][1] = 'A'
            x = x + 1

        x = 1
        while (0 <= (i - x) < n_linhas and 0 <= (j + x) < n_colunas and tabuleiro[i - x][j + x][0] == 0):
            tabuleiro[i - x][j + x][1] = 'A'
            x = x + 1

        x = 1
        while (0 <= (i) < n_linhas and 0 <= (j - x) < n_colunas and tabuleiro[i][j - x][0] == 0):
            tabuleiro[i][j - x][1] = 'A'
            x = x + 1

        x = 1
        while (0 <= (i) < n_linhas and 0 <= (j + x) < n_colunas and tabuleiro[i][j + x][0] == 0):
            tabuleiro[i][j + x][1] = 'A'
            x = x + 1

        x = 1
        while (0 <= (i + x) < n_linhas and 0 <= (j - x) < n_colunas and tabuleiro[i + x][j - x][0] == 0):
            tabuleiro[i + x][j - x][1] = 'A'
            x = x + 1

        x = 1
        while (0 <= (i + x) < n_linhas and 0 <= (j) < n_colunas and tabuleiro[i + x][j][0] == 0):
            tabuleiro[i + x][j][1] = 'A'
            x = x + 1

        x = 1
        while (0 <= (i + x) < n_linhas and 0 <= (j + x) < n_colunas and tabuleiro[i + x][j + x][0] == 0):
            tabuleiro[i + x][j + x][1] = 'A'
            x = x + 1

        q = q + 1
    """

# ---------------------------------------------------------------

# --------- Função para Validar o Quadrado --------------
def validarQuadrado(linha, coluna, tabuleiro):
    if tabuleiro[linha][coluna][1] == 'A' and tabuleiro[linha][coluna][0] == 'B':
        verificacao = 'bomba'
    else:
        verificacao = 'ok'
    return verificacao


# -------------------------------------------------------

# --------- Função para Indicar Quadrado Suspeito -------
def indicarSuspeito(tabuleiro, i, j):
    tabuleiro[i][j][1] = 'S'


# -------------------------------------------------------


# --------- Função para colocar Flag no Quadrado --------------
def colocarFlag(tabuleiro, i, j):
    tabuleiro[i][j][1] = 'F'


# -------------------------------------------------------

# --------- Função 'Click' --------------
def click(linha, coluna, tabuleiro, n_linhas, n_colunas):
    virarQuadrado(linha, coluna, tabuleiro)
    print("quadrado clicado - [", linha, ",", coluna, "]")
    resultado = validarQuadrado(linha, coluna, tabuleiro)
    print(resultado)
    # print(tabuleiro[linha][coluna])
    # print(tabuleiro[linha][coluna][0])
    if (resultado == 'ok'):
        #if (tabuleiro[linha][coluna][1] == 'A' and tabuleiro[linha][coluna][0] == 0):
        virarQuadradosVizinhos(linha, coluna, tabuleiro, n_linhas, n_colunas)
        status = 'continuar'
    else:
        status = 'interromper'

    return status


# ---------------------------------------------------------------

# --------- Função para Listar Quadrados virados --------------
def listarQuadradosInativos(n_linhas, n_colunas, tabuleiro):
    contador = 0
    listaQuadardosInativos = []
    for i in range(n_linhas):
        for j in range(n_colunas):
            contador = contador + 1
            if (tabuleiro[i][j][1] == 'I'):
                listaQuadardosInativos.append(contador)
    return listaQuadardosInativos


# -------------------------------------------------------------

# --------- Função para Identificar o Quadrados por um Número Indice --------------
def encontrarQuadradoPeloNumero(numero, n_linhas, n_colunas, tabuleiro):
    contador = 0
    for i in range(n_linhas):
        for j in range(n_colunas):
            contador = contador + 1
            if (numero == contador):
                break
        if (numero == contador):
            break
    quadrado = [i, j]
    return quadrado

def contarBombasMarcadas(n_linhas, n_colunas, tabuleiro):
    contador = 0
    for i in range(n_linhas):
        for j in range(n_colunas):
            if tabuleiro[i][j][1] == 'F':
                contador = contador + 1
    return contador


# --------------------------------------------------------------------------------

# ---------------------------------------------------------------------------------------------------
# ------------------------------ MANIPULAÇÃO DO TABULERO (FIM) --------------------------------------
# ---------------------------------------------------------------------------------------------------
# ************