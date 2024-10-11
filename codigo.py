# Passo 1: entrar no sistema da empresa - https://dlp.hashtagtreinamentos.com/python/intensivao/login
# pip install pyautogui
import pyautogui
import time
# pyautogui.write -> escrever um texto
# pyautogui.click -> clicar em algo
# pyautogui.press -> apertar uma tecla
# pyautogui.hotkey -> apertar um atalho de teclado (ctrl, c)

pyautogui.PAUSE = 0.5

# abrir o navegador
# apertar a tecla win
pyautogui.press("win")
pyautogui.write("chrome")
pyautogui.press("enter")

# entrar no link: https://dlp.hashtagtreinamentos.com/python/intensivao/login


# Passo 2: fazer login
pyautogui.write("https://dlp.hashtagtreinamentos.com/python/")
pyautogui.press("enter")

# quero dar uma pausa de 3 segundos
time.sleep(3)

# Passo 3: importar a base de dados


# Passo 4: cadastrar 1 produto


# Passo 5: repetir o processo ate acabar os produtos

