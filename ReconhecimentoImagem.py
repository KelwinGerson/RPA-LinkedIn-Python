#Bibliotecas utilizadas
from ast import Break
import pyautogui
import Site
from time import sleep
from pyautogui import click, moveTo, typewrite, doubleClick, displayMousePosition
from User import User,Password

Site

#IMAGENS
Bt_SignIn = ('Imagens/SignIn.PNG')
MeProfile = ('Imagens/Me.PNG')
Perfil = ('Imagens/Profile.PNG')
DownChat = ('Imagens/DownChat.PNG')
Bt_Refresh = ('Imagens/Refresh.PNG')
Bt_Net = ('Imagens/Networking.PNG')
#Bt_Connect = ('Imagens/Connect.PNG')

Bt_Connect = (822,564)
Bt_Connect2 = (1026,570)
Bt_Connect3 = (1217,569)
Bt_Connect4 = (1405,569)


#SIGN IN
click(Bt_SignIn)
sleep(1)

#CREDENCIAIS
typewrite(User)
pyautogui.press('tab')
typewrite(Password)
pyautogui.press('enter')
sleep(4)

#NETWORKING
click(Bt_Net)
sleep(4)

#CONECTANDO
click(Bt_Connect)
click(Bt_Connect2)
click(Bt_Connect3)
click(Bt_Connect4)


# COMO RODAR PROCESSOS AUTOMATICAMENTE