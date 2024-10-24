<!DOCTYPE html>
<html lang="pt">
<head>
    <meta charset="UTF-8">
    <title>Projeto de Gestão de Eventos</title>
    <style>
        body { font-family: Arial, sans-serif; line-height: 1.6; margin: 20px; }
        pre { background-color: #f4f4f4; padding: 10px; overflow-x: auto; }
        code { background-color: #f4f4f4; padding: 2px 4px; }
        h1, h2, h3 { color: #333; }
        ul { list-style-type: disc; margin-left: 20px; }
        ol { list-style-type: decimal; margin-left: 20px; }
        a { color: #0366d6; text-decoration: none; }
        a:hover { text-decoration: underline; }
    </style>
</head>
<body>

<h1>Projeto de Gestão de Eventos</h1>

<p>Este projeto consiste num sistema para gerir eventos de início e término de visualização de programas por utilizadores, calcular utilizadores ativos por programa e exportar esses dados para um ficheiro CSV. O projeto está organizado em módulos separados e utiliza um ambiente virtual Python para gerir as dependências.</p>

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
    <li><a href="#licenca">Licença</a></li>
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
</ul>

<h2 id="configuracao-do-ambiente">Configuração do Ambiente</h2>

<h3>1. Clonar o Repositório</h3>
<pre><code class="language-bash">git clone https://github.com/o_seu_utilizador/o_seu_repositorio.git
cd o_seu_repositorio
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
    <li>Executar testes unitários e exibir os resultados.</li>
</ul>

<h2 id="execucao-dos-testes">Execução dos Testes</h2>
<p>Os testes unitários estão incluídos no final do ficheiro <code>main.py</code> e serão executados automaticamente quando o programa for executado. Se desejar executar apenas os testes, pode modificar o código conforme necessário.</p>

<h2 id="desativacao-do-ambiente-virtual">Desativação do Ambiente Virtual</h2>
<p>Após concluir o trabalho, desative o ambiente virtual:</p>
<pre><code class="language-bash">deactivate</code></pre>

<h2 id="notas-adicionais">Notas Adicionais</h2>
<ul>
    <li><strong>Dependências Adicionais:</strong>
        <ul>
            <li>Caso precise adicionar novas dependências, instale-as com <code>pip install nome_do_pacote</code> e atualize o <code>requirements.txt</code>:</li>
            <pre><code class="language-bash">pip freeze > requirements.txt</code></pre>
        </ul>
    </li>
    <li><strong>Ficheiro <code>events.tsv</code>:</strong>
        <ul>
            <li>Certifique-se de que o ficheiro <code>events.tsv</code> está no mesmo diretório que <code>main.py</code>.</li>
            <li>O formato esperado é um ficheiro tabular com os campos: <code>show</code>, <code>event</code>, <code>timestamp</code>, <code>user_id</code>, separados por tabulações.</li>
        </ul>
    </li>
    <li><strong>Ambiente Virtual:</strong>
        <ul>
            <li>Recomenda-se o uso do ambiente virtual para evitar conflitos de dependências.</li>
            <li>Não inclua a pasta <code>venv/</code> no controlo de versão. Adicione-a ao <code>.gitignore</code> se necessário.</li>
        </ul>
    </li>
    <li><strong>Atualização das Dependências:</strong>
        <ul>
            <li>Para atualizar as dependências para as versões mais recentes:</li>
            <pre><code class="language-bash">pip install --upgrade -r requirements.txt</code></pre>
        </ul>
    </li>
    <li><strong>Contribuição:</strong>
        <ul>
            <li>Sinta-se à vontade para contribuir para o projeto através de pull requests.</li>
            <li>Para reportar problemas ou sugerir melhorias, abra uma issue no GitHub.</li>
        </ul>
    </li>
    <li><strong>Contacto:</strong>
        <ul>
            <li>Para dúvidas ou suporte, entre em contacto via e-mail: <a href="mailto:o_seu_email@example.com">o_seu_email@example.com</a>.</li>
        </ul>
    </li>
</ul>

<h2 id="licenca">Licença</h2>
<p>Este projeto está licenciado sob os termos da <a href="LICENSE">Licença MIT</a>.</p>

<hr>

<h3>Exemplo de Utilização:</h3>
<p>Após executar <code>python main.py</code>, deverá ver uma saída indicando que os dados foram exportados com sucesso:</p>
<pre><code>Data successfully exported to output.csv
Todos os testes foram concluídos com sucesso.
</code></pre>
<p>O ficheiro <code>output.csv</code> conterá uma tabela com os programas e o número de utilizadores ativos.</p>

</body>
</html>
