<h1>🐍 Estudos em Python 3</h1>

<p>Este repositório reúne diversos **scripts e projetos de estudo em Python 3**, organizados em pastas separadas dentro de uma única estrutura principal.</p>  
<p>Cada diretório contém exemplos, testes e experimentos relacionados a diferentes tópicos da linguagem — desde fundamentos até módulos avançados.</p>
<p>Todo o ambiente é executado dentro de um **container Docker**, garantindo portabilidade, isolamento e facilidade na execução dos códigos.</p>
<p>Cada pasta representa uma área específica de aprendizado e contém scripts independentes.</p>

<h2>🐳 Executando com Docker</h2>

 <h3>1. Clonar o repositório</h3>
<p>git clonehttps://github.com/leonardomarcatti/python.git</p>
<p>cd python</p>


<h3>2. Construir a imagem Docker</h3>
<p>docker build -t python3-studies .</p>

<h3>3. Executar o container</h3>
<p>docker run -it --rm -v $(pwd):/app python3-studies bash</p>

<h3>🧠 Como usar</h3>
<p>python3 caminho/para/o/script.py</p>
<h3>🧩 Requisitos</h3>
<p>Docker instalado</p>
<p>Nenhum outro requisito é necessário — o ambiente é totalmente configurado pelo container.</p>

<h3>💡 Objetivo</h3>

<p>O propósito deste repositório é centralizar e organizar estudos de Python 3, abordando:</p>
<ul>
   <li>Sintaxe e fundamentos da linguagem</li>
   <li>Programação orientada a objetos</li>
   <li>Manipulação de arquivos</li>
   <li>Expressões regulares</li>
   <li>Uso de módulos e pacotes</li>
   <li>Scripts utilitários para automação</li>
</ul>

<h3>🐍 Licença</h3>
<p>Este projeto é de uso livre para fins de estudo e aprendizado.</p>
<p>Sinta-se à vontade para clonar, modificar e contribuir!</p>
