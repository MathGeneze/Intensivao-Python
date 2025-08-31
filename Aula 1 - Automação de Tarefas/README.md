# Aula 1 - Automação de Tarefas | Intensivão de Python

<!--------------- 📌 Introdução -------------->
## 📌 Introdução
> Este Projeto foi feito durante a 1° aula da **Jornada Python Hashtag**, onde nos foi ensinado a como utilizar o Python para automatizar processos que levariam muitas horas em situações do dia-a-dia na rotina empresarial.     

&nbsp;

<!----------- Sumário ---------->
## 📒 Sumário
- [▶︎ Explicação do Projeto](#explicação-do-projeto)
- [▶︎ Estrutura do Projeto](#estrutura-do-projeto)
- [▶︎ Requisitos](#requisitos)
- [▶︎ Observações](#observações)

&nbsp;

<!--------------- ♻️ Explicação do Projeto -------------->
## <a id="explicação-do-projeto">♻️ Explicação do Projeto</a>
> Temos informações de quase **300 produtos** (ex: *Nome do produto*, *Marca*, *Preço* ... ) em uma planilha e precisamos cadastrá-los no site da empresa diáriamente para fazer um relatório. O objetivo deste projeto é simples: Tornar este processo completamente automático usando Python.
> 
> ⚑ O processo se baseia em: **Entrar no site da empresa  *⮕*  fazer login  *⮕*  Cadastrar os produtos**.
> 
> Para fazer isso de maneira automática, usaremos duas Biblioteca: 
  * `pyautogui` - Controla os movimentos do Mouse e do Teclado;
  * `pandas` - Manipulação de dados dos produtos.

&nbsp;

<!--------------- 🗂️ Estrutura do Projeto -------------->
## <a id="estrutura-do-projeto">🗂️ Estrutura do Projeto</a>
> - `main.py` - Scrpit principal do projeto.
> - `produtos.csv` - Contém os dados que serão utilizados no projeto.

&nbsp;

<!--------------- ⚙️ Requisitos -------------->
## <a id="requisitos">⚙️ Requisitos</a>
* Ter um editor de código instalado (Ex: **VsCode, PyCharm, Jupiter Notebook**).
  
* Ter o **Python** instalado e atualizado até pelo menos a `versão 3.10`.
* **Instale** as bibliotecas  `pyautogui` e `pandas` pelo terminal através do comando `pip install pyautogui pandas`.
* Ter o navegador **Google Chrome** instalado.

&nbsp;

<!--------------- ⚠️ Observações -------------->
## <a id="observações">⚠️ Observações</a>
- ❗ O site da empresa não **armazena nenhum dado**, ele foi criado especialmente para a aula e a área de login pode ser preenchida com qualquer informação.

- ‼️ Este programa foi feito com a especificação de caso o usuário tiver **mais de 1 perfil** no Google.

- Caso você tenha apenas 1 perfil, entre no arquivo `main.py` e apague o trecho de código da `linha 14` até a `linha 17`.

- Para **encerrar a automação**, basta arrastar o cursor no **canto superior esquerdo** da tela.



  
