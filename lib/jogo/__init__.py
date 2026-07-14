from os import system
from msvcrt import getch
from lib.dungeon import *
from lib.personagem import *
from lib.itens import *
from lib.interface import *


def hud_jogo(ficha):
    while True:
        limpa_tela()
        resposta = menu('MENU DO JOGADOR', ['Explorar Dungeon', 'Vericar Status','Lista de Inventário','Lista Equipamentos' , 'Sair'])
        if resposta == 1:
            resultado_final = explorar_dungeon(ficha)
            verifica_vitoria(ficha, resultado_final)
            print('Pressione qualquer tecla...')
            getch()
            #break
        elif resposta == 2:
            mostra_status(ficha)
            print('Pressione qualquer tecla...')
            getch()
        elif resposta == 3:
            mostra_inventario(ficha)
            print('Pressione qualquer tecla...')
            getch()
        elif resposta == 4:
            mostra_equipamentos(ficha)
            print('Pressione qualquer tecla...')
            getch()
        elif resposta == 5:
            break
        else:
            print('Digite uma opção Válida')


def verifica_vitoria(ficha, status):
    if status:
        print('VITÓRIA!!! O Heroi Sobreviveu!')
        print(f'O ouro acumulado foi {ficha["ouro"]} Ouro')
    else:
        print('DERROTA!!! Tente na proxima!')


            
        