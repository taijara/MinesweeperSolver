'''
Universidade Federal da Bahia
Mestrado em Ciencia da Computação
Disciplina: Algortimos e Grafos
Versão 2.3
Controle Versão: Correção da função de click
'''

#----------------- Imports ----------------------
import random
import os
#------------------------------------------------


#----- Definindo qtd bombas e tamanho da grid ---
qtdBombas = 5
qtdLinhasTabela = 6
qtdColunasTabela = 6
#--------------------------------------------------

#************
#---------------------------------------------------------------------------------------------------
#--------------------------- MONTAGEM DO TABULERO (INICIO) -----------------------------------------
#---------------------------------------------------------------------------------------------------

#--------- Função Para Criar Matriz --------------
def crie_matriz(n_linhas, n_colunas, valor, status):
    '''
    Cria e retorna uma matriz com n_linhas x n_colunas
    em que cada elemento é iniciado com o valor passado por parametro.
    '''
            
    matriz = [] # lista vazia
    for i in range(n_linhas):
        # cria a linha i
        linha = [] # lista vazia
        for j in range(n_colunas):
            linha.append([valor,status])
            
        # coloque linha na matriz
        matriz.append(linha)
            
    return matriz

#--------------------------------------------------

#--------- Função Para Sortear bombas na Matriz --------------
def sortearBombas(A, n_linhas, n_colunas, qtdBombas):
    bombas = random.sample(range(0, (n_linhas*n_colunas-1)), qtdBombas)
    valor = 0
    print("Lista das Bombas - " ,bombas)
    for i in range(n_linhas):
        for j in range(n_colunas):
            if(valor in bombas):
                A[i][j][0] = 'B'
            valor = valor + 1
#-------------------------------------------------------------


#--------- Função Para Preencher campos que não são bombas --------------
def prencherCamposNum(A, n_linhas, n_colunas):
    for i in range(n_linhas):
        contador = 0
        for j in range(n_colunas):
            if(A[i][j][0] == 0):
                if(0<=(i-1)<n_linhas and 0<=(j-1)<n_colunas and A[i-1][j-1][0] == 'B'):
                    contador = contador + 1
                if(0<=(i-1)<n_linhas and 0<=(j)<n_colunas and A[i-1][j][0] == 'B'):
                    contador = contador + 1
                if(0<=(i-1)<n_linhas and 0<=(j+1)<n_colunas and A[i-1][j+1][0] == 'B'):
                    contador = contador + 1
                if(0<=(i)<n_linhas and 0<=(j-1)<n_colunas and A[i][j-1][0] == 'B'):
                    contador = contador + 1
                if(0<=(i)<n_linhas and 0<=(j+1)<n_colunas and A[i][j+1][0] == 'B'):
                    contador = contador + 1
                if(0<=(i+1)<n_linhas and 0<=(j-1)<n_colunas and A[i+1][j-1][0] == 'B'):
                    contador = contador + 1
                if(0<=(i+1)<n_linhas and 0<=(j)<n_colunas and A[i+1][j][0] == 'B'):
                    contador = contador + 1
                if(0<=(i+1)<n_linhas and 0<=(j+1)<n_colunas and A[i+1][j+1][0] == 'B'):
                    contador = contador + 1
                A[i][j][0] = contador
                contador = 0
#------------------------------------------------------------------------

#--------- Função Montar Tabuleiro Completo --------------
def montarTabuleiroCompleto():
    tabuleiro = crie_matriz(qtdLinhasTabela,qtdColunasTabela,0,'I')
    sortearBombas(tabuleiro,qtdLinhasTabela,qtdColunasTabela,qtdBombas)
    prencherCamposNum(tabuleiro, qtdLinhasTabela,qtdColunasTabela)
    return tabuleiro
#---------------------------------------------------------

#---------------------------------------------------------------------------------------------------
#------------------------------ MONTAGEM DO TABULERO (FIM) -----------------------------------------
#---------------------------------------------------------------------------------------------------
#************

#************
#---------------------------------------------------------------------------------------------------
#--------------------------- MANIPULAÇÃO DO TABULERO (INICIO) --------------------------------------
#---------------------------------------------------------------------------------------------------

#--------- Função para Virar o Quadrado --------------
def virarQuadrado(linha,coluna,tabuleiro):
    tabuleiro[linha][coluna][1] = 'A'
#-------------------------------------------------------

#--------- Função para Listar Quadrados Vizinhos --------------
def listarQuadradosVizinhos(linha,coluna,n_linhas,n_colunas):
    listaVizinhos = []
    if((coluna-1) >= 0):
        listaVizinhos.append((linha,coluna-1))        
    if((coluna+1) <= n_colunas-1):
        listaVizinhos.append((linha,coluna+1))
    if(linha-1 >=0):
        listaVizinhos.append((linha-1,coluna))
    if(linha+1 <= n_linhas-1):
        listaVizinhos.append((linha+1,coluna))
    if(linha-1 >=0 and (coluna-1) >= 0):
        listaVizinhos.append((linha-1,coluna-1))
    if(linha+1 <= n_linhas-1 and (coluna+1) <= n_colunas-1):
        listaVizinhos.append((linha+1,coluna+1))
    if(linha-1 >=0 and (coluna+1) <= n_colunas-1):
       listaVizinhos.append((linha-1,coluna+1))
    if(linha+1 <= n_linhas-1 and (coluna-1) >= 0):
        listaVizinhos.append((linha+1,coluna-1))
    return listaVizinhos
            
#--------------------------------------------------------------

#--------- Função para Virar Quadrados Vizinhos --------------
def virarQuadradosVizinhos(linha,coluna,tabuleiro,n_linhas,n_colunas):
    #print('teste inicio funcao -')
    qVizinhos = listarQuadradosVizinhos(linha,coluna,n_linhas,n_colunas)
    #print('quadrados vizinhos',qVizinhos)
    listaVirar = [(0,0)]
    #print('lista aqui -',listaVirar)
    r = 0
    #for r in range(len(listaVirar)):
    while r < len(listaVirar):
        #print('teste loop')

        p = 0
        while p < len(qVizinhos): 
            #print('p',p)
            #print('tamanho p',len(qVizinhos))
            #print('-----',qVizinhos[p][0],qVizinhos[p][1])
            #print('-----',tabuleiro[qVizinhos[p][0]][qVizinhos[p][1]][0],tabuleiro[qVizinhos[p][0]][qVizinhos[p][1]][1])
            if(tabuleiro[qVizinhos[p][0]][qVizinhos[p][1]][0] == 0 and tabuleiro[qVizinhos[p][0]][qVizinhos[p][1]][1] == 'I'):
                #print('estou no if')
                #print('r 1',r)
                if r == 0 and p==0:
                     del listaVirar[r]
                if qVizinhos[p] not in listaVirar:
                    #print('------------->------------>--------->',qVizinhos[p])
                    listaVirar.append(qVizinhos[p])
                    #print(listaVirar)
            else:
                #print('estou no else')
                del qVizinhos[p]
                p=p-1
            p = p + 1
        #print('r 2',r)
        qVizinhos = listarQuadradosVizinhos(listaVirar[r][0],listaVirar[r][1],n_linhas,n_colunas)
        #print('quadrados vizinhos',qVizinhos)
        r = r + 1

    #print('lista para virar -',listaVirar)
    
    q = 0
    for cont in range(len(listaVirar)):
        i=listaVirar[q][0]
        j=listaVirar[q][1]
        x = 1
        while(0<=(i-x)<n_linhas and 0<=(j-x)<n_colunas and tabuleiro[i-x][j-x][0] == 0):
            tabuleiro[i-x][j-x][1] = 'A'
            x = x + 1
            
        x = 1
        while(0<=(i-x)<n_linhas and 0<=(j)<n_colunas and tabuleiro[i-x][j][0] == 0):
            tabuleiro[i-x][j][1] = 'A'
            x = x + 1

        x = 1
        while(0<=(i-x)<n_linhas and 0<=(j+x)<n_colunas and tabuleiro[i-x][j+x][0] == 0):
            tabuleiro[i-x][j+x][1] = 'A'
            x = x + 1

        x = 1
        while(0<=(i)<n_linhas and 0<=(j-x)<n_colunas and tabuleiro[i][j-x][0] == 0):
            tabuleiro[i][j-x][1] = 'A'
            x = x + 1

        x = 1
        while(0<=(i)<n_linhas and 0<=(j+x)<n_colunas and tabuleiro[i][j+x][0] == 0):
            tabuleiro[i][j+x][1] = 'A'
            x = x + 1

        x = 1
        while(0<=(i+x)<n_linhas and 0<=(j-x)<n_colunas and tabuleiro[i+x][j-x][0] == 0):
            tabuleiro[i+x][j-x][1] = 'A'
            x = x + 1

        x = 1
        while(0<=(i+x)<n_linhas and 0<=(j)<n_colunas and tabuleiro[i+x][j][0] == 0):
            tabuleiro[i+x][j][1] = 'A'
            x = x + 1

        x = 1
        while(0<=(i+x)<n_linhas and 0<=(j+x)<n_colunas and tabuleiro[i+x][j+x][0] == 0):
            tabuleiro[i+x][j+x][1] = 'A'
            x = x + 1

        q = q + 1
    
#---------------------------------------------------------------

#--------- Função para Validar o Quadrado --------------
def validarQuadrado(linha,coluna,tabuleiro):
    if(tabuleiro[linha][coluna][1] == 'A' and tabuleiro[linha][coluna][0] == 'B'):
        verificacao = 'bomba'
    else:
        verificacao = 'ok'
    return  verificacao    
#-------------------------------------------------------

#--------- Função para Indicar Quadrado Suspeito -------
def indicarSuspeito(tabuleiro):
    tabuleiro[i][j][1] = 'S'
#-------------------------------------------------------


#--------- Função para colocar Flag no Quadrado --------------
def colocarFlag(tabuleiro):
    tabuleiro[i][j][1] = 'F'
#-------------------------------------------------------
            
#--------- Função 'Click' --------------
def click(linha,coluna,tabuleiro,n_linhas,n_colunas):
    virarQuadrado(linha,coluna,tabuleiro)
    resultado = validarQuadrado(linha,coluna,tabuleiro)
    if(resultado == 'ok'):
        if(tabuleiro[linha][coluna][1] == 'A' and tabuleiro[linha][coluna][0] == 0):
            virarQuadradosVizinhos(linha,coluna,tabuleiro,n_linhas,n_colunas)
        status = 'continuar'
    else:
        status = 'interromper'

    return status
#---------------------------------------------------------------

#--------- Função para Listar Quadrados virados --------------
def listarQuadradosInativos(n_linhas,n_colunas,tabuleiro):
    contador = 0
    listaQuadardosInativos = []
    for i in range(n_linhas):
        for j in range(n_colunas):
            contador = contador + 1
            if(tabuleiro[i][j][1] == 'I'):
                listaQuadardosInativos.append(contador)
    return listaQuadardosInativos
#-------------------------------------------------------------

#--------- Função para Identificar o Quadrados por um Número Indice --------------
def encontrarQuadradoPeloNumero(numero,n_linhas,n_colunas,tabuleiro):
    contador = 0
    for i in range(n_linhas):
        for j in range(n_colunas):
            contador = contador + 1
            if(numero == contador):
                break
        if(numero == contador):
            break
    quadrado = [i,j]
    return quadrado
#--------------------------------------------------------------------------------


#------------ Função para Imprimir Tabuleiro --------------
def imprimirTabuleiro(n_linhas, tabuleiro):
    for i in range(n_linhas):
        print(tabuleiro[i])
#----------------------------------------------------------

#---------------------------------------------------------------------------------------------------
#------------------------------ MANIPULAÇÃO DO TABULERO (FIM) --------------------------------------
#---------------------------------------------------------------------------------------------------
#************
        
#************
#---------------------------------------------------------------------------------------------------
#-------------------------------- IMPLEMENTAÇÃO DE REGRAS (INICIO) ---------------------------------
#---------------------------------------------------------------------------------------------------

def posicionamento1(i,j,tabuleiro):
    if(tabuleiro[i][j+1][0] == 2 and
        tabuleiro[i][j-1][0] != 'B' and tabuleiro[i][j-1][1] == 'A' and    #leste
       tabuleiro[i-1][j-1][0] != 'B' and tabuleiro[i-1][j-1][1] == 'A' and #
       tabuleiro[i-1][j][0] != 'B' and tabuleiro[i-1][j][1] == 'A' and     #norte
       tabuleiro[i-1][j+1][0] != 'B' and tabuleiro[i-1][j+1][1] == 'A' and
       tabuleiro[i-1][j+2][0] != 'B' and tabuleiro[i-1][j+2][1] == 'A' and
       tabuleiro[i][j+2][0] != 'B' and tabuleiro[i][j+2][1] == 'A' and     #oeste
       tabuleiro[i+1][j-1][1] == 'I' and tabuleiro[i+1][j][1] == 'I' and
       tabuleiro[i+1][j+1][1] == 'I' and tabuleiro[i+1][j+2][1] == 'I'):
        posicao = 'ok'
    else:
        posicao = 'er'
    return posicao

def posicionamento2(i,j,tabuleiro):
    if(tabuleiro[i][j-1][0] == 2 and
        tabuleiro[i][j-1][0] != 'B' and tabuleiro[i][j-1][1] == 'A' and #leste
       tabuleiro[i-1][j-1][0] != 'B' and tabuleiro[i-1][j-1][1] == 'A' and
       tabuleiro[i-1][j][0] != 'B' and tabuleiro[i-1][j][1] == 'A' and
       tabuleiro[i-1][j+1][0] != 'B' and tabuleiro[i-1][j+1][1] == 'A' and
       tabuleiro[i-1][j-2][0] != 'B' and tabuleiro[i-1][j-2][1] == 'A' and
       tabuleiro[i][j-2][0] != 'B' and tabuleiro[i][j-2][1] == 'A' and
       tabuleiro[i+1][j-1][1] == 'I' and tabuleiro[i+1][j][1] == 'I' and
       tabuleiro[i+1][j+1][1] == 'I' and tabuleiro[i+1][j+2][1] == 'I'):
        posicao = 'ok'
    else:
        posicao = 'er'
    return posicao

'''  x xx
     x21x
0000 | x000 | xxxx | 000x | condição 1 - existir quadrado Q1 aberto(A) e com valor 1
0000 | x100 | 0120 | 001x | condição 2 - Q1 ter um vizinho Q2, tambem aberto(A) com valor 2
0120 | x200 | 0000 | 002x | condição 3 - existir 6 vizinhos consecutivos de Q1Q2 aberto(A) e com valor 0 
xxxx | x000 | 0000 | 000x | condição 4 - existir 3 vizinhos consecutivos de Q1Q2 fechado(I)
'''
def regra_1_2(n_linhas,n_colunas,tabuleiro):
    contador = 0
    listaQuadrados_1 = []

    for i in range(n_linhas):
        for j in range(n_colunas):
            contador = contador + 1
            if(tabuleiro[i][j][0] == 1):
                listaQuadrados_1.append(contador)

    print(listaQuadrados_1)

    if len(listaQuadrados_1) > 0:
        for q in range(len(listaQuadrados_1)):
            indiceQ = encontrarQuadradoPeloNumero(listaQuadrados_1[q],n_linhas,n_colunas,tabuleiro)
            #print('quadrados com valor 1 -',indiceQ)
            if indiceQ[0] > 0 and indiceQ[0] < (n_linhas-1) and indiceQ[1] > 0 and indiceQ[1] < (n_colunas-1): 
                #print("xxx--->",tabuleiro[indiceQ[0]][indiceQ[1]])
                #print("xxx--->",tabuleiro[indiceQ[0]][indiceQ[1]+1])
                if(posicionamento1(indiceQ[0],indiceQ[1],tabuleiro)=="ok"):
                    print("achei!!")
                    tabuleiro[indiceQ[0]+1][indiceQ[1]+2][1] = 'F'
                    click(indiceQ[0]+1,indiceQ[1]-1,tabuleiro,n_linhas,n_colunas)
                if(posicionamento2(indiceQ[0],indiceQ[1],tabuleiro)=="ok"):
                    print("achei!!")
                    tabuleiro[indiceQ[0]+1][indiceQ[1]-2][1] = 'F'
                    click(indiceQ[0]+1,indiceQ[1]+1,tabuleiro,n_linhas,n_colunas)
                    #imprimirTabuleiro(qtdLinhasTabela, tabuleiro)
                #if(tabuleiro[indiceQ[0]][indiceQ[1]+1][0] == 2 and posicionamento2(indiceQ[0],indiceQ[1],tabuleiro)=="ok"):
                #if(tabuleiro[indiceQ[0]][indiceQ[1]+1][0] == 2 and posicionamento3(indiceQ[0],indiceQ[1],tabuleiro)=="ok"):
                #if(tabuleiro[indiceQ[0]][indiceQ[1]+1][0] == 2 and posicionamento4(indiceQ[0],indiceQ[1],tabuleiro)=="ok"):

#---------------------------------------------------------------------------------------------------
#-------------------------------- IMPLEMENTAÇÃO DE REGRAS (FIM) ------------------------------------
#---------------------------------------------------------------------------------------------------
#************

#************
#---------------------------------------------------------------------------------------------------
#---------------------------------- ROTINAS DE RESOLUÇÃO (INICIO) ----------------------------------
#---------------------------------------------------------------------------------------------------
def forcaBruta(n_linhas,n_colunas,n_bombas):
    vitorias = 0
    derrotas = 0
    jogos = 1
    
    while vitorias == 0:
        print('Jogo',jogos)
        print('Placar')
        print('Vitorias',vitorias,"x",derrotas,'Derrotas')
        tabuleiro = montarTabuleiroCompleto()
        imprimirTabuleiro(qtdLinhasTabela, tabuleiro)

        for reps in range((n_linhas * n_colunas)-n_bombas):
            lista = listarQuadradosInativos(n_linhas,n_colunas,tabuleiro)
            print(lista)
            numQuadradoSorteado = random.choice(lista)
            quadradoSorteado = encontrarQuadradoPeloNumero(numQuadradoSorteado,n_linhas,n_colunas,tabuleiro)
            print("Clique -",reps, "|Posição -", numQuadradoSorteado,"|Quadrado-", quadradoSorteado)
            status = click(quadradoSorteado[0],quadradoSorteado[1],tabuleiro,n_linhas,n_colunas)
            if(status == 'interromper'):    
                print('Game Over')
                imprimirTabuleiro(qtdLinhasTabela, tabuleiro)
                derrotas = derrotas + 1
                break
            if((reps+1) == ((n_linhas * n_colunas)- n_bombas)):
                vitorias = 1
        jogos = jogos + 1       

    print('Vitorias',vitorias,"x",derrotas,'Derrotas')
    imprimirTabuleiro(qtdLinhasTabela, tabuleiro)

def simularClickAleatorio(n_linhas,n_colunas,tabuleiro):
    lista = listarQuadradosInativos(n_linhas,n_colunas,tabuleiro)
    print('lista quadrados inativos -',lista)
    numQuadradoSorteado = random.choice(lista)
    quadradoSorteado = encontrarQuadradoPeloNumero(numQuadradoSorteado,n_linhas,n_colunas,tabuleiro)
    print('quadrado clicado -',quadradoSorteado)
    status = click(quadradoSorteado[0],quadradoSorteado[1],tabuleiro,n_linhas,n_colunas)
    if(status == 'interromper'):    
        print('Game Over')
        imprimirTabuleiro(qtdLinhasTabela, tabuleiro)
    #imprimirTabuleiro(qtdLinhasTabela, tabuleiro)

def rotinaRegrasBasicas(n_linhas,n_colunas):
    tabuleiro = montarTabuleiroCompleto()
    imprimirTabuleiro(qtdLinhasTabela, tabuleiro)
    for x in range(4):
        simularClickAleatorio(n_linhas,n_colunas,tabuleiro)
        regra_1_2(n_linhas,n_colunas,tabuleiro)
    imprimirTabuleiro(qtdLinhasTabela, tabuleiro)
    
def testeBasico():
    tabuleiro = crie_matriz(qtdLinhasTabela,qtdColunasTabela,0,'I')
    print('posição das bombas')
    sortearBombas(tabuleiro,qtdLinhasTabela,qtdColunasTabela,qtdBombas)
    prencherCamposNum(tabuleiro, qtdLinhasTabela,qtdColunasTabela)
    print('tabuleiro ANTES do click')
    print(tabuleiro)
    click(3,3,tabuleiro,qtdLinhasTabela,qtdColunasTabela)
    print('tabuleiro DEPOIS do click')
    print(tabuleiro)

def testes(n_linhas,n_colunas):
    tabuleiro = montarTabuleiroCompleto()
    imprimirTabuleiro(qtdLinhasTabela, tabuleiro)
    linha = 0
    coluna = 0
    listarQuadradosVizinhos(linha,coluna,n_linhas,n_colunas)

#---------------------------------------------------------------------------------------------------
#---------------------------------- ROTINAS DE RESOLUÇÃO (FIM) -----------------------------------------
#---------------------------------------------------------------------------------------------------
#************

#************
#---------------------------------------------------------------------------------------------------
#---------------------------------- START ROTINAS (INICIO) -----------------------------------------
#---------------------------------------------------------------------------------------------------

#forcaBruta(qtdLinhasTabela,qtdColunasTabela,qtdBombas)
rotinaRegrasBasicas(qtdLinhasTabela,qtdColunasTabela)
#testeBasico()
#testes(qtdLinhasTabela,qtdColunasTabela)

#---------------------------------------------------------------------------------------------------
#---------------------------------- START ROTINAS (FIM) --------------------------------------------
#---------------------------------------------------------------------------------------------------
#************

#possiveis estados dos quadrados
# I - inativo
# A - ativo
# S - suspeito
# F - flag 
