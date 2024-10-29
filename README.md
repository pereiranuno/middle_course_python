<!DOCTYPE html>
<html lang="pt">
<head>

</head>
<body>

<h1>Projeto de informação de subcrição de utilizadores de um conjunto de programas.</h1>

<p>Este programa permite ler dados de registo de adesão/cancelamento de subscritores de programa Netflix, e calcular os utilizadores ativos por programa, e exportar esses dados para um ficheiro output. O projeto está organizado em módulos separados e utiliza um ambiente virtual Python para gerir as dependências.</p>

<h2>Sumário</h2>
<ul>
    <li><a href="#estrutura-do-projeto">Estrutura do Projeto</a></li>
    <li><a href="#requisitos">Requisitos</a></li>
    <li><a href="#configuracao-do-ambiente">Configuração do Ambiente</a></li>
    <li><a href="#instalacao-das-dependencias">Instalação das Dependências</a></li>
    <li><a href="#execucao-do-programa">Execução do Programa</a></li>
    <li><a href="#execucao-dos-testes">Execução dos Testes</a></li>
    <li><a href="#desativacao-do-ambiente-virtual">Desativação do Ambiente Virtual</a></li>
    <li><a href="#notas-adicionais">Notas Adicionais</a></li>
</ul>

<h2 id="estrutura-do-projeto">Estrutura do Projeto</h2>
<pre><code>meu_projeto/
├── event.py
├── event_manager.py
├── utils.py
├── main.py
├── events.tsv
├── requirements.txt
└── venv/
</code></pre>

<ul>
    <li><strong><code>event.py</code></strong>: Contém a classe <code>Event</code>.</li>
    <li><strong><code>event_manager.py</code></strong>: Contém a classe <code>EventManager</code>.</li>
    <li><strong><code>utils.py</code></strong>: Contém a função <code>convert_tabular_file_content_to_dictionary</code>.</li>
    <li><strong><code>main.py</code></strong>: Ponto de entrada do programa e testes unitários.</li>
    <li><strong><code>events.tsv</code></strong>: Ficheiro de dados contendo os eventos.</li>
    <li><strong><code>requirements.txt</code></strong>: Lista de dependências do projeto.</li>
    <li><strong><code>venv/</code></strong>: Ambiente virtual Python.</li>
</ul>

<h2 id="requisitos">Requisitos</h2>
<ul>
    <li>Python 3.6 ou superior</li>
    <li>Biblioteca <code>pandas</code></li>
    <li>Biblioteca <code>matplotlib</code></li>
</ul>

<h2 id="configuracao-do-ambiente">Configuração do Ambiente</h2>

<h3>1. Clonar o Repositório</h3>
<pre><code class="language-bash">git clone https://github.com/pereiranuno/middle_course_python
cd local_rep
</code></pre>

<h3>2. Criar o Ambiente Virtual</h3>
<pre><code class="language-bash">python3 -m venv venv</code></pre>

<h3>3. Ativar o Ambiente Virtual</h3>
<ul>
    <li><strong>No Linux ou macOS:</strong>
        <pre><code class="language-bash">source venv/bin/activate</code></pre>
    </li>
    <li><strong>No Windows (PowerShell):</strong>
        <pre><code class="language-powershell">.\venv\Scripts\Activate.ps1</code></pre>
    </li>
    <li><strong>No Windows (Command Prompt):</strong>
        <pre><code class="language-cmd">venv\Scripts\activate.bat</code></pre>
    </li>
    <li><strong>No Windows (Git Bash):</strong>
        <pre><code class="language-bash">source venv/Scripts/activate</code></pre>
    </li>
</ul>

<h2 id="instalacao-das-dependencias">Instalação das Dependências</h2>
<p>Com o ambiente virtual ativado, instale as dependências:</p>
<pre><code class="language-bash">pip install -r requirements.txt</code></pre>

<h2 id="execucao-do-programa">Execução do Programa</h2>
<p>Para executar o programa principal:</p>
<pre><code class="language-bash">python main.py</code></pre>
<p>Este comando irá:</p>
<ul>
    <li>Ler os eventos do ficheiro <code>events.tsv</code>.</li>
    <li>Calcular os utilizadores ativos por programa.</li>
    <li>Exportar os dados para um ficheiro <code>output.csv</code>.</li>
    <li>Executar testes unitários e exibir os resultados em gráfico.</li>
</ul>

<h2 id="execucao-dos-testes">Execução dos Testes</h2>
<p>Os testes unitários estão incluídos no final do ficheiro <code>main.py</code> e serão executados automaticamente quando o programa for executado. Se desejar executar apenas os testes, pode modificar o código conforme necessário.</p>

<h2 id="desativacao-do-ambiente-virtual">Desativação do Ambiente Virtual</h2>
<p>Após concluir o trabalho, desative o ambiente virtual:</p>
<pre><code class="language-bash">deactivate</code></pre>

<h2 id="notas-adicionais">Notas Adicionais</h2>
<ul>
    <li><strong>Ficheiro <code>events.tsv</code>:</strong>
        <ul>
            <li>Certifique-se de que o ficheiro <code>events.tsv</code> está no mesmo diretório que <code>main.py</code>.</li>
            <li>O formato esperado é um ficheiro tabular com os campos: <code>show</code>, <code>event</code>, <code>timestamp</code>, <code>user_id</code>, separados por tabulações.</li>
        </ul>
    </li>
    <li><strong>Ambiente Virtual:</strong>
        <ul>
            <li>Recomenda-se o uso do ambiente virtual para evitar conflitos de dependências.</li>
        </ul>
    </li>
    <li><strong>Atualização das Dependências:</strong>
        <ul>
            <li>Para atualizar as dependências para as versões mais recentes:</li>
            <pre><code class="language-bash">pip install --upgrade -r requirements.txt</code></pre>
        </ul>
    </li>
    <li><strong>Contacto:</strong>
        <ul>
            <li>Para dúvidas entre em contacto via e-mail: <a href="mailto:pereiranuno88@gmail.com">pereiranuno88@gmail.com</a>.</li>
        </ul>
    </li>
</ul>



<hr>

<h3>Exemplo de Utilização:</h3>
<p>Após executar <code>python main.py</code>, deverá ver uma saída indicando que os dados foram exportados com sucesso:</p>
<pre><code>Data successfully exported to output.csv
Todos os testes foram concluídos com sucesso.
</code></pre>
<p>O ficheiro <code>output.csv</code> conterá uma tabela com os programas e o número de utilizadores ativos.</p>
</body>
</html>
