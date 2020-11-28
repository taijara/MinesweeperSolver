# MinesweeperSolver

UFBA - UNIVERSIDADE FEDERAL DA BAHIA
DEPARTAMENTO DE CIÊNCIA DA COMPUTAÇÃO

MATA52 - ANÁLISE E PROJETO DE ALGORITMOS | MATD74 - ALGORITMOS E GRAFOS 
PROFESSORES: GEORGE LIMA E RAFAEL MELO 
				
EQUIPE:
Jamile de Barros Vasconcelos
	Paulo da Silva Cruz
	Taijara Loiola de Santana


PROBLEMA

JOGO CAMPO MINADO (Minesweeper)
Versão de decisão


a) Descrição formal do problema.


Descrição Informal
O Campo Minado é um jogo que consiste em um tabuleiro m X n (onde m, n ∈ 𝕫2), composto por quadrados que iniciam escondidos e, ao serem clicados, podem revelar uma bomba b, um quadrado vazio ou um número natural  k ∈ [0,8] (não negativo) que sinaliza a quantidade de bombas que há ao redor e localizadas nos quadrados adjacentes (quadrados com os quais compartilham um canto, lado ou aresta),. (YOUNG, FOWLER, 2004)
É possível ainda sinalizar/marcar um quadrado com uma "bandeira", para os casos em que o jogador tem certeza do local da bomba, ou com o símbolo de "interrogação", caso haja uma desconfiança de que ali pode existir uma bomba. As marcações são formas do jogador traçar sua estratégia.
O objetivo final do jogo é revelar todos os espaços em branco e marcar com uma bandeira todos os quadrados que contém uma bomba. Consequentemente, ao revelar uma bomba perde-se o jogo. 
Além destas ações, o jogo fornece algumas dicas. O Campo Minado tradicional informa o número total de bombas existentes. Apesar das regras, há momentos que o jogo não fornece opções lógicas, deixando o jogador relegado à sua própria sorte. Desta forma, o jogo é uma mistura de elementos do acaso, raciocínio lógico e estratégias. Existe um ranking mundial do Campo Minado Tradicional no site http://www.minesweeper.info/


Descrição Formal 
Am,n,b é um tabuleiro, conjunto de todos os quadrados m x n com b bombas 
B é tabuleiro, sendo B ∈ Am,n,b , e Bi,j  o quadrado nas coordenadas (i,j) onde 1 ≤ i ≤ m , 1 ≤ j ≤ n, e i,j ∈ 𝕫
Dado o tabuleiro B e o quadrado Bi,j  ∈ B,  K(Bi,j) representa o conteúdo de Bi,j
Dado o tabuleiro B e o quadrado Bi,j  ∈ B, sendo RBi,j ∈ B todos os quadrados adjacentes a Bi,j. (YOUNG, FOWLER, 2004)

Sendo i = (i; j), para cada i ∈ R, o conjunto de quadrados adjacentes é definido por Ri = {i + r | r ∈ R} ∩ A; onde R = {(1; 1); (0; 1); (1; 1); (1; 0); (1;1); (0;1); (1;1); (1; 0)}.(GERMAN, LAKSHTANOV, 2010)


b) Justificativa (ou demonstração) de o problema ser NP-difícil (ou NP-completo);

O Problema do Campo Minado
Campo Minado é um jogo de computador que exige que se localize as bombas sem explodi-las. Quando executado com habilidade, ele pode ser concluído sem a necessidade de muitas suposições arriscadas, entretanto, é necessário que o jogador não cometa erros como: realizar movimentos arriscados, quando há possibilidade de revelar um quadrado com segurança, e não determinar imediatamente que um quadrado está livre de bombas, marcando-o e checando em seguida se isso é correto. 
Em linhas gerais, a solução do Campo Minado pode ser expressa por uma matriz Booleana S de dimensões Sn×m que informa as células que o usuário pode clicar. Percorre-se a matriz Sn×m e, para cada valor verdadeiro si,j ∈ S, verifica-se a célula da posição [i,j] correspondente no campo minado original para confirmar se a solução é válida. Este procedimento tem custo computacional O(n · m). (JANUÁRIO, 2016)
O jogo traz um tipo de problema bem geral e pode-se usar um algoritmo para tentar encontrar sua solução completa. Para resolvê-lo utilizando uma solução "força bruta", por exemplo, bastaria percorrer todas as diferentes combinações de bombas no campo. Entretanto, o jogo tradicional traz variadas versões. Dentre estas, podemos citar um modo “avançado” que contém 99 bombas distribuídas em 480 quadrados. A resolução computacional deste tabuleiro implicaria em 5602209993374213454290589857758... 9570631168198385673295159633481600 ou acima de 10100 possibilidades de distribuição das bombas, o que representaria uma demanda considerável de tempo. (KAYE, 2003)
Campo Minado traz como dificuldade o fato de ser um espaço de estado infinito. Este espaço é representado por O(Cms 2m-s) onde  Cms é o número de minas distribuídas e 2m-s mostra se um quadrado é revelado. (TANG, TIAN, 2018)
Além disso, há inúmeras incertezas para resolver o jogo. Há situações que não é possível fazer deduções, sendo necessário fazer "adivinhações". Nesses casos, um jogador humano comum, por exemplo, pode ser obrigado a fazer um "chute" para definir o próximo passo. Um caminho é fazer esta adivinhação através com a probabilidade do quadrado ser uma mina. De qualquer sorte, é um processo incerto que pode facilmente culminar com o fracasso da partida. Uma situação como esta pode acontecer até mesmo na primeira jogada; não há regras que impeçam que o primeiro quadrado seja bomba.
Até o momento, não há um método conhecido que determine uma solução em tempo razoável para o Minesweeper em uma versão de maior escala do jogo. É possível encontrar essa solução? É possível ter um algoritmo eficiente e rápido, que consuma um tempo proporcional a um polinômio fixo com relação ao número de quadrados na configuração de entrada, ao invés de um tempo exponencial? Parece provável que não mas, até hoje, ninguém foi capaz de afirmar ou negar, de forma definitiva e comprovada, esta pergunta.
 
Problema de decisão
Na teoria da complexidade computacional, um problema de decisão é uma questão que está relacionada a um conjunto finito de parâmetros, que têm como resposta “sim” ou “não”. Ao longo do tempo, foram estudados dois problemas de decisão relacionados ao jogo Campo Minado:

1) CONSISTÊNCIA: O problema de consistência do Campo Minado (MCP) coloca a seguinte questão: dado um grid de jogo, ele é consistente? Ou seja, dada uma configuração do tabuleiro, existe uma atribuição de bombas para as células não reveladas, que seja consistente com a configuração?
MCT - Problema de Consistência Campo Minado
Instância: Uma matriz de tamanho m×n, sendo cada campo ou livre, ou com um número, ou escondido.
Decisão: A matriz é consistente (há uma disposição de bombas que é consistente com os números visíveis e espaços marcados)?
(RITT, 2011)
2) INFERÊNCIA (INFERENCE): O Problema de Inferência do Campo Minado questiona se é possível localizar todas as bombas dado um tabuleiro (board) do Campo Minado. A complexidade deste problema foi provada CoNP-Complete por Scott, Stege e Rooij (2011), através de redução a partir do problema de Circuito UNSAT. Os autores trazem como crítica ao trabalho onde Kaye (2000) prova que o jogo é NP-Completo, o fato deste não ter considerado que o Campo Minado tradicional informa ao jogador a quantidade total de bombas da partida.

Problemas de natureza co-NP-Completo não são objeto deste trabalho  Será avaliado a seguir porque Campo Minado é NP-Completo.

O Campo Minado está ainda associado a outras classes, em outros contextos. Apenas a título de curiosidade citamos algumas: é Sharp-P-Complete quando há descrição do tabuleiro do jogo como CSP (Constraint Satisfaction Problem) e utilizado um solver geral para encontrar todas as possibilidades de distribuição das bombas (CICVÁREK, 2017) e PP-Hard, quando o objetivo é localizar todas as minas com maior probabilidade (DE BONDT, 2000). A complexidade teórica para geração de um tabuleiro solucionável é desconhecida. (CICVÁREK, 2017)

Complexidade Computacional e NP-Completude
Na teoria da complexidade computacional, a classe P (Deterministic Polynomial time) está associada aos problemas tratáveis, que podem ser resolvidos em tempo polinomial. A Classe NP significa Tempo Polinomial Não-Determinístico (Non-Deterministic Polynomial time) e é a que denota o conjunto de problemas que são decidíveis em tempo polinomial por uma máquina de Turing não-determinística.
Desde 1971 a comunidade científica discute sobre a possibilidade de haver (ou não haver) um algoritmo capaz de reduzir ou redefinir problemas NP de forma que estes pudessem ser resolvidos em tempo polinomial. Caso alguém prove que todos os problemas NP são variações de problemas P, então todos os problemas NP estariam, em essência, sujeitos a este tipo de redução. Daí surge o problema P versus NP. 
Um problema pertence à classe NP-Completo, por sua vez, se ele está em NP (pode ser verificado em tempo polinomial ou existe um algoritmo não-determinístico polinomial que o resolva), e se qualquer problema que está em NP pode ser transformado (ou reduzido) em tempo polinomial. Se você conseguir resolver um problema NP-Completo em tempo polinomial, você terá resolvido todos os problemas NP em tempo polinomial. 
Existem vários problemas NP-completo e um dos mais simples é o SAT (Boolean Satisfiability Problem), que envolve circuito Booleanos. Todo problema da classe NP pode ser reduzido polinomialmente ao SAT. Trata-se de circuitos construídos a partir de portas lógicas, AND, OR e NOT, e trabalham com duas entradas: T(1) para verdadeiro e F(0) para falso. Existe uma ligação de cada porta que, de maneira específica, produz um resultado como sua saída. Uma maneira de demonstração é, considerando uma porta NOT, a mesma transforma uma entrada T em uma saída F, e assim vice-versa. O problema SAT é um circuito simples, mas se torna difícil quando há uma grande demanda de entradas.  
Richard Kaye (2000) apontou uma relação entre o jogo campo minado e o problema P vs. NP, através do SAT. A conexão surge com o problema de decisão MCT (Problema de Consistência do Campo Minado). (STEWART, 2000)
Conforme apontado no item anterior, o desafio do MCP não é encontrar as bombas, mas determinar se uma posição do tabuleiro é logicamente consistente. Se, por exemplo, durante o jogo, for encontrada a posição "(b)" ilustrada abaixo, sabe-se que o programador cometeu um erro. Ao contrário da figura "(a)", que traz uma configuração consistente.









(KAYE,2000)
Kaye (2000) prova que o Problema SAT de um dado circuito Booleano pode ser transformado no problema de consistência para uma posição do jogo Campo Minado.
O autor começa demonstrando que CONSISTÊNCIA está na classe NP. O certificado para a consistência é a atribuição de bombas às células cobertas. O verificador checa que essas bombas produzem os números no tabuleiro. Kaye então argumenta que a consistência é, de fato, NP-Completo. Ele monta uma construção de fios e portas lógicas Booleanas a partir das configurações do Campo Minado. (BECERRA, 2015) Apesar da complicada eletrônica do jogo, o autor consegue resolver todas estas limitações. Richard então mostra como construir partes do Campo Minado que se comportam como portas lógicas, onde certos quadrados gerados pela redução possuem minas se e somente se um componente do circuito reduzido produz uma saída 1. (FIX, MCPHAIL, 2004)
Com esta estrutura bem definida para as portas lógicas, ele, por fim, é capaz de fornecer uma redução em tempo polinomial do SAT para Consistência, o que leva, assim, a constatação que Campo Minado é NP-Completo. 
Conclui-se, desta forma, que reduzindo instâncias do SAT fornecidas como circuitos  de portas lógicas Booleanas a instâncias do jogo, Richard Kaye forneceu uma redução em tempo polinomial do SAT para o Campo Minado, mostrando que o jogo é NP-Completo.(BEN-ARI, 2005)


c) Breve revisão da literatura contendo trabalhos relacionados (o problema em questão e/ou problemas similares) e pequena descrição das técnicas já usadas para resolver os problemas em questão;

Campo Minado se torna matemático à partir do momento que busca-se estratégias para vencer o jogo. Desde que Richard Kaye (KAYE, 2020) provou que ele é NP-Completo ao reduzi-lo ao problema de satisfabilidade de circuito (SAT), variadas técnicas e estratégias, de variadas complexidades e eficácias, foram elaboradas para encontrar novas soluções para resolver o problema e vencer o jogo. 
Algumas destas soluções são triviais e resultam em baixa probabilidade de vitória, outras são avançadas e complexas, exigem alto nível de conhecimento matemático, e apresentam resultados com elevadas taxas de sucesso. Estas soluções passam por variados objetivos e critérios como: propor novas reduções, implementar originais provas de complexidade, buscar estratégias diferentes para algoritmos já existentes ou modificar a estrutura dos já testados. Dentre os diversos modelos e estruturas de dados utilizados, encontra-se redes neurais, grafos, árvores, matrizes, machine learning, processos heurísticos, processo de decisão de Markov, redes bayesianas e programação genética.
O jogo traz ainda como item adicional o fato de estar sujeito ao fator sorte, trazendo situações onde não há um caminho lógico a ser seguido e o jogador precisa fazer adivinhações, "chutes". Mesmo para um habilidoso jogador ou para o mais eficiente algoritmo, uma escolha errada nestas situações pode levar ao fracasso da partida e, gastar tempo para resolvê-la, pode apenas representar uma perda de tempo. Por este motivo, questiona-se que talvez a saída razoável seja avaliar o problema sob um ponto de vista probabilístico, ao invés de dedução lógica. No entanto, KAYEb (2000) pontua que, apesar de concordar que trata-se de um problema com indicação para uma solução probabilística, esta saída tornaria ainda maior a sua complexidade.
Atualmente Campo Minado é mencionado pelo Clay Mathematics Institute na descrição não-oficial do prêmio "P versus NP", um dos mais importantes problemas em aberto deste milênio. KAYE (2000) afirma que a descoberta de um algoritmo que determine todas as combinações das localizações das minas em uma versão em escala maior do Minesweeper, implica também na solução do problema. Ou seja, se for encontrada uma solução em tempo polinomial para o MCT, Problema de Consistência do Campo Minado, todos os problemas NP terão soluções em tempo polinomial e, portanto, P é igual a NP. Da mesma forma, se for provado que tal solução não existe para este problema, então P não é igual a NP, e a questão seria respondida da mesma forma.
Dentre os algoritmos mais conhecidos para resolver os tabuleiros do Campo Minado, ou para gerar o tabuleiro e resolvê-lo, destaca-se: Single Point e CSPStrategy, Equation strategy. (CICVÁREK, 2017)
Single Point Strategy (SPS): Algoritmo muito utilizado em soluções complexas. Opera em um ponto único do tabuleiro em busca de espaço, tendo este ponto gradualmente expandido em busca de uma melhor localização. Cada iteração do algoritmo consiste em duas etapas:		
1. For every clear square, the algorithm compares number of mines in vicinity and the number of marked mines in vicinity. If they equal and there are any undecided neighbours, algorithm marks undecided neighbours as clear.
 2. For every clear square, the algorithm compares number of mines in vicinity and the number of unrevealed neighbour squares. If the two numbers are equal, algorithm marks all undecided neighbour squares as mines.  (CICVÁREK, 2017)
 						
Em todas as etapas deste algoritmo é necessário passar por todos os quadrados em branco, mas o número total destes quadrados é sempre menor que m*n e o tempo para resolver cada quadrado é uma constante. Por este motivo, este passo pode ser realizado em tempo polinomial.  (CICVÁREK, 2017) Desenvolvido por John D. Ramsdell em um projeto de software chamado PGMS (Programmer's Minesweeper). 

CSPStrategy: Implementado por C. Studholme. Este algoritmo é conhecido por resolver o jogo mais rapidamente que qualquer outro. Neste caso, cada estado do tabuleiro é implementado como um Problema de Satisfação de Constraint e as constraints (restrições) são representadas como um conjunto de equações. (CICVÁREK, 2017)
These equations are simplified and divided into subsets of equations with same variables. These equations are solved with a backtracking algorithm. Variables are each in turn assigned a value. After every such assignment, all the constraints are checked. If there still is a solution for the equations, another assignment is made, if there isn’t one, backtracking fetches previous configuration. When domain of any variable is reduced to only one, the new step is made and new constraints formed. 
 
Equation strategy: Também integra o projeto PGMS, de John D. Ramsdell. É uma solução que  também interpreta o jogo como um conjunto linear de equações, mas relaciona as equações diretamente ao quadrado no tabuleiro do qual ele se origina e usa esta relação para passar por eles. O Algoritmo é formado por três algoritmos independentes que rodam ao mesmo tempo, independentemente do resultado do anterior, mas todos modificam o mesmo tabuleiro e conjunto de equações. O primeiro algoritmo é o Single Point, o segundo não realiza muitas etapas, apenas expande os conjuntos em conhecidas equações em um caso especial. O terceiro algoritmo foca em subtrair duas equações em uma."	
		Apresentamos a seguir uma revisão de literatura elencando trabalhos relacionados ao Campo Minado.

BECERRA, David J. Algorithmic Approaches to Playing Minesweeper. Bachelor's thesis, Harvard College (2015) || https://dash.harvard.edu/bitstream/handle/1/14398552/BECERRA-SENIORTHESIS-2015.pdf?sequence=1
Explora desafios associados a algoritmos para resolução do Campo Minado. Levanta formas para iniciar o jogo, heurísticas para lidar com os elementos de sorte (chutes) e estratégias para deduções determinísticas. Explora a abordagem Single Point e modelo do problema de satisfação de restrição(constraint) e propõe duas novas implementações.

CASTILLO, Lourdes Pena. Search improvements in multirelational learning. (2004). || http://www.minesweeper.info/articles/SearchImprovementsInMultirelationalLearning.pdf
Apresenta como é possível aplicar técnicas de aprendizagem com sistemas multirelacionais (multirelational learning systems) e aprendizado indutivo (inductive learning) para implementar estratégia para o jogo do Campo Minado.
				 							
DE BONDT, Michiel. The computational complexity of Minesweeper. arXiv preprint arXiv:1204.4659 (2012). || https://arxiv.org/abs/1204.4659
Questiona a prova NP-Completo de Kayea (2000), afirmando que este autor ignora o fato de que o número total de minas é conhecido no jogo Minesweeper. Mostra que Minesweeper é PP-Hard quando o objetivo é alocar todas as minas com maior probabilidade e PSPACE-Complete quando a probabilidade para localizar todas as minas for infinitesimal.

KADLAC, M., Explorations of the Minesweeper Consistency Problem, Proceedings of the Research Experiences for Undergraduates Program in Mathematics, Oregon State University, pp.78-126 , 2003. || http://sites.science.oregonstate.edu/~math_reu/proceedings/REU_Proceedings/Proceedings2003/2003MK.pdf					 
Solução restringiu o problema a uma estrutura unidimensional para torná-lo mais simples. Autor mostrou que a consistência deste problema é regular e pode ser reconhecida por um autômato finito determinístico. 
 
KAYEa, Richard. Minesweeper is NP-complete. The Mathematical Intelligencer 22.2 (2000): 9-15. || http://simon.bailey.at/random/kaye.minesweeper.pdf	
Publicação que prova que Minesweeper é NP-Completo. Para o autor, se for descoberto um algoritmo que determine todas as combinações das localizações das minas em uma versão em escala maior do Minesweeper, o problema P versus NP estará resolvido.

KAYEb, Richard. Some minesweeper configurations. http://www. mat. bham. ac. uk/RW Kaye (2000). || http://web.mat.bham.ac.uk/R.W.Kaye/minesw/minesw.pdf
Autor cita outras configurações desenvolvidas para o jogo, tais como: grids em formatos diferentes de quadrado ou retângulo, como forma triangular, hexagonal,..., além de versão tridimensional e versão infinita.

KAYE, Richard. Infinite versions of minesweeper are Turing-complete. Manuscript, August (2000). || http://web.mat.bham.ac.uk/R.W.Kaye/minesw/infmsw.pdf
Proposta de variação do Campo Minado, prevendo uma grade quadrada infinita. 

GOLAN, Shahar. Minesweeper on graphs. Applied mathematics and computation 217.14 (2011): 6616-6623. || https://www.sciencedirect.com/science/article/abs/pii/S0096300311000622
Avalia os problemas de consistência, contagem e satisfação de restrições (constrained counting) para o Campo Minado usando árvores e grafos de largura limitada, fornecendo algoritmos polinomiais e provando suas corretudes.

GOLAN, S. Minesweeper strategy for one mine. Applied Mathematics and Computation, 232, 292–302. doi:10.1016/j.amc.2014.01.045 (2014) || https://www.sciencedirect.com/science/article/abs/pii/S0096300314000824
Apresenta uma estratégia considerada ótima usando grafos para um Campo Minado contendo apenas 01 mina. 

HU, Shu-Chiung, and Shun-Shii Lin. 2× n Minesweeper Consistency Problem is in P. Proceedings of the 2007 National Computer Symposium (NCS 2007). 2007 || http://asiair.asia.edu.tw/ir/bitstream/310904400/5809/1/9032.pdf		
Extensão do trabalho de Kadlac (2003). Estende o problema de consistência MCP para 2×n Minesweeper, estrutura bi-dimensional mas com uma dimensão restrita a 2.
		
MASSAIOLI, Robert. Solving Minesweeper with Matrices. 2013. Disponível em: https://massaioli.wordpress.com/2013/01/12/solving-minesweeper-with-matricies/. Acesso em: 16 nov. 2020. || https://massaioli.wordpress.com/2013/01/12/solving-minesweeper-with-matricies/
Demonstração de uma solução do Campo Minado através de matrizes.

NAKOV, P.; WEI, Z.; MATTERN, C. MINESWEEPER , # MINESWEEPER. v. 1991, p. 1–29, 2003. || http://www.minesweeper.info/articles/Minesweeper(Nakov,Wei).pdf
Definição de problema de contagem correspondente, denominado #MINESWEEPER, para provar que o jogo é #P-Complete.

PACKARD, Brandon. Solving a Minesweeper Board By Visually Parsing It. Clarion University of Pennsylvania, Computer Information Science Department. || 
https://d1wqtxts1xzle7.cloudfront.net/63984350/Brandon_Packard_Minebot20200721-33990-1lft446.pdf?1595354127=&response-content-disposition=inline%3B+filename%3DSolving_a_Minesweeper_Board_by_Visually.pdf&Expires=1605106321&Signature=PCOPxIBZGdlNqJh~WQ8Z~n9NQnWd3Ft2BNatfJ1loUYE1ysbIvrhdu~~npBGvSAecnTIaejoRuu6L97zf6Kw4KmDEBW~MA4SyPOG~NxOqiP1IiH04KDPsmIpOrLdWKKPowCH2qZMdeZEaUY0DLv5hnOapH0rCMQPQXR-d46XfeI7V25TQp9h35BS02uyvnjNdX9D8IHhpG0wxbvSlu28p4PMqLIgpQjJ4fYhF076hMjc1NrNMitujD2SSBvGULyZ-Wc3CrPGTQShopeh0-sAEy0IY-evVCvUTK7gT5iA13IAin1Vb0PeOlaTTldnf38jpeps57fbInEoC-BncMH4Kg__&Key-Pair-Id=APKAJLOHF5GGSLRBV4ZA
Apresenta um bot capaz de solucionar Campo Minado sem necessidade de acesso ao jogo, apenas através de visual parsing.

PEDERSEN, Kasper. The complexity of Minesweeper and strategies for game playing. Project report, univ. Warwick (2004). || http://www.minesweeper.info/articles/ComplexityMinesweeperStrategiesForGamePlaying.pdf
Trabalho busca desenvolver três estratégias para resolver o jogo; a) Single point, para identificar movimentos seguros com base em informações fornecidas por um movimento concluído e quadrados imediatamente adjacentes, b) Limited search, que compreende um algoritmo de retrocesso (backtracking), e c) Busca por estimativa probabilística, para estimar a probabilidade de cada quadrado conter uma mina. A solução "c" foi a que apresentou os melhores resultados.

QUARTETTI, Chris. Evolving a Program to Play the Game Minesweeper. Genetic Algorithms and Genetic Programming at Stanford 1998, pp. 137-146, Stanford Bookstore, 17 March 1998.
QUARTETTI, C. Evolving a Program to Play the Game Minesweeper, Genetic Algorithms and Genetic Programming at Stanford 6 (2000), 137-146. || http://www.quartetti.com/Chris/papers/minesweeper/MineSweeper_genetic_programming.pdf
Descreve como programação genética pode ser usada para jogar o Campo Minado.
	
SCOTT, Allan, Ulrike Stege, and Iris Van Rooij. Minesweeper may not be NP-complete but is hard nonetheless. The Mathematical Intelligencer 33.4 (2011): 5-17. || https://link.springer.com/article/10.1007/s00283-011-9256-x
Questiona a publicação de Kaye e afirma que Campo Minado não é NP-Completo mas um problema difícil, e defende que ele é co-NP-Complete. 

STUDHOLME, Chris. Minesweeper as a constraint satisfaction problem. Unpublished project report (2000). || http://www.cs.utoronto.ca/~cvs/minesweeper/minesweeper.pdf
Desenvolvimento de uma bem sucedida estratégia baseada em redução do problema para CSP (Constraint satisfaction problem).

VOMLELOVÁ, Marta, and Jirı Vomlel. Applying Bayesian networks in the game of Minesweeper. Proceedings of the Twelfth Czech-Japan Seminar on Data Analysis and Decision Making under Uncertainty. 2009. || http://www.minesweeper.info/articles/ApplyingBayesianNetworksToMinesweeper.pdf
Realiza experimentos com redes Bayesianas construídas para o jogo de Campo Minado.	



d) Metodologia a ser utilizada, que pode ser algoritmo ou modelo matemático. Não simplesmente repitam o que já foi feito, façam algo original.

Como já especificado, é vasta a variedade de soluções e técnicas  implementadas para resolver o Campo Minado. Este caminho pode ser encontrado a partir do desenvolvimento de novos algoritmos, adaptações de soluções já implementadas, diferentes tecnologias e estruturas, e usando variadas técnicas probabilísticas, matemáticas,  estratégicos e/ou  para dedução lógica.

A solução a ser implementada por esta proposta, propõe:

Implementar as operações e estrutura do jogo Campo Minado de forma básica, sem interface gráfica.

Implementar uma solução para resolver o jogo através do uso de regras aplicadas por jogadores do Campo Minado. 
O site http://computronium.org/minesweeper/index.html traz uma série de regras criadas com o intuito de documentar estratégias para vencer o jogo. Segundo o autor (desconhecido), estas estratégias foram descobertas por ele após extensivos jogos e análises computacionais realizadas ao longo dos anos. O mesmo defende que as inúmeras publicações encontradas sobre o Campo Minado trazem soluções lógicas mas pecam em não demonstrar e empregar situações práticas derivadas de regras simples. Estas saídas partem dos padrões de distribuição dos números tabuleiro, estruturados em diferentes categorias (básicos,  triângulos, combos, buracos e avançados).

Realizar comparativo de desempenho e checar a eficácia ou ineficácia das regras traçadas.
Para encontrar este resultado será realizada duas versões do jogo: a primeira de "força bruta", e a segunda através da utilização de algumas das regras citadas. Haverá então medição da performance de ambos os casos para variados tamanhos de tabuleiro após x tentativas.



REFERÊNCIAS BIBLIOGRÁFICAS
 
BECERRA, David J. Algorithmic Approaches to Playing Minesweeper. Bachelor's thesis, Harvard College, 2015.
 
BEN-ARI, Mordechai. Minesweeper as an np-complete problem. ACM SIGCSE Bulletin 37.4, 39-40, 2005.
 
CICVÁREK, Jan. Algorithms for Minesweeper Game Grid Generation. Trabalho de Conclusão de Curso. České vysoké učení technické v Praze. Vypočetní a informační centrum, 2017.
 
FIX, James D.; MCPHAIL, Brandon. Offline 1-Minesweeper is NP-complete. Unpublished Manuscript, Available at: www. minesweeper. info/articles/Offline1MinesweeperIsNPComplete. pdf, 2004.
 
GERMAN, Oleg; LAKSHTANOV, Evgeny. Minesweeper and spectrum of discrete Laplacians. Applicable Analysis, v. 89, n. 12, p. 1907-1916, 2010.

JANUÁRIO, Tiago de Oliveira. Salvador, BA, out  2016. Solução da prova 3, aplicada no dia 20/10/2016, para a disciplina MATD74 - Algoritmos e Grafos, Universidade Federal da Bahia.
 
KAYE, Richard. Minesweeper is NP-complete. The Mathematical Intelligencer 22.2, 9-15, 2000.

KAYEb, Richard. Some minesweeper configurations. http://www. mat. bham. ac. uk/RW Kaye (2000).
	
KAYE, Richard. How Complicated is Minesweeper? 2003. Disponível em: http://web.mat.bham.ac.uk/R.W.Kaye/minesw/ASE2003.pdf. Acesso em: 22 nov. 2020.
RITT, Marcus. Algoritmos e complexidade: notas de aula. N/d: N/d, 2011. (N/D). Disponível em: http://arquivoescolar.org/bitstream/arquivo-e/103/1/algoritmos.pdf Acesso em: 20 nov. 2020.
SCOTT, Allan, Ulrike Stege, and Iris Van Rooij. Minesweeper may not be NP-complete but is hard nonetheless. The Mathematical Intelligencer 33.4 (2011): 5-17. 

STEWART, Ian. Million-Dollar Minesweeper: ian stewart explains how a computer game can make you rich. Scientific American: Mathematical Recreations. N/d, p. 94-95. 01 out. 2000.
TANG, Yimin, TIAN Jiang, and Yanpeng Hu. A Minesweeper Solver Using Logic Inference, CSP and Sampling. arXiv preprint arXiv:1810.03151, 2018.

YOUNG, Andrew; FOWLER, Andrew. Minesweeper: A statistical and computational analysis. 2004.
