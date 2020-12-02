"""
Universidade Federal da Bahia
Mestrado em Ciencia da Computação
Disciplina: Algortimos e Grafos
Versão 2.3
Controle Versão: Correção da função de click
"""

# ----------------- Imports ----------------------
import random
import Tabuleiro
import RegrasBasicas

# ------------------------------------------------


# ----- Definindo qtd bombas e tamanho da grid ---
qtdBombas = 5
qtdLinhasTabela = 8
qtdColunasTabela = 8


# --------------------------------------------------


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
    resultado = validarQuadrado(linha, coluna, tabuleiro)
    if (resultado == 'ok'):
        if (tabuleiro[linha][coluna][1] == 'A' and tabuleiro[linha][coluna][0] == 0):
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


# --------------------------------------------------------------------------------

# ---------------------------------------------------------------------------------------------------
# ------------------------------ MANIPULAÇÃO DO TABULERO (FIM) --------------------------------------
# ---------------------------------------------------------------------------------------------------
# ************

# ************
# ---------------------------------------------------------------------------------------------------
# -------------------------------- IMPLEMENTAÇÃO DE REGRAS (INICIO) ---------------------------------
# ---------------------------------------------------------------------------------------------------

def posicionamento1(i, j, tabuleiro):
    if (tabuleiro[i][j + 1][0] == 2 and
            tabuleiro[i][j - 1][0] != 'B' and tabuleiro[i][j - 1][1] == 'A' and  # leste
            tabuleiro[i - 1][j - 1][0] != 'B' and tabuleiro[i - 1][j - 1][1] == 'A' and  #
            tabuleiro[i - 1][j][0] != 'B' and tabuleiro[i - 1][j][1] == 'A' and  # norte
            tabuleiro[i - 1][j + 1][0] != 'B' and tabuleiro[i - 1][j + 1][1] == 'A' and
            tabuleiro[i - 1][j + 2][0] != 'B' and tabuleiro[i - 1][j + 2][1] == 'A' and
            tabuleiro[i][j + 2][0] != 'B' and tabuleiro[i][j + 2][1] == 'A' and  # oeste
            tabuleiro[i + 1][j - 1][1] == 'I' and tabuleiro[i + 1][j][1] == 'I' and
            tabuleiro[i + 1][j + 1][1] == 'I' and tabuleiro[i + 1][j + 2][1] == 'I'):
        posicao = 'ok'
    else:
        posicao = 'er'
    return posicao


def posicionamento2(i, j, tabuleiro):
    if (tabuleiro[i][j - 1][0] == 2 and
            tabuleiro[i][j - 1][0] != 'B' and tabuleiro[i][j - 1][1] == 'A' and  # leste
            tabuleiro[i - 1][j - 1][0] != 'B' and tabuleiro[i - 1][j - 1][1] == 'A' and
            tabuleiro[i - 1][j][0] != 'B' and tabuleiro[i - 1][j][1] == 'A' and
            tabuleiro[i - 1][j + 1][0] != 'B' and tabuleiro[i - 1][j + 1][1] == 'A' and
            tabuleiro[i - 1][j - 2][0] != 'B' and tabuleiro[i - 1][j - 2][1] == 'A' and
            tabuleiro[i][j - 2][0] != 'B' and tabuleiro[i][j - 2][1] == 'A' and
            tabuleiro[i + 1][j - 1][1] == 'I' and tabuleiro[i + 1][j][1] == 'I' and
            tabuleiro[i + 1][j + 1][1] == 'I' and tabuleiro[i + 1][j + 2][1] == 'I'):
        posicao = 'ok'
    else:
        posicao = 'er'
    return posicao


'''
0000 | x000 | xxxx | 000x | condição 1 - existir quadrado Q1 aberto(A) e com valor 1
0000 | x100 | 0120 | 001x | condição 2 - Q1 ter um vizinho Q2, tambem aberto(A) com valor 2
0120 | x200 | 0000 | 002x | condição 3 - existir 6 vizinhos consecutivos de Q1Q2 aberto(A) e com valor 0 
xxxx | x000 | 0000 | 000x | condição 4 - existir 3 vizinhos consecutivos de Q1Q2 fechado(I)
'''


def regra_1_2(n_linhas, n_colunas, tabuleiro):
    contador = 0
    listaQuadrados_1 = []

    for i in range(n_linhas):
        for j in range(n_colunas):
            contador = contador + 1
            if tabuleiro[i][j][0] == 1:
                listaQuadrados_1.append(contador)

    print(listaQuadrados_1)

    if len(listaQuadrados_1) > 0:
        for q in range(len(listaQuadrados_1)):
            indiceQ = encontrarQuadradoPeloNumero(listaQuadrados_1[q], n_linhas, n_colunas, tabuleiro)
            # print('quadrados com valor 1 -',indiceQ)
            if indiceQ[0] > 0 and indiceQ[0] < (n_linhas - 1) and indiceQ[1] > 0 and indiceQ[1] < (n_colunas - 1):
                # print("xxx--->",tabuleiro[indiceQ[0]][indiceQ[1]])
                # print("xxx--->",tabuleiro[indiceQ[0]][indiceQ[1]+1])
                if posicionamento1(indiceQ[0], indiceQ[1], tabuleiro) == "ok":
                    print("achei!!")
                    tabuleiro[indiceQ[0] + 1][indiceQ[1] + 2][1] = 'F'
                    click(indiceQ[0] + 1, indiceQ[1] - 1, tabuleiro, n_linhas, n_colunas)
                if posicionamento2(indiceQ[0], indiceQ[1], tabuleiro) == "ok":
                    print("achei!!")
                    tabuleiro[indiceQ[0] + 1][indiceQ[1] - 2][1] = 'F'
                    click(indiceQ[0] + 1, indiceQ[1] + 1, tabuleiro, n_linhas, n_colunas)
                    # imprimirTabuleiro(qtdLinhasTabela, tabuleiro)
                # if(tabuleiro[indiceQ[0]][indiceQ[1]+1][0] == 2 and posicionamento2(indiceQ[0],indiceQ[1],tabuleiro)=="ok"):
                # if(tabuleiro[indiceQ[0]][indiceQ[1]+1][0] == 2 and posicionamento3(indiceQ[0],indiceQ[1],tabuleiro)=="ok"):
                # if(tabuleiro[indiceQ[0]][indiceQ[1]+1][0] == 2 and posicionamento4(indiceQ[0],indiceQ[1],tabuleiro)=="ok"):


# ---------------------------------------------------------------------------------------------------
# -------------------------------- IMPLEMENTAÇÃO DE REGRAS (FIM) ------------------------------------
# ---------------------------------------------------------------------------------------------------
# ************

# ************
# ---------------------------------------------------------------------------------------------------
# ---------------------------------- ROTINAS DE RESOLUÇÃO (INICIO) ----------------------------------
# ---------------------------------------------------------------------------------------------------
def forcaBruta(n_linhas, n_colunas, n_bombas):
    vitorias = 0
    derrotas = 0
    jogos = 1

    while vitorias == 0:
        print('Jogo', jogos)
        print('Placar')
        print('Vitorias', vitorias, "x", derrotas, 'Derrotas')
        tabuleiro = Tabuleiro.montarTabuleiroCompleto(qtdLinhasTabela, qtdColunasTabela, qtdBombas)
        Tabuleiro.imprimirTabuleiro(qtdLinhasTabela, tabuleiro)

        for reps in range((n_linhas * n_colunas) - n_bombas):
            lista = listarQuadradosInativos(n_linhas, n_colunas, tabuleiro)
            print(lista)
            numQuadradoSorteado = random.choice(lista)
            quadradoSorteado = encontrarQuadradoPeloNumero(numQuadradoSorteado, n_linhas, n_colunas, tabuleiro)
            print("Clique -", reps, "|Posição -", numQuadradoSorteado, "|Quadrado-", quadradoSorteado)
            status = click(quadradoSorteado[0], quadradoSorteado[1], tabuleiro, n_linhas, n_colunas)
            if status == 'interromper':
                print('Game Over')
                Tabuleiro.imprimirTabuleiro(qtdLinhasTabela, tabuleiro)
                derrotas = derrotas + 1
                break
            if (reps + 1) == ((n_linhas * n_colunas) - n_bombas):
                vitorias = 1
        jogos = jogos + 1

    print('Vitorias', vitorias, "x", derrotas, 'Derrotas')
    Tabuleiro.imprimirTabuleiro(qtdLinhasTabela, tabuleiro)


def simularClickAleatorio(n_linhas, n_colunas, tabuleiro):
    lista = listarQuadradosInativos(n_linhas, n_colunas, tabuleiro)
    print('lista quadrados inativos -', lista)
    valido = ''
    resultado = "continuar"
    numQuadradoSorteado = random.choice(lista)
    quadradoSorteado = encontrarQuadradoPeloNumero(numQuadradoSorteado, n_linhas, n_colunas, tabuleiro)
    if tabuleiro[quadradoSorteado[0]][quadradoSorteado[1]][1] == 'F':
        simularClickAleatorio(n_linhas, n_colunas, tabuleiro)
    else:
        print('quadrado clicado -', quadradoSorteado)
        status = click(quadradoSorteado[0], quadradoSorteado[1], tabuleiro, n_linhas, n_colunas)
        if status == 'interromper':
            resultado = "Game Over"
            print(resultado)
    return resultado


def rotinaRegrasBasicas(n_linhas, n_colunas, n_bombas):
    tabuleiro = Tabuleiro.montarTabuleiroCompleto(qtdLinhasTabela, qtdColunasTabela, qtdBombas)
    Tabuleiro.imprimirTabuleiro(qtdLinhasTabela, tabuleiro)
    resultado = "continuar"
    reps = 0
    while resultado == "continuar" and reps <= ((n_linhas * n_colunas) - n_bombas):
        resultado = simularClickAleatorio(n_linhas, n_colunas, tabuleiro)

        rule12 = RegrasBasicas.regra_1_2(n_linhas, n_colunas, tabuleiro)
        if rule12 != "SO":
            click(rule12[0], rule12[1], tabuleiro, n_linhas, n_colunas)

        rule11 = RegrasBasicas.regra_1_1(n_linhas, n_colunas, tabuleiro)
        if rule12 != "SO":
            click(rule11[0], rule11[1], tabuleiro, n_linhas, n_colunas)
        reps = reps + 1

    Tabuleiro.imprimirTabuleiro(qtdLinhasTabela, tabuleiro)


def testeBasico():
    tabuleiro = Tabuleiro.crie_matriz(qtdLinhasTabela, qtdColunasTabela, 0, 'I')
    print('posição das bombas')
    Tabuleiro.sortearBombas(tabuleiro, qtdLinhasTabela, qtdColunasTabela, qtdBombas)
    Tabuleiro.prencherCamposNum(tabuleiro, qtdLinhasTabela, qtdColunasTabela)
    print('tabuleiro ANTES do click')
    print(tabuleiro)
    click(3, 3, tabuleiro, qtdLinhasTabela, qtdColunasTabela)
    print('tabuleiro DEPOIS do click')
    print(tabuleiro)


def testes(n_linhas, n_colunas):
    tabuleiro = Tabuleiro.montarTabuleiroCompleto(qtdLinhasTabela, qtdColunasTabela, qtdBombas)
    Tabuleiro.imprimirTabuleiro(qtdLinhasTabela, tabuleiro)
    linha = 0
    coluna = 0
    listarQuadradosVizinhos(linha, coluna, n_linhas, n_colunas)


# ---------------------------------------------------------------------------------------------------
# ---------------------------------- ROTINAS DE RESOLUÇÃO (FIM) -----------------------------------------
# ---------------------------------------------------------------------------------------------------
# ************

# ************
# ---------------------------------------------------------------------------------------------------
# ---------------------------------- START ROTINAS (INICIO) -----------------------------------------
# ---------------------------------------------------------------------------------------------------

# forcaBruta(qtdLinhasTabela,qtdColunasTabela,qtdBombas)
rotinaRegrasBasicas(qtdLinhasTabela, qtdColunasTabela, qtdBombas)
# testeBasico()
# testes(qtdLinhasTabela,qtdColunasTabela)

# ---------------------------------------------------------------------------------------------------
# ---------------------------------- START ROTINAS (FIM) --------------------------------------------
# ---------------------------------------------------------------------------------------------------
# ************

# possiveis estados dos quadrados
# I - inativo
# A - ativo
# S - suspeito
# F - flag
