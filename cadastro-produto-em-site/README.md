# Automação: Cadastro de produtos em site

## Índice

- [Descrição](#descrição)
- [Demonstração](#demonstração)
- [Funcionalidades](#funcionalidades)
- [Pré-requisitos](#pre-requisitos)
- [Instalação](#instalacao)
- [Utilização](#utilizacao)
- [Estrutura do projeto](#estrutura-do-projeto)
- [Conclusão](conclusao)
- [Contato](contato)

# Descrição

O objetivo desse projeto é demonstrar como automatizar tarefas repetitivas usando Python, economizando tempo e reduzindo a possibilidade de erros humanos. A automação foca no cadastro de produtos em um sistema, utilizando a biblioteca pyautogui para simular ações de teclado e mouse.

Este é um projeto foi desenvolvido como forma de praticar praticar e aplicar conceitos de Python aprendidos durante as Lives [Hashtag](https://hashtagtreinamentos.com "Site da Hashtag").

## Demonstração

![Gif demonstração página](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiKeUdguTS7RkhPfzcsjQRRGkf_2qz3LEoouFBH689P64G2z3VkFP561rmWnbiYIZiRILNTftJgPb5u7r-Oz5sKFVQF9zxYKMXA0DVZSJ_yxqquSjMEgsjKZO4GbTmLYBKkSdrh5x-gjaFWN2m9PB924KWbBOCubVeoNF0MDz_aeyWXvkK0w2uPNqC79Kxq/s16000/Automa%C3%A7%C3%A3o-Cadastrodeprodutosemsite.gif)

## Funcionalidades

- **Leitura de Dados**: Utiliza a biblioteca pandas para importar e visualizar dados de um arquivo CSV (produtos.csv).
- **Automação de Tarefas**: Emprega a biblioteca pyautogui para automatizar o processo de login e cadastro de produtos em um sistema.
- **Controle de Mouse e Teclado**: Comandos como pyautogui.click, pyautogui.write, e pyautogui.press são usados para simular as ações do usuário.
- **Verificação de Dados**: Implementa uma verificação condicional para preencher apenas os campos que possuem informações, garantindo a integridade dos dados.

## Pré-requisitos

- Python 3.x instalado
- Bibliotecas pandas e pyautogui instaladas

## Instalação

- Baixe o projeto em seu computador (clique no botão verde no alto na página "code" e clique em "Download ZIP".
- Descompacte a pasta (use o software de sua preferência 7zip, winrar...).

1. Clone o repositório para o seu ambiente local:

   ```bash
   git clone https://github.com/seu-usuario/nome-do-repositorio.git
   ```

2. Navegue até o diretório do projeto:

   ```bash
   cd nome-do-repositorio
   ```

3. Instale as dependências necessárias:

   ```bash
   pip install -r requirements.txt
   ```

## Utilização

1. Importe os dados :
   Coloque o arquivo produtos.csv na mesma pasta do seu script Python e use o comando pd.read_csv para importar os dados.

   ```bash
   import pandas as pd
   df = pd.read_csv('produtos.csv')
   print(df.head())
   ```

2. Controle do Mouse e Teclado:
   Instale a biblioteca pyautogui e use os comandos básicos para simular ações.

   ```bash
   pip install pyautogui
   ```

3. Automação do Cadastro:
   Utilize um loop para iterar sobre os dados e automatizar o processo de cadastro.

   ```bash
   import pyautogui

   pyautogui.press('win')
   pyautogui.write('chrome')
   pyautogui.click(x=100, y=200)
   ```

## Estrutura do projeto

`main.py`: Script principal contendo a lógica de automação.
`produtos.csv`: Base de dados com os produtos a serem cadastrados.
`pegar_posicao`.py: Script auxiliar para obter a posição do mouse.

## Conclusão

Este projeto demonstra como a automação com Python pode ser uma ferramenta poderosa para otimizar tarefas repetitivas, aumentando a eficiência e minimizando erros. Sinta-se à vontade para adaptar o código para outras aplicações e melhorar sua produtividade no dia a dia.

## Contato

👩‍💻 Patrícia Freitas

📬 brpatyfreitas@gmail.com

 <div><a href="https://www.linkedin.com/in/patyfreitasbr"><img src="https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white" target="_blank"></>
  <a href="https://www.instagram.com/patyfreitasbr"><img src="https://img.shields.io/badge/Instagram-E4405F?style=for-the-badge&logo=instagram&logoColor=white" target="_blank"></></div>
  
<br>

[![NPM](https://img.shields.io/npm/l/react)](https://github.com/patyfreitasbr/projetos-Python/blob/main/cadastro-produto-em-site/LICENSE)
