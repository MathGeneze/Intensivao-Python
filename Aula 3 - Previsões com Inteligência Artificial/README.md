# Projeto - Previsões com Inteligência Artificial | Intensivão de Python

<!--------------- 📍 Introdução -------------->
## 📍 Introdução
> Este Projeto foi feito durante a 3° aula da **Jornada Python Hashtag**, onde fomos contratados por um banco com o objetivo de definir o Score de Crédito dos clientes. Iremos criar um modelo de IA para que ele consiga ler as informações dos clientes e dizer qual o Score dele.  
&nbsp;

<!----------- 📁 Sumário ---------->
## 📁 Sumário
- [▶︎ Explicação do Projeto](#explicação-do-projeto)
- [▶︎ Estrutura do Projeto](#estrutura-do-projeto)
- [▶︎ Requisitos](#requisitos)

&nbsp;

<!--------------- 🌐 Explicação do Projeto -------------->
## <a id="explicação-do-projeto">🌐 Explicação do Projeto</a>
> Temos informações de clientes de um banco (ex: profissão, salário, n° de contas...) e precisamos criar um modelo de IA que consiga analisar todas as informações do cliente e diga qual é a nota de crédito dele (Score do cliente), pode estar entre Bom, Ok ou Ruim.

⚑  Vamos separar a lógica do nosso programa em 5 passos:

* Passo 1: **Importar** a Base de Dados.

* Passo 2: Preparar a Base de Dados.
    * Limpeza de Dados.
    * Separar a Base de Dados para o modelo de IA.

* Passo 3: **Criar o modelo de IA**.

* Passo 4: Criando a previsão e Escolhendo o melhor modelo.

* Passo 5: Fazendo novas previões.
> Para este projeto, usaremos duas Biblioteca:
  * `pandas` - Manipulação de dados dos clientes;
  * `scikit-learn` - Criação de modelos de Inteligência Artificial;

&nbsp;

<!--------------- 📄 Estrutura do Projeto -------------->
## <a id="estrutura-do-projeto">📄 Estrutura do Projeto</a>
> - `inicial.ipynb` - **Script principal** do projeto.
> - `clientes.csv` - Contém os dados dos clientes que serão utilizados para **alimentar o modelo de IA**.
> - `novos_clientes` - Contém os dados dos clientes que utilizaremos para ter **novas previões** após a criação do modelo.

&nbsp;

<!--------------- 🖥️ Requisitos -------------->
## <a id="requisitos">🖥️ Requisitos</a>
* Ter um editor de código instalado (Ex: **VsCode, PyCharm**).

* Ter o **Python** instalado e atualizado até pelo menos a `versão 3.10`.

* **Instale** as bibliotecas  `scikit-learn` e `pandas` pelo terminal através do comando `pip install scikit-learn pandas`.

* **Instale** a extensão **Jupyter** para utilizar os arquivos `ipynb`.

&nbsp;

