<h1 align="center">Caso 2:</h1>
<br>
<p>Neste cenário teve o incremento de duas novas variaves, sendo elas, chance de quebra e junção de uma molécula.
A intenção é ver como as moléculas irão se comportar a partir desta situação.</p>

<h2 align="center">INFORMAÇÕES:</h2>

 - 500 MOLÉCULAS INICIAS

 - 50 BASES CADA MOLÉCULA(Tamanho inicial)

 - 100 CICLOS

CP [Apaga 50% das moléculas aleatoriamente]

AFF(Afinidade) [Contém tamanho de 5 bases (sequência aleatória)]
(Tamanho do filtro = 5)

EFICIÊNCIA DE FILTRO (Beta): 20% 
(Percentual de uma moléculas não-afim morrer)

TAXA DE MUTAÇÃO (Alfa): 5% (Inicialmente)
(Percentual de erro que cada base pode ter.)

QUEBRA:
Se encontrar "TTT" a molécula quebra e remove este pedaço.

JUNÇÃO:
Gera uma sequência de tamanho 5 para ter base.
Se encontrar uma outra molécula que tenha o encaixe dessa sequência, elas se juntam.

<br>
<h1 align="center">ANALISES</h1>

<h2 align="center">VARIAÇÃO DE MUTAÇÃO:</h2>

Teste 1.0 - (Alfa: 0% / Beta: 20%)

Teste 1.1 - (Alfa: 5% / Beta: 20%)

Teste 1.2 - (Alfa: 10% / Beta: 20%)


<h2 align="center">VARIAÇÃO DE EFICIÊNCIA DE FILTRO:</h2>

Teste 1.5 - (Alfa: 5% / Beta: 20%)

Teste 1.6 - (Alfa: 5% / Beta: 40%)

Teste 1.9 - (Alfa: 5% / Beta: 90%)
