
# instalar pyautogui
#importar pyautogui

import pyautogui
import time 



pyautogui.PAUSE = 0.5

#Abrir o navegador
pyautogui.press("win")
pyautogui.write("navegador opera")
pyautogui.press("enter")

#entrar no link https://dlp.hashtagtreinamentos.com/python/intensivao/login
pyautogui.write("https://dlp.hashtagtreinamentos.com/python/intensivao/login")
pyautogui.press("enter")

time.sleep(3)

#fazer login no sistema
pyautogui.click(x=736, y=403)  
pyautogui.hotkey("ctrl", "a")
pyautogui.write("emailteste@gmail.com")

#digitar a senha
pyautogui.press("tab")
pyautogui.write("minha senha")
pyautogui.click(x=795, y=507)

# fazer login
pyautogui.click(x=1023, y=565)
pyautogui.press("enter")

# remover salvar
pyautogui.click(x=1832, y=140)
pyautogui.press("enter")

time.sleep(3)

# importar base de dados

import pandas

tabela = pandas.read_csv("produtos.csv")

print(tabela)


for linha in tabela.index:    
    # cadastrar produto 
    # codigo
    pyautogui.click(x=780, y=289)  

    codigo =str(tabela.loc[linha, "codigo"])
    pyautogui.write(codigo)    
    
    # marca
    marca =str(tabela.loc[linha, "marca"])
    pyautogui.press("tab")
    pyautogui.write(marca)
    
    # tipo
    tipo =str(tabela.loc[linha, "tipo"])
    pyautogui.press("tab")
    pyautogui.write(tipo)
    
    # categoria
    categoria =str(tabela.loc[linha, "categoria"])
    pyautogui.press("tab")
    pyautogui.write(categoria)
    
    # preco unitario
    preco =str(tabela.loc[linha, "preco_unitario"])
    pyautogui.press("tab")   
    pyautogui.write(preco)
    
    # custo
    custo =str(tabela.loc[linha, "custo"])
    pyautogui.press("tab")
    pyautogui.write(custo)
    
    # obs
    obs =str(tabela.loc[linha, "obs"])
    pyautogui.press("tab")
    if obs != "nan":
        pyautogui.write(obs)
       
    #enviar
    pyautogui.press("tab")
    pyautogui.press("enter")
    
    # voltar top
    pyautogui.scroll(5000)

# repetir para todos os produtos


