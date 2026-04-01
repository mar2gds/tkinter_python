import pyautogui
from time import sleep
#realizarlogin
pyautogui.click(331,167, duration=1)
pyautogui.press('enter')
sleep(3)
pyautogui.click(962,618, duration=2)
pyautogui.write('maria!123')
pyautogui.press('enter')
sleep(2)
pyautogui.press('enter')

pyautogui.click(638,287, duration=1)

with open('itensaleatorios.txt', 'r') as arquivo:
    for linha in arquivo:
        id_prod = linha.split(',')[0]
        nome = linha.split(',')[1]
        qntd = linha.split(',')[2]
        preco = linha.split(',')[3]


        pyautogui.click(243,214, duration=1)
        pyautogui.write(id_prod)
        pyautogui.click(283,280, duration=1)
        pyautogui.write(nome)
        pyautogui.click(266,345, duration=1)
        pyautogui.write(qntd)
        pyautogui.click(252,410, duration=1)
        pyautogui.write(preco)
        pyautogui.click(252,410, duration=1)
        
        sleep(2)
        pyautogui.press('enter')


