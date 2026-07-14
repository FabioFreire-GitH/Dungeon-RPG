from os import system
from time import sleep
from lib.interface import *
from lib.jogo import*


#Programa Principal
while True:
    limpa_tela()
    resposta = menu('DUNGEON RPG: MENU PRINCIPAL',['Novo Jogo','Sair'])
    if resposta == 1:
        limpa_tela()
        cabeçalho('CRIAR PERSONAGEM')
        ficha = criar_personagem()
        hud_jogo(ficha)
    elif resposta == 2:
        cabeçalho('SAINDO DO JOGO...')
        break
    else:
        limpa_tela()
        cabeçalho('Digite um opção Valida!')
        sleep(2) 


