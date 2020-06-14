<h1 align="center">Evolução molecular computacional</h1>
<br>
<p align="center">Evolução molecular por meio de simulações computacionais</p>
<br>
<div align="center">
  <img src="./image/logo/biotechnology1.jpg" alt="BioTech" width="120">
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
  <img src="./image/logo/diagram.png" alt="BioTech" height="425" width="660">
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


<h2 align="center">PARAMETERS</h2>
<strong>QUANTITY OF MOLECULES:</strong><br>
<code>quantity_molecules = 500</code>
<br><br>
<strong>MOLECULES SIZE:</strong><br>
<code>size_molecule = 50</code>
<br><br>
<strong>MUTATION RATE(%):</strong><br>
<code>alpha = 10</code>
<br><br>
<strong>FILTER EFFICIENCY(%):</strong><br>
<code>beta = 20</code>
<br><br>
<strong>TARGET:</strong><br>
<code>target = 5</code>
<br><br>
<strong>CYCLES LIMIT:</strong><br>
<code>cycles_limit = 3</code>
<br><br>
<strong>MOLECULES LIMIT:</strong><br>
<code>molecules_limit = 500</code>
<br>

<br>
  <h2 align="center">CLASS AND FUNCTIONS:</h2>
<br>
  <h3 align="center">PRIMARY CLASS AND FUNCTIONS:</h3>
<br>


<strong>Class Selex:</strong><br>
Onde estão as funções referentes a amplificação, mutação e seleção de moléculas.<br>
<strong>Parameters:</strong> <code>Selex(quantity_molecules, size_molecule, target)</code>
<br><br>
<strong>Function PolymeraseChainReaction:</strong><br>
Onde acontece a replicação das moléculas com probabilidade de mutação.<br>
<strong>Parameters:</strong> <code>Selex().PolymeraseChainReaction(alpha)</code>
<br><br>
<strong>Function ConstantPopulation:</strong><br>
Limita a quantidade de moléculas.<br>
<strong>Parameters:</strong> <code>Selex().ConstantPopulation(molecules_limit)</code>
<br><br>
<strong>Function Filter:</strong><br>
Elimina moléculas não afim com base na eficiencia do filtro.<br>
<strong>Parameters:</strong> <code>Selex().Filter(beta)</code>

<br>
  <h3 align="center">SECUNDARY CLASS AND FUNCTIONS:</h3>
<br>

<strong>Class Tools:</strong><br>
Onde estão armazenadas funções para analise ou métodos abstraidos.
<br><br>
<strong>Function RandomBase:</strong><br>
Retorna sequencia de bases aleatórias de acordo com a quantidade pedida.<br>
<strong>Parameters:</strong> <code>Tools().RandomBase(amount)</code>
<br><br>
<strong>Function Affinity:</strong><br>
Retorna o precentual de afinidade do clico com base nas moleculas.<br>
<strong>Parameters:</strong> <code>Tools().Affinity(target, molecules)</code>
<br><br>
<strong>Function AverageSize:</strong><br>
Retorna o tamanho médio de todas as moléculas.<br>
<strong>Parameters:</strong> <code>Tools().AverageSize(molecules)</code>
<br>

<br>
  <h2 align="center">RESULTS:</h2>
<br>

<h2 align="center">VARIAÇÃO DE MUTAÇÃO:</h2>
<table>
  <tr>
    <td>
      <div align="center">
        <strong>ALPHA: 0% | BETA: 20%</strong>
        <img src="./image/graphic1_results/image1_alpha00_beta_20.png" alt="BioTech" height="200" width="400">
      </div>
    </td>
    <td>
      <div align="center">
        <strong>ALPHA: 0% | BETA: 20%</strong>
        <img src="./image/graphic1_results/image1_alpha05_beta_20.png" height="200" width="400">
      </div>
    </td>
  </tr>
  <tr>
    <td>
      <div align="center">
        <strong>ALPHA: 0% | BETA: 20%</strong>
        <img src="./image/graphic1_results/image1_alpha00_beta_20.png" alt="BioTech" height="200" width="400">
      </div>
    </td>
  </tr>
  <tr>
    <td>
      <div align="center">
        <strong>ALPHA: 0% | BETA: 20%</strong>
        <img src="./image/graphic1_results/image1_alpha00_beta_20.png" alt="BioTech" height="200" width="400">
      </div>
    </td>
  </tr>
</table>



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


