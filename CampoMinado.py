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
import RegraProbabilidade
import Regra_1_1
import Regra_1_2
import Regra_1_2_1
import Regra_1_3_1
import Regra_1_2_2_1
import Regra_1_4_Combo
import Regra_2_5_Combo
import Regra_3_6_Combo
import Regra_1_3_2_Combo
import Regra_1_2_1_Combo
import time
import copy

# ------------------------------------------------


# ----- Definindo qtd bombas e tamanho da grid ---
qtdBombas = 3
qtdLinhasTabela = 9
qtdColunasTabela = 9
tempoExecucao = 0
qtdTabuleiros = 1000
nivel = ''


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
    lista = []
    lista = ManipulacaoTabuleiro.listarQuadradosInativos(n_linhas, n_colunas, tabuleiro)
    # print('lista quadrados inativos -', lista)
    valido = ''
    resultado = "continuar"
    numQuadradoSorteado = random.choice(lista)
    quadradoSorteado = ManipulacaoTabuleiro.encontrarQuadradoPeloNumero(numQuadradoSorteado, n_linhas, n_colunas, tabuleiro)
    if tabuleiro[quadradoSorteado[0]][quadradoSorteado[1]][1] == 'F':
        simularClickAleatorio(n_linhas, n_colunas, tabuleiro)
    else:
        # print('quadrado clicado -', quadradoSorteado)
        status = ManipulacaoTabuleiro.click(quadradoSorteado[0], quadradoSorteado[1], tabuleiro, n_linhas, n_colunas)
        if status == 'interromper':
            resultado = "Game Over"
            # print(resultado)
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



def rotinaRegrasBasicasProbabilidade(n_linhas, n_colunas, n_bombas):
    vitorias = 0
    derrotas = 0
    jogos = 1
    while vitorias == 0:
        print('Jogo', jogos)
        print('Placar')
        print('Vitorias', vitorias, "x", derrotas, 'Derrotas')
        tabuleiro = Tabuleiro.montarTabuleiroCompleto(qtdLinhasTabela, qtdColunasTabela, qtdBombas)
        Tabuleiro.imprimirTabuleiro(qtdLinhasTabela, tabuleiro)

        resultado = simularClickAleatorio(5, 5, tabuleiro)
        reps = 1
        while resultado == "continuar" and reps !=0:
            probabilidades = RegraProbabilidade.listarQuadradosProbabilidade(n_linhas, n_colunas, n_bombas, tabuleiro)
            resultado = RegraProbabilidade.simularClickProbabilistico(n_linhas, n_colunas, tabuleiro, probabilidades)
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

def forcaBrutaLog(n_linhas, n_colunas, n_bombas):
    vitorias = 0
    derrotas = 0
    jogos = 1
    mediaAcertos = 0.00
    end_time = time.time() + tempoExecucao
    while time.time() < end_time:
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
                mediaAcertos = mediaAcertos + (reps / ((n_linhas * n_colunas) - n_bombas))
                break
            if (reps + 1) == ((n_linhas * n_colunas) - n_bombas):
                vitorias = 1
                mediaAcertos = mediaAcertos + 1
        jogos = jogos + 1

    print('Vitorias', vitorias, "x", derrotas, 'Derrotas')
    Tabuleiro.imprimirTabuleiro(qtdLinhasTabela, tabuleiro)
    tempo = 'Tempo de Execucao: ' + str(tempoExecucao) + ' segundos\n'
    rodadas = 'Rodadas: ' + str((vitorias + derrotas)) + '\n'
    tempoMedioRodada = 'Tempo Medio por Rodada: ' + str(
        round(tempoExecucao / (vitorias + derrotas), 4)) + ' milisegundos\n'
    qtdVitorias = 'Quantidade de Vitorias: ' + str(vitorias) + '\n'
    qtdDerrotas = 'Quantidade de Derrotas: ' + str(derrotas) + '\n'
    acertosMedios = 'Media de Acertos por Rodadas:' + str(
        round((mediaAcertos / (vitorias + derrotas)) * 100, 2)) + '%\n'
    return tempo + rodadas + tempoMedioRodada + qtdVitorias + qtdDerrotas + acertosMedios


def rotinaRegrasBasicasLog(n_linhas, n_colunas, n_bombas):
    vitorias = 0
    derrotas = 0
    jogos = 1
    mediaAcertos = 0.00
    end_time = time.time() + tempoExecucao
    while time.time() < end_time:
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

                parada = True
                while parada:
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

                    if len(rule11) == 0 and len(rule12) == 0 and len(rule131) == 0 and len(rule121) == 0 and len(rule1221) == 0:
                        parada = False

                reps = len(ManipulacaoTabuleiro.listarQuadradosInativos(n_linhas, n_colunas, tabuleiro))
                if reps == 0:
                    vitorias = vitorias + 1
                    mediaAcertos = mediaAcertos + 1

            else:
                derrotas = derrotas + 1
                mediaAcertos = mediaAcertos + (
                            ((n_linhas * n_colunas) - n_bombas - reps) / ((n_linhas * n_colunas) - n_bombas))

    print('Jogo', jogos)
    print('Placar')
    print('Vitorias', vitorias, "x", derrotas, 'Derrotas')
    Tabuleiro.imprimirTabuleiro(qtdLinhasTabela, tabuleiro)
    tempo = 'Tempo de Execucao: ' + str(tempoExecucao) + ' segundos\n'
    rodadas = 'Rodadas: ' + str((vitorias + derrotas)) + '\n'
    tempoMedioRodada = 'Tempo Medio por Rodada: ' + str(
        round(tempoExecucao / (vitorias + derrotas), 4)) + ' milisegundos\n'
    qtdVitorias = 'Quantidade de Vitorias: ' + str(vitorias) + '\n'
    qtdDerrotas = 'Quantidade de Derrotas: ' + str(derrotas) + '\n'
    acertosMedios = 'Media de Acertos por Rodadas:' + str(
        round((mediaAcertos / (vitorias + derrotas)) * 100, 2)) + '%\n'
    return tempo + rodadas + tempoMedioRodada + qtdVitorias + qtdDerrotas + acertosMedios



def rotinaRegrasBasicasProbabilidadeLog(n_linhas, n_colunas, n_bombas):
    vitorias = 0
    derrotas = 0
    jogos = 1
    mediaAcertos = 0.00
    end_time = time.time() + tempoExecucao
    while time.time() < end_time:
        print('Jogo', jogos)
        print('Placar')
        print('Vitorias', vitorias, "x", derrotas, 'Derrotas')
        tabuleiro = Tabuleiro.montarTabuleiroCompleto(qtdLinhasTabela, qtdColunasTabela, qtdBombas)
        Tabuleiro.imprimirTabuleiro(qtdLinhasTabela, tabuleiro)

        resultado = simularClickAleatorio(5, 5, tabuleiro)
        reps = 1
        while resultado == "continuar" and reps !=0:
            probabilidades = RegraProbabilidade.listarQuadradosProbabilidade(n_linhas, n_colunas, n_bombas, tabuleiro)
            resultado = RegraProbabilidade.simularClickProbabilistico(n_linhas, n_colunas, tabuleiro, probabilidades)
            if resultado == "continuar":

                parada = True
                while parada:
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

                    if len(rule11) == 0 and len(rule12) == 0 and len(rule131) == 0 and len(rule121) == 0 and len(
                            rule1221) == 0:
                        parada = False

                reps = len(ManipulacaoTabuleiro.listarQuadradosInativos(n_linhas, n_colunas, tabuleiro))
                if reps == 0:
                    vitorias = vitorias + 1
                    mediaAcertos = mediaAcertos + 1
            else:
                derrotas = derrotas + 1
                mediaAcertos = mediaAcertos + (((n_linhas * n_colunas) - n_bombas-reps) / ((n_linhas * n_colunas) - n_bombas))

    print('Jogo', jogos)
    print('Placar')
    print('Vitorias', vitorias, "x", derrotas, 'Derrotas')
    Tabuleiro.imprimirTabuleiro(qtdLinhasTabela, tabuleiro)

    tempo = 'Tempo de Execucao: ' + str(tempoExecucao) + ' segundos\n'
    rodadas = 'Rodadas: ' + str((vitorias+derrotas)) + '\n'
    tempoMedioRodada = 'Tempo Medio por Rodada: ' + str(round(tempoExecucao/(vitorias+derrotas), 4)) + ' milisegundos\n'
    qtdVitorias = 'Quantidade de Vitorias: ' + str(vitorias) + '\n'
    qtdDerrotas = 'Quantidade de Derrotas: ' + str(derrotas) + '\n'
    acertosMedios = 'Media de Acertos por Rodadas:' + str(round((mediaAcertos/(vitorias+derrotas)) * 100, 2)) + '%\n'
    return tempo+rodadas+tempoMedioRodada+qtdVitorias+qtdDerrotas+acertosMedios


def forcaBrutaLogTab(n_linhas, n_colunas, n_bombas, tabuleiros1):
    tempoIni = time.time()
    vitorias = 0
    derrotas = 0
    jogos = 1
    mediaAcertos = 0.00
    i = 0
    while i < len(tabuleiros1):
        print('Jogo', jogos)
        print('Placar')
        print('Vitorias', vitorias, "x", derrotas, 'Derrotas')
        tabuleiro = tabuleiros1[i]
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
                mediaAcertos = mediaAcertos + (reps / ((n_linhas * n_colunas) - n_bombas))
                break
            if (reps + 1) == ((n_linhas * n_colunas) - n_bombas):
                vitorias = 1
                mediaAcertos = mediaAcertos + 1
        jogos = jogos + 1
        i = i + 1

    tempoFim = time.time()

    print('Vitorias', vitorias, "x", derrotas, 'Derrotas')
    Tabuleiro.imprimirTabuleiro(qtdLinhasTabela, tabuleiro)
    tempo = 'Tempo de Execucao: ' + str(round(tempoFim-tempoIni, 4)) + ' segundos\n'
    rodadas = 'Rodadas: ' + str((vitorias + derrotas)) + '\n'
    tempoMedioRodada = 'Tempo Medio por Rodada: ' + str(
        round((tempoFim-tempoIni) / (vitorias + derrotas), 4)) + ' milisegundos\n'
    qtdVitorias = 'Quantidade de Vitorias: ' + str(vitorias) + '\n'
    qtdDerrotas = 'Quantidade de Derrotas: ' + str(derrotas) + '\n'
    acertosMedios = 'Media de Acertos por Rodadas:' + str(
        round((mediaAcertos / (vitorias + derrotas)) * 100, 2)) + '%\n'
    return tempo + rodadas + tempoMedioRodada + qtdVitorias + qtdDerrotas + acertosMedios


def rotinaRegrasBasicasLogTab(n_linhas, n_colunas, n_bombas, tabuleiros2):
    tempoIni = time.time()
    vitorias = 0
    derrotas = 0
    jogos = 1
    mediaAcertos = 0.00

    i = 0
    while i < len(tabuleiros2):
        print('-------------------- INICIO DO JOGO --------------------')
        print('Jogo', jogos)
        print('Placar')
        print('Vitorias', vitorias, "x", derrotas, 'Derrotas')
        tabuleiro = tabuleiros2[i]
        Tabuleiro.imprimirTabuleiro(qtdLinhasTabela, tabuleiro)

        resultado = "continuar"
        reps = 0
        while resultado == "continuar" and reps != qtdBombas:
            resultado = simularClickAleatorio(n_linhas, n_colunas, tabuleiro)
            if resultado == "continuar":

                parada = True
                while parada:
                    rule11 = Regra_1_1.verificarPosicoes(n_linhas, n_colunas, tabuleiro)
                    if len(rule11) != 0:
                        r = 0
                        while r <= len(rule11) - 1:
                            ManipulacaoTabuleiro.click(rule11[r][0], rule11[r][1], tabuleiro, n_linhas, n_colunas)
                            Tabuleiro.imprimirTabuleiro(qtdLinhasTabela, tabuleiro)
                            r = r + 1

                    rule12 = Regra_1_2.verificarPosicoes(n_linhas, n_colunas, tabuleiro)
                    if len(rule12) != 0:
                        r = 0
                        while r <= len(rule12)-1:
                            ManipulacaoTabuleiro.click(rule12[r][0], rule12[r][1], tabuleiro, n_linhas, n_colunas)
                            Tabuleiro.imprimirTabuleiro(qtdLinhasTabela, tabuleiro)
                            r = r + 1

                    rule121 = Regra_1_2_1.verificarPosicoes(n_linhas, n_colunas, tabuleiro)
                    if len(rule121) != 0:
                        r = 0
                        while r <= len(rule121) - 1:
                            ManipulacaoTabuleiro.click(rule121[r][0], rule121[r][1], tabuleiro, n_linhas, n_colunas)
                            Tabuleiro.imprimirTabuleiro(qtdLinhasTabela, tabuleiro)
                            r = r + 1

                    rule131 = Regra_1_3_1.verificarPosicoes(n_linhas, n_colunas, tabuleiro)
                    if len(rule131) != 0:
                        r = 0
                        while r <= len(rule131) - 1:
                            ManipulacaoTabuleiro.click(rule131[r][0], rule131[r][1], tabuleiro, n_linhas, n_colunas)
                            Tabuleiro.imprimirTabuleiro(qtdLinhasTabela, tabuleiro)
                            r = r + 1

                    rule1221 = Regra_1_2_2_1.verificarPosicoes(n_linhas, n_colunas, tabuleiro)
                    if len(rule1221) != 0:
                        r = 0
                        while r <= len(rule1221) - 1:
                            ManipulacaoTabuleiro.click(rule1221[r][0], rule1221[r][1], tabuleiro, n_linhas, n_colunas)
                            Tabuleiro.imprimirTabuleiro(qtdLinhasTabela, tabuleiro)
                            r = r + 1

                    rule14Combo = Regra_1_4_Combo.verificarPosicoes(n_linhas, n_colunas, tabuleiro)
                    if len(rule14Combo) != 0:
                        r = 0
                        while r <= len(rule14Combo) - 1:
                            ManipulacaoTabuleiro.click(rule14Combo[r][0], rule14Combo[r][1], tabuleiro, n_linhas,
                                                       n_colunas)
                            Tabuleiro.imprimirTabuleiro(qtdLinhasTabela, tabuleiro)
                            r = r + 1

                    rule25Combo = Regra_2_5_Combo.verificarPosicoes(n_linhas, n_colunas, tabuleiro)
                    if len(rule25Combo) != 0:
                        r = 0
                        while r <= len(rule25Combo) - 1:
                            ManipulacaoTabuleiro.click(rule25Combo[r][0], rule25Combo[r][1], tabuleiro, n_linhas,
                                                       n_colunas)
                            Tabuleiro.imprimirTabuleiro(qtdLinhasTabela, tabuleiro)
                            r = r + 1

                    rule36Combo = Regra_3_6_Combo.verificarPosicoes(n_linhas, n_colunas, tabuleiro)
                    if len(rule36Combo) != 0:
                        r = 0
                        while r <= len(rule36Combo) - 1:
                            ManipulacaoTabuleiro.click(rule36Combo[r][0], rule36Combo[r][1], tabuleiro, n_linhas,
                                                       n_colunas)
                            Tabuleiro.imprimirTabuleiro(qtdLinhasTabela, tabuleiro)
                            r = r + 1

                    rule121Combo = Regra_1_2_1_Combo.verificarPosicoes(n_linhas, n_colunas, tabuleiro)
                    if len(rule121Combo) != 0:
                        r = 0
                        while r <= len(rule121Combo) - 1:
                            ManipulacaoTabuleiro.click(rule121Combo[r][0], rule121Combo[r][1], tabuleiro, n_linhas,
                                                       n_colunas)
                            Tabuleiro.imprimirTabuleiro(qtdLinhasTabela, tabuleiro)
                            r = r + 1

                    rule132Combo = Regra_1_3_2_Combo.verificarPosicoes(n_linhas, n_colunas, tabuleiro)
                    if len(rule132Combo) != 0:
                        r = 0
                        while r <= len(rule132Combo) - 1:
                            ManipulacaoTabuleiro.click(rule132Combo[r][0], rule132Combo[r][1], tabuleiro, n_linhas,
                                                       n_colunas)
                            Tabuleiro.imprimirTabuleiro(qtdLinhasTabela, tabuleiro)
                            r = r + 1

                    if len(rule11) == 0 and len(rule12) == 0 and len(rule131) == 0 and len(rule121) == 0 and len(rule1221) == 0 and len(rule14Combo) == 0 and len(rule25Combo) == 0 and len(rule36Combo) == 0 and len(rule121Combo) == 0 and len(rule132Combo) == 0:
                        parada = False

                reps = len(ManipulacaoTabuleiro.listarQuadradosInativos(n_linhas, n_colunas, tabuleiro))
                bombasMacardas = ManipulacaoTabuleiro.contarBombasMarcadas(n_linhas, n_colunas, tabuleiro)
                if reps == qtdBombas or bombasMacardas == qtdBombas:
                    vitorias = vitorias + 1
                    mediaAcertos = mediaAcertos + 1
                    break
            else:
                derrotas = derrotas + 1
                mediaAcertos = mediaAcertos + (
                            ((n_linhas * n_colunas) - reps) / ((n_linhas * n_colunas)))
        jogos = jogos + 1
        i = i + 1

        print('-------------------- FIM DO JOGO --------------------')

    print('-------------------- RESUMO DOS JOGOS --------------------')
    tempoFim = time.time()
    print('Jogo', jogos)
    print('Placar')
    print('Vitorias', vitorias, "x", derrotas, 'Derrotas')
    Tabuleiro.imprimirTabuleiro(qtdLinhasTabela, tabuleiro)
    tempo = 'Tempo de Execucao: ' + str(round(tempoFim-tempoIni, 4)) + ' segundos\n'
    rodadas = 'Rodadas: ' + str((vitorias + derrotas)) + '\n'
    tempoMedioRodada = 'Tempo Medio por Rodada: ' + str(
        round((tempoFim-tempoIni) / (vitorias + derrotas), 4)) + ' milisegundos\n'
    qtdVitorias = 'Quantidade de Vitorias: ' + str(vitorias) + '\n'
    qtdDerrotas = 'Quantidade de Derrotas: ' + str(derrotas) + '\n'
    acertosMedios = 'Media de Acertos por Rodadas:' + str(
        round((mediaAcertos / (vitorias + derrotas)) * 100, 2)) + '%\n'
    return tempo + rodadas + tempoMedioRodada + qtdVitorias + qtdDerrotas + acertosMedios



def rotinaRegrasBasicasProbabilidadeLogTab(n_linhas, n_colunas, n_bombas, tabuleiros3):
    tempoIni = time.time()
    vitorias = 0
    derrotas = 0
    jogos = 1
    mediaAcertos = 0.00
    # print(tabuleiros3)
    i = 0
    while i < len(tabuleiros3):
        print('-------------------- INICIO DO JOGO --------------------')
        print('Jogo', jogos)
        print('Placar')
        print('Vitorias', vitorias, "x", derrotas, 'Derrotas')
        #print(i)
        tabuleiro = tabuleiros3[i]
        Tabuleiro.imprimirTabuleiro(qtdLinhasTabela, tabuleiro)

        resultado = "continuar"
        reps = 0
        while resultado == "continuar" and reps != qtdBombas:
            if reps == 1:
                resultado = simularClickAleatorio(n_linhas, n_colunas, tabuleiro)
                Tabuleiro.imprimirTabuleiro(qtdLinhasTabela, tabuleiro)
            else:
                probabilidades = RegraProbabilidade.listarQuadradosProbabilidade(n_linhas, n_colunas, n_bombas, tabuleiro)
                resultado = RegraProbabilidade.simularClickProbabilistico(n_linhas, n_colunas, tabuleiro, probabilidades)
                Tabuleiro.imprimirTabuleiro(qtdLinhasTabela, tabuleiro)

            if resultado == "continuar":

                parada = True
                while parada:
                    rule11 = Regra_1_1.verificarPosicoes(n_linhas, n_colunas, tabuleiro)
                    if len(rule11) != 0:
                        r = 0
                        while r <= len(rule11) - 1:
                            ManipulacaoTabuleiro.click(rule11[r][0], rule11[r][1], tabuleiro, n_linhas, n_colunas)
                            Tabuleiro.imprimirTabuleiro(qtdLinhasTabela, tabuleiro)
                            r = r + 1

                    rule12 = Regra_1_2.verificarPosicoes(n_linhas, n_colunas, tabuleiro)
                    if len(rule12) != 0:
                        r = 0
                        while r <= len(rule12)-1:
                            ManipulacaoTabuleiro.click(rule12[r][0], rule12[r][1], tabuleiro, n_linhas, n_colunas)
                            Tabuleiro.imprimirTabuleiro(qtdLinhasTabela, tabuleiro)
                            r = r + 1

                    rule121 = Regra_1_2_1.verificarPosicoes(n_linhas, n_colunas, tabuleiro)
                    if len(rule121) != 0:
                        r = 0
                        while r <= len(rule121) - 1:
                            ManipulacaoTabuleiro.click(rule121[r][0], rule121[r][1], tabuleiro, n_linhas, n_colunas)
                            Tabuleiro.imprimirTabuleiro(qtdLinhasTabela, tabuleiro)
                            r = r + 1

                    rule131 = Regra_1_3_1.verificarPosicoes(n_linhas, n_colunas, tabuleiro)
                    if len(rule131) != 0:
                        r = 0
                        while r <= len(rule131) - 1:
                            ManipulacaoTabuleiro.click(rule131[r][0], rule131[r][1], tabuleiro, n_linhas, n_colunas)
                            Tabuleiro.imprimirTabuleiro(qtdLinhasTabela, tabuleiro)
                            r = r + 1

                    rule1221 = Regra_1_2_2_1.verificarPosicoes(n_linhas, n_colunas, tabuleiro)
                    if len(rule1221) != 0:
                        r = 0
                        while r <= len(rule1221) - 1:
                            ManipulacaoTabuleiro.click(rule1221[r][0], rule1221[r][1], tabuleiro, n_linhas, n_colunas)
                            Tabuleiro.imprimirTabuleiro(qtdLinhasTabela, tabuleiro)
                            r = r + 1

                    rule14Combo = Regra_1_4_Combo.verificarPosicoes(n_linhas, n_colunas, tabuleiro)
                    if len(rule14Combo) != 0:
                        r = 0
                        while r <= len(rule14Combo) - 1:
                            ManipulacaoTabuleiro.click(rule14Combo[r][0], rule14Combo[r][1], tabuleiro, n_linhas, n_colunas)
                            Tabuleiro.imprimirTabuleiro(qtdLinhasTabela, tabuleiro)
                            r = r + 1

                    rule25Combo = Regra_2_5_Combo.verificarPosicoes(n_linhas, n_colunas, tabuleiro)
                    if len(rule25Combo) != 0:
                        r = 0
                        while r <= len(rule25Combo) - 1:
                            ManipulacaoTabuleiro.click(rule25Combo[r][0], rule25Combo[r][1], tabuleiro, n_linhas, n_colunas)
                            Tabuleiro.imprimirTabuleiro(qtdLinhasTabela, tabuleiro)
                            r = r + 1

                    rule36Combo = Regra_3_6_Combo.verificarPosicoes(n_linhas, n_colunas, tabuleiro)
                    if len(rule36Combo) != 0:
                        r = 0
                        while r <= len(rule36Combo) - 1:
                            ManipulacaoTabuleiro.click(rule36Combo[r][0], rule36Combo[r][1], tabuleiro, n_linhas, n_colunas)
                            Tabuleiro.imprimirTabuleiro(qtdLinhasTabela, tabuleiro)
                            r = r + 1

                    rule121Combo = Regra_1_2_1_Combo.verificarPosicoes(n_linhas, n_colunas, tabuleiro)
                    if len(rule121Combo) != 0:
                        r = 0
                        while r <= len(rule121Combo) - 1:
                            ManipulacaoTabuleiro.click(rule121Combo[r][0], rule121Combo[r][1], tabuleiro, n_linhas, n_colunas)
                            Tabuleiro.imprimirTabuleiro(qtdLinhasTabela, tabuleiro)
                            r = r + 1

                    rule132Combo = Regra_1_3_2_Combo.verificarPosicoes(n_linhas, n_colunas, tabuleiro)
                    if len(rule132Combo) != 0:
                        r = 0
                        while r <= len(rule132Combo) - 1:
                            ManipulacaoTabuleiro.click(rule132Combo[r][0], rule132Combo[r][1], tabuleiro, n_linhas, n_colunas)
                            Tabuleiro.imprimirTabuleiro(qtdLinhasTabela, tabuleiro)
                            r = r + 1


                    if len(rule11) == 0 and len(rule12) == 0 and len(rule131) == 0 and len(rule121) == 0 and len(
                            rule1221) == 0 and len(rule14Combo) == 0 and len(rule25Combo) == 0 and len(rule36Combo) == 0 and len(rule121Combo) == 0 and len(rule132Combo) == 0:
                        parada = False

                reps = len(ManipulacaoTabuleiro.listarQuadradosInativos(n_linhas, n_colunas, tabuleiro))
                bombasMacardas = ManipulacaoTabuleiro.contarBombasMarcadas(n_linhas, n_colunas, tabuleiro)
                if reps == qtdBombas or bombasMacardas == qtdBombas:
                    vitorias = vitorias + 1
                    mediaAcertos = mediaAcertos + 1
                    break
            else:
                derrotas = derrotas + 1
                mediaAcertos = mediaAcertos + (((n_linhas * n_colunas) -reps) / ((n_linhas * n_colunas)))

            Tabuleiro.imprimirTabuleiro(qtdLinhasTabela, tabuleiro)
        jogos = jogos + 1
        i = i + 1

        print('-------------------- FIM DO JOGO --------------------')

    tempoFim = time.time()
    print('-------------------- RESUMO DOS JOGOS --------------------')
    print('Jogos:', jogos-1)
    print('Placar')
    print('Vitorias', vitorias, "x", derrotas, 'Derrotas')

    tempo = 'Tempo de Execucao: ' + str(round(tempoFim-tempoIni, 4)) + ' segundos\n'
    rodadas = 'Rodadas: ' + str((vitorias+derrotas)) + '\n'
    tempoMedioRodada = 'Tempo Medio por Rodada: ' + str(round((tempoFim-tempoIni)/(vitorias+derrotas), 4)) + ' milisegundos\n'
    qtdVitorias = 'Quantidade de Vitorias: ' + str(vitorias) + '\n'
    qtdDerrotas = 'Quantidade de Derrotas: ' + str(derrotas) + '\n'
    acertosMedios = 'Media de Acertos por Rodadas:' + str(round((mediaAcertos/(vitorias+derrotas)) * 100, 2)) + '%\n'
    return tempo+rodadas+tempoMedioRodada+qtdVitorias+qtdDerrotas+acertosMedios


def testeTabuleirosIguais():
    if qtdLinhasTabela <= 9 and qtdColunasTabela <= 9 and qtdBombas <= 10:
        nivel = 'Iniciante'
    if qtdLinhasTabela <= 16 and qtdColunasTabela <= 16 and qtdBombas <= 40:
        nivel = 'Intermediario'
    if qtdLinhasTabela <= 30 and qtdColunasTabela <= 16 and qtdBombas <= 99:
        nivel = 'Avancado'

    tabuleiros = []
    tabuleiros1 = []
    tabuleiros2 = []
    tabuleiros3 = []
    i = 0
    while i < qtdTabuleiros:
        tabuleiros.append(Tabuleiro.montarTabuleiroCompleto(qtdLinhasTabela, qtdColunasTabela, qtdBombas))
        i = i + 1

    tabuleiros1 = copy.deepcopy(tabuleiros)
    tabuleiros2 = copy.deepcopy(tabuleiros)
    tabuleiros3 = copy.deepcopy(tabuleiros)


    resutadoForcaBruta = forcaBrutaLogTab(qtdLinhasTabela, qtdColunasTabela, qtdBombas, tabuleiros1)
    resultadoRegrasBasicasForcaBruta = rotinaRegrasBasicasLogTab(qtdLinhasTabela, qtdColunasTabela, qtdBombas, tabuleiros2)
    resultadoRegrasBasicasProbabilidade = rotinaRegrasBasicasProbabilidadeLogTab(qtdLinhasTabela, qtdColunasTabela,
                                                                                 qtdBombas, tabuleiros3)

    infosGerais = 'Tabuleiro: ' + str(qtdLinhasTabela) + ' x ' + str(qtdColunasTabela) + '\nNumero de Bombas ' + str(qtdBombas)
    arquivo = open('LogResultados.txt', 'w', encoding="cp1252")
    arquivo.write(infosGerais)
    arquivo.write('\n\n')
    arquivo.write('Resultado Forca Bruta \n')
    arquivo.write(resutadoForcaBruta)
    arquivo.write('\n')
    arquivo.write('Resultado Regras Basicas + Forca Bruta \n')
    arquivo.write(resultadoRegrasBasicasForcaBruta)
    arquivo.write('\n')
    arquivo.write('Resultado Regras Basicas + Probabilidade nos clicks \n')
    arquivo.write(resultadoRegrasBasicasProbabilidade)
    arquivo.close()

def testeTabuleirosDiferentes():
    if qtdLinhasTabela <= 9 and qtdColunasTabela <= 9 and qtdBombas <= 10:
        nivel = 'Iniciante'
    if qtdLinhasTabela <= 16 and qtdColunasTabela <= 16 and qtdBombas <= 40:
        nivel = 'Intermediario'
    if qtdLinhasTabela <= 30 and qtdColunasTabela <= 16 and qtdBombas <= 99:
        nivel = 'Avancado'

    tabuleiros1 = []
    tabuleiros2 = []
    tabuleiros3 = []
    i = 0
    while i < qtdTabuleiros:
        tabuleiros1.append(Tabuleiro.montarTabuleiroCompleto(qtdLinhasTabela, qtdColunasTabela, qtdBombas))
        i = i + 1
    i = 0
    while i < qtdTabuleiros:
        tabuleiros2.append(Tabuleiro.montarTabuleiroCompleto(qtdLinhasTabela, qtdColunasTabela, qtdBombas))
        i = i + 1
    i = 0
    while i < qtdTabuleiros:
        tabuleiros3.append(Tabuleiro.montarTabuleiroCompleto(qtdLinhasTabela, qtdColunasTabela, qtdBombas))
        i = i + 1

    resutadoForcaBruta = forcaBrutaLogTab(qtdLinhasTabela, qtdColunasTabela, qtdBombas, tabuleiros1)
    resultadoRegrasBasicasForcaBruta = rotinaRegrasBasicasLogTab(qtdLinhasTabela, qtdColunasTabela, qtdBombas, tabuleiros2)
    resultadoRegrasBasicasProbabilidade = rotinaRegrasBasicasProbabilidadeLogTab(qtdLinhasTabela, qtdColunasTabela,
                                                                                 qtdBombas, tabuleiros3)

    infosGerais = 'Tabuleiro: ' + str(qtdLinhasTabela) + ' x ' + str(qtdColunasTabela) + '\nNumero de Bombas ' + str(qtdBombas)
    arquivo = open('LogResultados.txt', 'w', encoding="cp1252")
    arquivo.write(infosGerais)
    arquivo.write('\n\n')
    arquivo.write('Resultado Forca Bruta \n')
    arquivo.write(resutadoForcaBruta)
    arquivo.write('\n')
    arquivo.write('Resultado Regras Basicas + Forca Bruta \n')
    arquivo.write(resultadoRegrasBasicasForcaBruta)
    arquivo.write('\n')
    arquivo.write('Resultado Regras Basicas + Probabilidade nos clicks \n')
    arquivo.write(resultadoRegrasBasicasProbabilidade)
    arquivo.close()

# ---------------------------------------------------------------------------------------------------
# ---------------------------------- ROTINAS DE RESOLUÇÃO (FIM) -----------------------------------------
# ---------------------------------------------------------------------------------------------------
# ************

# ************
# ---------------------------------------------------------------------------------------------------
# ---------------------------------- START ROTINAS (INICIO) -----------------------------------------
# ---------------------------------------------------------------------------------------------------

#forcaBruta(qtdLinhasTabela,qtdColunasTabela,qtdBombas)
#rotinaRegrasBasicas(qtdLinhasTabela, qtdColunasTabela, qtdBombas)
#rotinaRegrasBasicasProbabilidade(qtdLinhasTabela, qtdColunasTabela, qtdBombas)
#forcaBrutaLog(qtdLinhasTabela,qtdColunasTabela,qtdBombas)
#rotinaRegrasBasicasLog(qtdLinhasTabela, qtdColunasTabela, qtdBombas)
#rotinaRegrasBasicasProbabilidadeLog(qtdLinhasTabela, qtdColunasTabela, qtdBombas)
testeTabuleirosIguais()
#testeTabuleirosDiferentes()


# ---------------------------------------------------------------------------------------------------
# ---------------------------------- START ROTINAS (FIM) --------------------------------------------
# ---------------------------------------------------------------------------------------------------
# ************

# possiveis estados dos quadrados
# I - inativo
# A - ativo
# S - suspeito
# F - flag
