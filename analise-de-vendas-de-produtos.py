
"""
**Passo a passo da solução do desafio**"""

# Lógica de programação
# Passo 0 - Entender o desafio que você quer resolver
# Passo 1 - percorrer todos os arquivos da pasta base de dados
import os
import pandas as pd



lista_arquivo = os.listdir("/content/drive/MyDrive/Curso basico de python/Vendas")
display (lista_arquivo)

tabela_total = pd.DataFrame()

# Passo 2 - Importar as bases de dados de vendas
for arquivo in lista_arquivo:
# se tem "vendas" no nome do arquivo entao
  if "Vendas" in arquivo:
#importar o arquivo
    tabela = pd.read_csv(f"/content/drive/MyDrive/Curso basico de python/Vendas/{arquivo}")
    tabela_total = pd.concat([tabela_total, tabela], ignore_index = True)


# Passo 3 - tratar / Compilar as bases de dados
display(tabela_total)

# Passo 4 - Calcular o produto mais venddo (em quantidade)
tabela_produtos = tabela_total.groupby("Produto").sum()
tabela_produtos = tabela_produtos[['Quantidade Vendida']].sort_values(by='Quantidade Vendida', ascending=False)
display(tabela_produtos)

# Passo 5 - Calcular o produto que mais faturou
tabela_total['Faturamento'] = tabela_total['Quantidade Vendida'] * tabela_total['Preco Unitario']

tabela_faturamento = tabela_total.groupby('Produto').sum()
tabela_faturamento = tabela_faturamento[['Faturamento']].sort_values(by='Faturamento', ascending=False)
display(tabela_faturamento)

# passo 6 - Calcular a loja   que mais vendeu em faturamento

tabela_lojas = tabela_total.groupby('Loja').sum()
tabela_lojas = tabela_lojas[['Faturamento']]
display(tabela_lojas)

import plotly.express as px

# grafico
grafico = px.bar(tabela_lojas, x=tabela_lojas.index, y='Faturamento')
grafico.show()