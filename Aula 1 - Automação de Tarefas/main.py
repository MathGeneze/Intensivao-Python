# Passo 1: Entrar no sistema da empresa - https://dlp.hashtagtreinamentos.com/python/intensivao/login

import pyautogui as py
from time import sleep

    # Definindo 1 segundo para cada ação
py.PAUSE = 0.8

    # Entrando no google
py.press('win')
py.write('chrome')
py.press('enter')

    # Opcional: Clica no 1° perfil
sleep(1)
py.press('tab')
py.press('enter')

    # Criando uma aba e Entrando no site
py.hotkey('ctrl', 't')
py.write('https://dlp.hashtagtreinamentos.com/python/intensivao/login')
py.press('enter')


# Passo 2: Fazer login
sleep(3)

    # Inserindo o email
py.press('tab')
py.write('python.teste@gmail.com')

    # Inserindo a senha
py.press('tab')
py.write('123456789')

    # Clicando em login
py.press('tab')
py.press('enter')

sleep(3)


# Passo 3: Importar a Base de Dados
import pandas

tabela = pandas.read_csv('produtos.csv')

# Passo 4: Cadastrando os produtos

py.PAUSE = 0.3

for linha in tabela.index:
    
    py.click(x=765, y=327)
    codigo = tabela.loc[linha, 'codigo']
    py.write(codigo)
    
    py.press('tab')  # Passa pro próximo campo
    marca = tabela.loc[linha, 'marca']
    py.write(marca)
    
    py.press('tab')  
    tipo = tabela.loc[linha, 'tipo']
    py.write(tipo)
    
    py.press('tab')  
    categoria = str(tabela.loc[linha, 'categoria'])
    py.write(categoria)
    
    py.press('tab')  
    preco_unitario = str(tabela.loc[linha, 'preco_unitario'])
    py.write(preco_unitario)
    
    py.press('tab')  
    custo = str(tabela.loc[linha, 'custo'])
    py.write(custo)
    
    py.press('tab')  
    
    obs = str(tabela.loc[linha, 'obs'])
    if obs != 'nan':
        py.write(obs)

        # Enviando os dados 
    py.press('tab')    
    py.press('enter')

        # Indo para o topo da página 
    py.hotkey('ctrl', 'shift', 'home')