<h1 align="center">Evolução molecular computacional</h1>
<br>
<p align="center">Evolução molecular por meio de simulações computacionais</p>
<br>
<div align="center">
  <img src="./assets/image/biotechnology1.jpg" alt="BioTech" width="120">
</div>
<br>

<p align="center">
  <a href="https://opensource.org/licenses/MIT">
    <img src="https://img.shields.io/badge/License-MIT-blue.svg" alt="License MIT">
  </a>
</p>
<hr size="5"/>
<br>
<br>

<h1 align="center">CASE 1:</h1>
<br>

<h2 align="center">DIAGRAM</h2>
<br>

<div align="center">
  <img src="./assets/image/diagram.png" alt="BioTech" height="425" width="660">
</div>

<hr size="5"/>


<br>
  <h2 align="center">STEPS:</h2>
<br>

 1. As moléculas são geradas com base no tamanho e quantidade solicitada.
 2. As moléculas são replicadas, podendo conter uma probabilidade de mutação entre sua estrutura molecular.
 3. As moléculas são deletadas aleatóreamente de forma que não prejudique na analise.
 4. As moléculas são filtradas de forma que moléculas não adaptadas tenham uma probabilidade de morrer.
 5. As moléculas voltam para o passo de replicação.
<hr size="5"/>
<br>


<h2 align="center">PARAMETERS:</h2>
**QUANTITY OF MOLECULES**<br>
`quantity_molecules = 500`
<br>
**MOLECULES SIZE**<br>
`size_molecule = 50`
<br>
**MUTATION RATE(%)**<br>
`alpha = 10`
<br>
**FILTER EFFICIENCY(%)**<br>
`beta = 20`
<br>
**TARGET**<br>
`target = 5`
<br>
**CYCLES LIMIT**<br>
`cycles_limit = 3`
<br>
**MOLECULES LIMIT**<br>
`molecules_limit = 500`
<br>

<br>
  <h2 align="center">CLASS AND FUNCTIONS:</h2>
<br>
<br>
  <h3 align="center">PRIMARY CLASS AND FUNCTIONS:</h3>
<br>


<strong>Class Selex:</trong>
 - Onde estão as funções referentes a amplificação, mutação e seleção de moléculas.
 - **Parameters**:
 - `Selex(**quantity_molecules**, **size_molecule**, **target**)`

<br>
**Function PolymeraseChainReaction**:<br>
Onde acontece a replicação das moléculas com probabilidade de mutação.
**Parameters**: `Selex().PolymeraseChainReaction(**alpha**)`
<br>
**Function ConstantPopulation**:<br>
Limita a quantidade de moléculas.
**Parameters**: `Selex().ConstantPopulation(**molecules_limit**)`

**Function Filter**:<br>
Elimina moléculas não afim com base na eficiencia do filtro.
**Parameters**: `Selex().Filter(**beta**)`
<br>
<br>
  <h3 align="center">SECUNDARY CLASS AND FUNCTIONS:</h3>
<br>

**Class Tools**:
Onde estão armazenadas funções para analise ou métodos abstraidos.
<br>
**Function RandomBase:**
Retorna sequencia de bases aleatórias de acordo com a quantidade pedida.
**Parameters**: `Tools().RandomBase(**amount**)`
<br> 
**Function Affinity**:
Retorna o precentual de afinidade do clico com base nas moleculas.
**Parameters**: `Tools().Affinity(**target**, **molecules**)`
<br>
**Function AverageSize**:
Retorna o tamanho médio de todas as moléculas.
**Parameters**: `Tools().AverageSize(**molecules**)`
<br>

<br>
  <h2 align="center">RESULTS:</h2>
<br>

<table>
  <tr>
    <td>1</td>
    <td>2</td>
  </tr>
  <tr>
    <td>3</td>
    <td>4</td>
  </tr>
</table>

<h2 align="center">VARIAÇÃO DE MUTAÇÃO:</h2>

Teste 1.0 - (Alfa: 0% / Beta: 20%)

Teste 1.1 - (Alfa: 5% / Beta: 20%)

Teste 1.2 - (Alfa: 15% / Beta: 20%)

Teste 1.3 - (Alfa: 20% / Beta: 20%)

Teste 1.4 - (Alfa: 5% / Beta: 0% a 100%)

<h2 align="center">VARIAÇÃO DE EFICIÊNCIA DE FILTRO:</h2>

Teste 1.5 - (Alfa: 5% / Beta: 0%)

Teste 1.6 - (Alfa: 5% / Beta: 10%)

Teste 1.7 - (Alfa: 5% / Beta: 50%)

Teste 1.8 - (Alfa: 5% / Beta: 80%)

Teste 1.9 - (Alfa: 5% / Beta: 90%)

Teste 1.10 - (Alfa: 0% a 100% / Beta: 20%)


<h2 align="center">CALCULO X SIMULAÇÃO</h2>

Teste 1.11 - (Calculado X Simulado[Alfa: 5% / Beta: 60%])




## License

This project is licensed under the MIT License - see the [LICENSE](https://opensource.org/licenses/MIT) page for details.


