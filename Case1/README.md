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
<strong>QUANTITY OF MOLECULES</strong>
<code>quantity_molecules = 500</code>
<br>
<strong>MOLECULES SIZE</strong>
<code>size_molecule = 50</code>
<br>
<strong>MUTATION RATE(%)</strong>
<code>alpha = 10</code>
<br>
<strong>FILTER EFFICIENCY(%)</strong>
<code>beta = 20</code>
<br>
<strong>TARGET</strong>
<code>target = 5</code>
<br>
<strong>CYCLES LIMIT</strong>
<code>cycles_limit = 3</code>
<br>
<strong>MOLECULES LIMIT</strong>
<code>molecules_limit = 500</code>
<br>

<br>
  <h2 align="center">CLASS AND FUNCTIONS:</h2>
<br>
<br>
  <h3 align="center">PRIMARY CLASS AND FUNCTIONS:</h3>
<br>


<h4>Class Selex:</h4>
Onde estão as funções referentes a amplificação, mutação e seleção de moléculas.
<h5>Parameters: Selex(quantity_molecules, size_molecule, target)</h5>
<br>
<h4>Function PolymeraseChainReaction:</h4>
Onde acontece a replicação das moléculas com probabilidade de mutação.
<h5>Parameters: Selex().PolymeraseChainReaction(alpha)</h5>
<br>
<h4>Function ConstantPopulation:</h4>
Limita a quantidade de moléculas.
<h5>Parameters: Selex().ConstantPopulation(molecules_limit)</h5>
<br>
<h4>Function Filter:</h4>
Elimina moléculas não afim com base na eficiencia do filtro.
<h5>Parameters: Selex().Filter(beta)</h5>
<br>

<br>
  <h3 align="center">SECUNDARY CLASS AND FUNCTIONS:</h3>
<br>

<h4>Class Tools:</h4>
Onde estão armazenadas funções para analise ou métodos abstraidos.
<br>
<h4>Function RandomBase:</h4>
Retorna sequencia de bases aleatórias de acordo com a quantidade pedida.
<h5>Parameters: `Tools().RandomBase(amount)`
<br> 
<h4>Function Affinity:</h4>
Retorna o precentual de afinidade do clico com base nas moleculas.
<h5>Parameters: `Tools().Affinity(target, molecules)`
<br>
<h4>Function AverageSize:</h4>
Retorna o tamanho médio de todas as moléculas.
<h5>Parameters: `Tools().AverageSize(molecules)`
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


