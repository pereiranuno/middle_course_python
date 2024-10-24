Projeto de Gestão de Eventos
Este projeto consiste num sistema para gerir eventos de início e término de visualização de programas por utilizadores, calcular utilizadores ativos por programa e exportar esses dados para um ficheiro CSV. O projeto está organizado em módulos separados e utiliza um ambiente virtual Python para gerir as dependências.

Sumário
Estrutura do Projeto
Requisitos
Configuração do Ambiente
Instalação das Dependências
Execução do Programa
Execução dos Testes
Desativação do Ambiente Virtual
Notas Adicionais
Estrutura do Projeto
csharp
Copiar código
meu_projeto/
├── event.py
├── event_manager.py
├── utils.py
├── main.py
├── events.tsv
├── requirements.txt
└── venv/
event.py: Contém a classe Event.
event_manager.py: Contém a classe EventManager.
utils.py: Contém a função convert_tabular_file_content_to_dictionary.
main.py: Ponto de entrada do programa e testes unitários.
events.tsv: Ficheiro de dados contendo os eventos.
requirements.txt: Lista de dependências do projeto.
venv/: Ambiente virtual Python.
Requisitos
Python 3.6 ou superior
Biblioteca pandas
Configuração do Ambiente
1. Clonar o Repositório
   git clone https://github.com/o_seu_utilizador/o_seu_repositorio.git
cd o_seu_repositorio
