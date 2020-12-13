# ----------------- Imports ----------------------
import random


# ************
# ---------------------------------------------------------------------------------------------------
# --------------------------- MONTAGEM DO TABULERO (INICIO) -----------------------------------------
# ---------------------------------------------------------------------------------------------------

# --------- Função Para Criar Matriz --------------
def crie_matriz(n_linhas, n_colunas, valor, status):
    '''
    Cria e retorna uma matriz com n_linhas x n_colunas
    em que cada elemento é iniciado com o valor passado por parametro.
    '''

    matriz = []  # lista vazia
    for i in range(n_linhas):
        # cria a linha i
        linha = []  # lista vazia
        for j in range(n_colunas):
            linha.append([valor, status])

        # coloque linha na matriz
        matriz.append(linha)

    return matriz


# --------------------------------------------------

# --------- Função Para Sortear bombas na Matriz --------------
def sortearBombas(A, n_linhas, n_colunas, qtdBombas):
    bombas = random.sample(range(0, (n_linhas * n_colunas - 1)), qtdBombas)
    valor = 0
    # print("Lista das Bombas - ", bombas)
    for i in range(n_linhas):
        for j in range(n_colunas):
            if (valor in bombas):
                A[i][j][0] = 'B'
            valor = valor + 1


# -------------------------------------------------------------


# --------- Função Para Preencher campos que não são bombas --------------
def prencherCamposNum(A, n_linhas, n_colunas):
    for i in range(n_linhas):
        contador = 0
        for j in range(n_colunas):
            if A[i][j][0] == 0:
                if 0 <= (i - 1) < n_linhas and 0 <= (j - 1) < n_colunas and A[i - 1][j - 1][0] == 'B':
                    contador = contador + 1
                if 0 <= (i - 1) < n_linhas and 0 <= (j) < n_colunas and A[i - 1][j][0] == 'B':
                    contador = contador + 1
                if 0 <= (i - 1) < n_linhas and 0 <= (j + 1) < n_colunas and A[i - 1][j + 1][0] == 'B':
                    contador = contador + 1
                if 0 <= (i) < n_linhas and 0 <= (j - 1) < n_colunas and A[i][j - 1][0] == 'B':
                    contador = contador + 1
                if 0 <= (i) < n_linhas and 0 <= (j + 1) < n_colunas and A[i][j + 1][0] == 'B':
                    contador = contador + 1
                if 0 <= (i + 1) < n_linhas and 0 <= (j - 1) < n_colunas and A[i + 1][j - 1][0] == 'B':
                    contador = contador + 1
                if 0 <= (i + 1) < n_linhas and 0 <= (j) < n_colunas and A[i + 1][j][0] == 'B':
                    contador = contador + 1
                if 0 <= (i + 1) < n_linhas and 0 <= (j + 1) < n_colunas and A[i + 1][j + 1][0] == 'B':
                    contador = contador + 1
                A[i][j][0] = contador
                contador = 0


# ------------------------------------------------------------------------

# --------- Função Montar Tabuleiro Completo --------------
def montarTabuleiroCompleto(n_linhas, n_colunas, qtdBombas):
    tabuleiro = crie_matriz(n_linhas, n_colunas, 0, 'I')
    sortearBombas(tabuleiro, n_linhas, n_colunas, qtdBombas)
    prencherCamposNum(tabuleiro, n_linhas, n_colunas)
    return tabuleiro


# ---------------------------------------------------------

# ------------ Função para Imprimir Tabuleiro --------------
def imprimirTabuleiro(n_linhas, tabuleiro):
    for i in range(n_linhas):
        print(tabuleiro[i])
# ----------------------------------------------------------

# ---------------------------------------------------------------------------------------------------
# ------------------------------ MONTAGEM DO TABULERO (FIM) -----------------------------------------
# ---------------------------------------------------------------------------------------------------
# ************
