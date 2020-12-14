import Tabuleiro
import ManipulacaoTabuleiro
import random

"""
probabilidade basica de resolucao

regra 1 - considerando um quadrado com pelo menos 1 vizinho conhecido
A probabilidade deste quadrado ser bomba é de o valor do seu maior vizinho (v) dividido pela quantidade de 
vizinhos (8, 5, 3)

v/8 ou v/5 ou v/3

regra 2 - considerando um quadrado sem vizinhos conhecidos
A probabilidade deste quadrado ser bomba é q quantidade de bombas (qt_b) menos a soma dos valores dos quadrados virados 
(somaQV) dividido pela quantidade quantidade de linhas (ql) vezes a quantidade de colunas (qc) menos a quantidade de 
quadrados virados qt_qv

 qt_b - (somaQV)
-------------------
(qt_l)*(qt_c)-qt_qv
"""


# --------- Função para Listar Quadrados virados --------------
def listarQuadradosLocal(n_linhas, n_colunas, tabuleiro):
    contador = 0
    listaQuadardos = {}
    for i in range(n_linhas):
        for j in range(n_colunas):
            listaQuadardos.update({contador: (i, j)})
            contador = contador + 1
    return listaQuadardos


def listarQuadradosValor(n_linhas, n_colunas, tabuleiro):
    contador = 0
    listaQuadardos = []
    for i in range(n_linhas):
        for j in range(n_colunas):
            contador = contador + 1
            listaQuadardos.append(tabuleiro[i][j][0])
    return listaQuadardos

def listarQuadradosStatus(n_linhas, n_colunas, tabuleiro):
    contador = 0
    listaQuadardos = []
    for i in range(n_linhas):
        for j in range(n_colunas):
            contador = contador + 1
            listaQuadardos.append(tabuleiro[i][j][1])
    return listaQuadardos


def somaQuadradosAtivos(n_linhas, n_colunas, tabuleiro, listaStatus, listaValor):
    soma = 0
    l = 0
    listaSoma = []
    while l < len(listaStatus):
        if listaStatus[l] == 'A' and listaValor[l] !='B':
            soma = soma + listaValor[l]
        l = l + 1
    return soma

def qtdQuadradosVizinhos(n_linhas, n_colunas):
    qtd = 0
    for i in range(n_linhas):
        for j in range(n_colunas):
            if (j - 1) >= 0:
                qtd = qtd + 1
            if (j + 1) <= n_colunas - 1:
                qtd = qtd + 1
            if i - 1 >= 0:
                qtd = qtd + 1
            if i + 1 <= n_linhas - 1:
                qtd = qtd + 1
            if i - 1 >= 0 and (j - 1) >= 0:
                qtd = qtd + 1
            if i + 1 <= n_linhas - 1 and (j + 1) <= n_colunas - 1:
                qtd = qtd + 1
            if i - 1 >= 0 and (j + 1) <= n_colunas - 1:
                qtd = qtd + 1
            if i + 1 <= n_linhas - 1 and (j - 1) >= 0:
                qtd = qtd + 1
    return qtd


def qtdQuadradosAtivos(n_linhas, n_colunas, tabuleiro, listaStatus, listaValor, listaLocal):
    qtd = 0
    l = 0
    while l < len(listaStatus):
        if listaStatus[l] == 'A':
            qtd = qtd + 1
        l = l + 1
    qtd = qtd + qtdQuadradosVizinhos(n_linhas, n_colunas)
    return qtd


def listarQuadradosVizinhos(d, n_linhas, n_colunas, dicionarioQuadradosStatus, dicionarioQuadradosValor, dicionarioQuadradosLocal):
    listaVizinhos = []
    e = d
    if (dicionarioQuadradosLocal[d][1] - 1) >= 0 and dicionarioQuadradosStatus[e - 1] == 'A':
        listaVizinhos.append(dicionarioQuadradosValor[e - 1])

    if (dicionarioQuadradosLocal[d][0] - 1) >= 0 and (dicionarioQuadradosLocal[d][1] - 1) >= 0 and dicionarioQuadradosStatus[e - n_colunas - 1] == 'A':
        listaVizinhos.append(dicionarioQuadradosValor[e - n_colunas - 1])

    if (dicionarioQuadradosLocal[d][0] - 1) >= 0 and dicionarioQuadradosStatus[e - n_colunas] == 'A':
        listaVizinhos.append(dicionarioQuadradosValor[e - n_colunas])

    if (dicionarioQuadradosLocal[d][0] - 1) >= 0 and (dicionarioQuadradosLocal[d][1] + 1) <= (n_colunas - 1) and dicionarioQuadradosStatus[e - n_colunas + 1] == 'A':
        listaVizinhos.append(dicionarioQuadradosValor[e - n_colunas + 1])

    if (dicionarioQuadradosLocal[d][1] + 1) <= (n_colunas - 1) and dicionarioQuadradosStatus[e + 1] == 'A':
        listaVizinhos.append(dicionarioQuadradosValor[e + 1])

    if (dicionarioQuadradosLocal[d][0] + 1) <= (n_linhas - 1) and (dicionarioQuadradosLocal[d][1] + 1) <= (n_colunas - 1) and dicionarioQuadradosStatus[e + n_colunas + 1] == 'A':
        listaVizinhos.append(dicionarioQuadradosValor[e + n_colunas + 1])

    if (dicionarioQuadradosLocal[d][0] + 1) <= (n_linhas - 1) and dicionarioQuadradosStatus[e + n_colunas] == 'A':
        listaVizinhos.append(dicionarioQuadradosValor[e + n_colunas])

    if (dicionarioQuadradosLocal[d][0] + 1) <= (n_linhas - 1) and (dicionarioQuadradosLocal[d][1] - 1) >= 0 and dicionarioQuadradosStatus[e + n_colunas - 1] == 'A':
        listaVizinhos.append(dicionarioQuadradosValor[e + n_colunas - 1])
    return listaVizinhos

def listarQuadradosProbabilidade(n_linhas, n_colunas, n_bombas, tabuleiro):
    contador = 0
    listaProbabilidades = []
    dicionarioQuadradosStatus = listarQuadradosStatus(n_linhas, n_colunas, tabuleiro)
    dicionarioQuadradosValor = listarQuadradosValor(n_linhas, n_colunas, tabuleiro)
    dicionarioQuadradosLocal = listarQuadradosLocal(n_linhas, n_colunas, tabuleiro)
    for i in range(n_linhas):
        for j in range(n_colunas):
            vizinhos = listarQuadradosVizinhos(contador, n_linhas, n_colunas, dicionarioQuadradosStatus, dicionarioQuadradosValor, dicionarioQuadradosLocal)
            if dicionarioQuadradosStatus[contador] == "I" and vizinhos != []:
                v = 0
                qtd_vizinhos = len(vizinhos)
                while v < len(vizinhos):
                    if vizinhos[v] == 'B':
                        vizinhos.pop(v)
                        v = v - 1
                    v = v + 1
                if vizinhos == []:
                    probabilidade = 0.0
                else:
                    probabilidade = round(max(vizinhos, key=int) / qtd_vizinhos, 2)
                listaProbabilidades.append(probabilidade)
            else:
                if dicionarioQuadradosStatus[contador] == 'A':
                    probabilidade = 0.0
                else:
                    somaQA = somaQuadradosAtivos(n_linhas, n_colunas, tabuleiro, dicionarioQuadradosStatus, dicionarioQuadradosValor)
                    qtdQA = qtdQuadradosAtivos(n_linhas, n_colunas, tabuleiro, dicionarioQuadradosStatus, dicionarioQuadradosValor, dicionarioQuadradosLocal)
                    probabilidade = round((n_bombas - somaQA)/((n_linhas * n_colunas)-qtdQA), 2)
                listaProbabilidades.append(probabilidade)
            contador = contador + 1
    return listaProbabilidades



def simularClickAleatorio(n_linhas, n_colunas, tabuleiro):
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


def simularClickProbabilistico(n_linhas, n_colunas, tabuleiro,prob):
    l = 0
    flag = 0
    listaStatus = listarQuadradosStatus(n_linhas, n_colunas, tabuleiro)
    listaLocal = listarQuadradosLocal(n_linhas, n_colunas, tabuleiro)
    while l < len(prob):
        #print(prob)
        if (prob[l] == 0.0 or prob[l] == -0.0) and listaStatus[l] == 'I':
            status = ManipulacaoTabuleiro.click(listaLocal[l][0], listaLocal[l][1], tabuleiro, n_linhas, n_colunas)
            flag = 1
        l = l + 1
    if flag == 0:
        menorNumero = min(numero for numero in prob if numero != 0)
        indiceDoMenorNumero = prob.index(menorNumero)
        if tabuleiro[listaLocal[indiceDoMenorNumero][0]][listaLocal[indiceDoMenorNumero][1]] == 'F':
            simularClickProbabilistico(n_linhas, n_colunas, tabuleiro, prob)
        else:
            status = ManipulacaoTabuleiro.click(listaLocal[indiceDoMenorNumero][0], listaLocal[indiceDoMenorNumero][1], tabuleiro, n_linhas, n_colunas)
    # print("este aqui eh o status ---------------------------------------->", status)
    return status

"""
vitorias = 0
derrotas = 0

while vitorias == 0:
    tab = Tabuleiro.montarTabuleiroCompleto(5, 5, 5)
    Tabuleiro.imprimirTabuleiro(5, tab)
    resultado = simularClickAleatorio(5, 5, tab)
    if resultado == "continuar":
        reps = 1
        while reps != 0:
            probabilidades = []
            Tabuleiro.imprimirTabuleiro(5, tab)
            probabilidades = listarQuadradosProbabilidade(5, 5, 5, tab)
            print(probabilidades)
            resultado = simularClickProbabilistico(5,5,tab, probabilidades)
            print(resultado)
            if resultado != "continuar":
                print("Game Over")
                derrotas = derrotas + 1
            reps = len(ManipulacaoTabuleiro.listarQuadradosInativos(5, 5, tab))
            if reps == 0:
                vitorias = vitorias + 1
    else:
        print("Game Over de Primeira")
        derrotas = derrotas + 1

    print('Vitorias', vitorias, "x", derrotas, 'Derrotas')
print(probabilidades)
Tabuleiro.imprimirTabuleiro(5, tab)
"""
