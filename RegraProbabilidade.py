import Tabuleiro

"""
probabilidade basica de resolucao

regra 1 - considerando um quadrado com pelo menos 1 vizinho conhecido
A probabilidade deste quadrado ser bomba é de o valor do seu maior vizinho (v) dividido pela quantidade de vizinhos (8, 5, 3)

v/8 ou v/5 ou v/3

regra 2 - considerando um quadrado sem vizinhos conhecidos
A probabilidade deste quadrado ser bomba é q quantidade de bombas (qt_b) menos a soma dos valores dos quadrados virados (somaQV) dividido pela quantidade quantidade de linhas (ql) vezes a quantidade de colunas (qc) menos a quantidade de quadrados virados qt_qv

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
            contador = contador + 1
            listaQuadardos.update({contador: (i, j)})
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


def somaQuadradosAtivos(n_linhas, n_colunas, tabuleiro):
    soma = 0
    for l in listarQuadradosStatus(n_linhas, n_colunas, tabuleiro):
        if dicionarioQuadradosStatus(l) == 'A':
            soma = soma + listarQuadradosValor(l)
    return soma


def qtdQuadradosAtivos(n_linhas, n_colunas, tabuleiro):
    qtd = 0
    for l in listarQuadradosStatus(n_linhas, n_colunas, tabuleiro):
        if dicionarioQuadradosStatus(l) == 'A':
            qtd = qtd + 1
    return qtd


def listarQuadradosVizinhos(posicao, n_linhas, n_colunas):
    listaVizinhos = []
    if posicao - n_linhas > 0 and dicionarioQuadradosStatus[posicao - n_linhas] == 'A':
        listaVizinhos.append(dicionarioQuadradosValor[posicao - n_linhas])
    if posicao - n_linhas - 1 > 0 and dicionarioQuadradosStatus[posicao - n_linhas - 1] == 'A':
        listaVizinhos.append(dicionarioQuadradosValor[posicao - n_linhas - 1])
    if posicao - n_linhas + 1 > 0 and dicionarioQuadradosStatus[posicao - n_linhas + 1] == 'A':
        listaVizinhos.append(dicionarioQuadradosValor[posicao - n_linhas + 1])
    if posicao - 1 > 0 and dicionarioQuadradosStatus[posicao - 1] == 'A':
        listaVizinhos.append(dicionarioQuadradosValor[posicao - 1])
    if (posicao + n_linhas) < (n_linhas * n_colunas) and dicionarioQuadradosStatus[posicao + n_linhas] == 'A':
        listaVizinhos.append(dicionarioQuadradosValor[posicao + n_linhas])
    if posicao + n_linhas - 1 < n_linhas * n_colunas and dicionarioQuadradosStatus[posicao + n_linhas - 1] == 'A':
        listaVizinhos.append(dicionarioQuadradosValor[posicao + n_linhas - 1])
    if posicao + n_linhas + 1 < n_linhas * n_colunas and dicionarioQuadradosStatus[posicao + n_linhas + 1 == 'A']:
        listaVizinhos.append(dicionarioQuadradosValor[posicao + n_linhas + 1])
    if posicao + 1 < n_linhas * n_colunas and dicionarioQuadradosStatus[posicao + 1] == 'A':
        listaVizinhos.append(dicionarioQuadradosValor[posicao + 1])
    return listaVizinhos

def listarQuadradosProbabilidade(n_linhas, n_colunas, n_bombas, tabuleiro):
    contador = 0
    listaProbabilidades = []
    for i in range(n_linhas):
        for j in range(n_colunas):
            contador = contador + 1
            vizinhos = listarQuadradosVizinhos(contador, n_linhas, n_colunas)
            if dicionarioQuadradosStatus[contador] == "A" and vizinhos != [] :
                v = 0
                qtd_vizinhos = len(vizinhos)
                while v < len(vizinhos):
                    if vizinhos[v] == 'B':
                        vizinhos.pop(v)
                        v = v - 1
                    v = v + 1
                probabilidade = max(vizinhos, key=int)/qtd_vizinhos
                listaProbabilidades.append(probabilidade)
            else:
                somaQA = somaQuadradosAtivos(n_linhas, n_colunas, tabuleiro)
                qtdQA = qtdQuadradosAtivos(n_linhas, n_colunas, tabuleiro)
                probabilidade = (n_bombas - somaQA)/((n_linhas * n_colunas)-qtdQA)
                listaProbabilidades.append(probabilidade)
    return listaProbabilidades


tab = Tabuleiro.montarTabuleiroCompleto(5, 5, 5)
dicionarioQuadradosLocal = listarQuadradosLocal(5, 5, tab)
dicionarioQuadradosValor = listarQuadradosValor(5, 5, tab)
dicionarioQuadradosStatus = listarQuadradosStatus(5, 5, tab)
listarQuadradosProbabilidade(5, 5, 5, tab)
