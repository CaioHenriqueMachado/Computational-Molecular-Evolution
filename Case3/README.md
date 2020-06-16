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

<h1 align="center">CASE 3</h1>
<br>
<p align="center">NEWS: Neste cenário foi desenvolvido um resevatório onde
as moléculas que morrem nos ciclos vão diretamente para eles.
Nesta experiência, tem um limite de 50.000 bases a serem usadas e não existirá um limitador de moléculas.</p>
<br>
<h2 align="center">DIAGRAM</h2>
<br>

<div align="center">
  <img src="./image/logo/diagram.png" alt="BioTech" height="800" width="660">
</div>

<hr size="5"/>


<br>
  <h2 align="center">STEPS</h2>
<br>

 1. As moléculas são geradas com base no tamanho e quantidade solicitada.
 2. As moléculas são replicadas, podendo conter uma probabilidade de mutação entre sua estrutura molecular.
 3. As moléculas passam por um processo de quebra caso tenham uma seuqência de três bases denominada de 'stop códon'.
 4. As moléculas passam por um processo de junção caso uma tenham uma determinada sequência.
 5. As moléculas são filtradas de forma que moléculas não adaptadas tenham uma probabilidade de morrer.
 6. As moléculas voltam para o passo de replicação.
 7. As moléculas são analisadas base a base medindo o nível de organização entre elas apartir da entropia.
 8. A cada processo onde uma molécula é apagada, suas bases caem no tanque. São criadas novas moléculas se tiver quantidade no tanque.
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
<br><br>
<strong>BREAK:</strong><br>
<code>condon_break = 'TTT'</code><br>
<code>prob_break = 10</code>
<br><br>
<strong>JOIN:</strong><br>
<code>prob_join = 5</code>
<br>

<br>
  <h2 align="center">CLASS AND FUNCTIONS</h2>
<br>
  <h3 align="center">PRIMARY CLASS AND FUNCTIONS</h3>
<br>

<strong>Class Selex:</strong><br>
Onde estão as funções referentes a amplificação, mutação e seleção de moléculas.<br>
<strong>Parameters:</strong> <code>Selex(quantity_molecules, size_molecule, target)</code>
<br><br>
<strong>Function PolymeraseChainReaction:</strong><br>
Onde acontece a replicação das moléculas com probabilidade de mutação.<br>
<strong>Parameters:</strong> <code>Selex().PolymeraseChainReaction(alpha)</code>
<br><br>
<strong>Function Filter:</strong><br>
Elimina moléculas não afim com base na eficiencia do filtro.<br>
<strong>Parameters:</strong> <code>Selex().Filter(beta)</code>
<br><br>
<strong>Function Break:</strong><br>
Onde acontece a quebra de moléculas com base no Stop Códon 'TTT'.<br>
<strong>Parameters:</strong> <code>Selex().Break(codon_break, prob_break)</code>
<br><br>
<strong>Function Join:</strong><br>
Onde acontece a junção das moléculas que juntas tenha um par especifico de sequência e com uma probabilidade de ocorrer essa junção.<br>
<strong>Parameters:</strong> <code>Selex().Join(prob_join)</code>

<br>
  <h3 align="center">SECUNDARY CLASS AND FUNCTIONS</h3>
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
  <h3 align="center">CLASS AND FUNCTIONS FOR ANALYSIS</h3>
<br>

<strong>Class ShannonEntropy:</strong><br>
Onde são analisadas as moléculas base á base para medir a entropia.
<br><br>
<strong>Function Result:</strong><br>
Retorna a entropia com base nas moléculas.<br>
<strong>Parameters:</strong> <code>ShannonEntropy().Result(molecules)</code>
<br><br><br>




<br>
  <h2 align="center">RESULTS</h2>
<br>

<h2 align="center">CHANGE RATE VARIATION</h2>
<table>
  <tr>
    <td>
      <div align="center">
        <strong>ALPHA: 01% | BETA: 10%</strong>
        <img src="./image/graphic1_results/image1_alpha01_beta_10.png" alt="Mutation Rate Alpha 01 Beta 10" height="450" width="800">
      </div>
    </td>
  </tr>
  <tr>
    <td>
      <div align="center">
        <strong>ALPHA: 02% | BETA: 10%</strong>
        <img src="./image/graphic1_results/image2_alpha02_beta_10.png" alt="Mutation Rate Alpha 02 Beta 10" height="450" width="800">
      </div>
    </td>
  </tr>
  <tr>
    <td>
      <div align="center">
        <strong>ALPHA: 05% | BETA: 10%</strong>
        <img src="./image/graphic1_results/image3_alpha05_beta_10.png" alt="Mutation Rate Alpha 05 Beta 10" height="450" width="800">
      </div>
    </td>
  </tr>
  <tr>
    <td>
      <div align="center">
        <strong>ALPHA: 10% | BETA: 10%</strong>
        <img src="./image/graphic1_results/image4_alpha10_beta_10.png" alt="Mutation Rate Alpha 10 Beta 10" height="450" width="800">
      </div>
    </td>
  </tr>
</table>


## License

This project is licensed under the MIT License - see the [LICENSE](https://opensource.org/licenses/MIT) page for details.


