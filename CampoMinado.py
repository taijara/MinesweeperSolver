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
import ManipulacaoTabuleiro
import Regra_1_1
import Regra_1_2
import Regra_1_2_1
import Regra_1_3_1
import Regra_1_2_2_1

# ------------------------------------------------


# ----- Definindo qtd bombas e tamanho da grid ---
qtdBombas = 2
qtdLinhasTabela = 5
qtdColunasTabela = 5


# --------------------------------------------------

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
            lista = ManipulacaoTabuleiro.listarQuadradosInativos(n_linhas, n_colunas, tabuleiro)
            print(lista)
            numQuadradoSorteado = random.choice(lista)
            quadradoSorteado = ManipulacaoTabuleiro.encontrarQuadradoPeloNumero(numQuadradoSorteado, n_linhas, n_colunas, tabuleiro)
            print("Clique -", reps, "|Posição -", numQuadradoSorteado, "|Quadrado-", quadradoSorteado)
            status = ManipulacaoTabuleiro.click(quadradoSorteado[0], quadradoSorteado[1], tabuleiro, n_linhas, n_colunas)
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
    lista = ManipulacaoTabuleiro.listarQuadradosInativos(n_linhas, n_colunas, tabuleiro)
    print('lista quadrados inativos -', lista)
    valido = ''
    resultado = "continuar"
    numQuadradoSorteado = random.choice(lista)
    quadradoSorteado = ManipulacaoTabuleiro.encontrarQuadradoPeloNumero(numQuadradoSorteado, n_linhas, n_colunas, tabuleiro)
    if tabuleiro[quadradoSorteado[0]][quadradoSorteado[1]][1] == 'F':
        simularClickAleatorio(n_linhas, n_colunas, tabuleiro)
    else:
        print('quadrado clicado -', quadradoSorteado)
        status = ManipulacaoTabuleiro.click(quadradoSorteado[0], quadradoSorteado[1], tabuleiro, n_linhas, n_colunas)
        if status == 'interromper':
            resultado = "Game Over"
            print(resultado)
    return resultado


def rotinaRegrasBasicas(n_linhas, n_colunas, n_bombas):
    vitorias = 0
    derrotas = 0
    jogos = 1

    while vitorias == 0:
        print('Jogo', jogos)
        print('Placar')
        print('Vitorias', vitorias, "x", derrotas, 'Derrotas')
        tabuleiro = Tabuleiro.montarTabuleiroCompleto(qtdLinhasTabela, qtdColunasTabela, qtdBombas)
        Tabuleiro.imprimirTabuleiro(qtdLinhasTabela, tabuleiro)

        resultado = "continuar"
        reps = 1
        while resultado == "continuar" and reps !=0:
            resultado = simularClickAleatorio(n_linhas, n_colunas, tabuleiro)
            if resultado == "continuar":

                rule11 = Regra_1_1.verificarPosicoes(n_linhas, n_colunas, tabuleiro)
                if len(rule11) != 0:
                    r = 0
                    while r <= len(rule11) - 1:
                        ManipulacaoTabuleiro.click(rule11[r][0], rule11[r][1], tabuleiro, n_linhas, n_colunas)
                        r = r + 1

                rule12 = Regra_1_2.verificarPosicoes(n_linhas, n_colunas, tabuleiro)
                if len(rule12) != 0:
                    r = 0
                    while r <= len(rule12)-1:
                        ManipulacaoTabuleiro.click(rule12[r][0], rule12[r][1], tabuleiro, n_linhas, n_colunas)
                        r = r + 1

                rule121 = Regra_1_2_1.verificarPosicoes(n_linhas, n_colunas, tabuleiro)
                if len(rule121) != 0:
                    r = 0
                    while r <= len(rule121) - 1:
                        ManipulacaoTabuleiro.click(rule121[r][0], rule121[r][1], tabuleiro, n_linhas, n_colunas)
                        r = r + 1

                rule131 = Regra_1_3_1.verificarPosicoes(n_linhas, n_colunas, tabuleiro)
                if len(rule131) != 0:
                    r = 0
                    while r <= len(rule131) - 1:
                        ManipulacaoTabuleiro.click(rule131[r][0], rule131[r][1], tabuleiro, n_linhas, n_colunas)
                        r = r + 1

                rule1221 = Regra_1_2_2_1.verificarPosicoes(n_linhas, n_colunas, tabuleiro)
                if len(rule1221) != 0:
                    r = 0
                    while r <= len(rule1221) - 1:
                        ManipulacaoTabuleiro.click(rule1221[r][0], rule1221[r][1], tabuleiro, n_linhas, n_colunas)
                        r = r + 1

                reps = len(ManipulacaoTabuleiro.listarQuadradosInativos(n_linhas, n_colunas, tabuleiro))
                if reps == 0:
                    vitorias = vitorias + 1

            else:
                derrotas = derrotas + 1

    print('Jogo', jogos)
    print('Placar')
    print('Vitorias', vitorias, "x", derrotas, 'Derrotas')
    Tabuleiro.imprimirTabuleiro(qtdLinhasTabela, tabuleiro)


def testeBasico():
    tabuleiro = Tabuleiro.crie_matriz(qtdLinhasTabela, qtdColunasTabela, 0, 'I')
    print('posição das bombas')
    Tabuleiro.sortearBombas(tabuleiro, qtdLinhasTabela, qtdColunasTabela, qtdBombas)
    Tabuleiro.prencherCamposNum(tabuleiro, qtdLinhasTabela, qtdColunasTabela)
    print('tabuleiro ANTES do click')
    print(tabuleiro)
    ManipulacaoTabuleiro.click(3, 3, tabuleiro, qtdLinhasTabela, qtdColunasTabela)
    print('tabuleiro DEPOIS do click')
    print(tabuleiro)


def testes(n_linhas, n_colunas):
    tabuleiro = Tabuleiro.montarTabuleiroCompleto(qtdLinhasTabela, qtdColunasTabela, qtdBombas)
    Tabuleiro.imprimirTabuleiro(qtdLinhasTabela, tabuleiro)
    linha = 0
    coluna = 0
    ManipulacaoTabuleiro.listarQuadradosVizinhos(linha, coluna, n_linhas, n_colunas)


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
