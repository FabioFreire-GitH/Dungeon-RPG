from time import sleep
from random import randint
from msvcrt import getch
from lib.interface import *
from lib.itens import *


def combate(ficha, vida_inimigo):
    pergaminho(f"⚔️ O duelo começou! Você enfrenta o temível npc_nome! ⚔️\n")
    while ficha['vida'] > 0 and vida_inimigo > 0:
        pergaminho('\n===>Seu Turno! Escolha uma Opção:')
        print(f'1. Ataque ({ficha["equipamento"]["arma"]})')
        print(f'2. Curar ()')# verificar invenrario e suar item.
        op = input('Digite 1 ou 2: ')
        print(linha())
        #Turno Heroi
        if op == '1':
            ataq_heroi = ficha['força'] + randint(1,4)*10
            vida_inimigo -= ataq_heroi
            pergaminho(f'Você avança e golpeia! Causa {ataq_heroi} de dano no NPC.')
        elif op == '2':
            mostra_inventario(ficha)
        else:
            pergaminho('Você hesitou e perdeu a chance de atacar!')

        if vida_inimigo<=0:
            break
    
        #Turno NPC
        pergaminho(f'\n==> Turno do npc_nome...')
        ataq_inimigo = randint(0, 3)*10 - ficha['defesa']
        ficha['vida'] -= max(0, ataq_inimigo)
        pergaminho(f' O NPC contra-ataca e te causa {max(0, ataq_inimigo)} de dano!')

        #status turno
        print(linha())
        pergaminho(f' STATUS ATUAL | Seu HP: {max(0, ficha["vida"])} | HP do NPC: {max(0, vida_inimigo)}')
        print(linha())
    #resultado
    if ficha['vida'] > 0:
        resultado = f'VITÓRIA! Você derrotou o NPC e sobreviveu ao duelo!'
        cabeçalho(resultado)
        return True
    else:
        resultado = f'DERROTA... O NPC foi implacável. Você caiu em combate.'
        cabeçalho(pergaminho(resultado))
        return False
    


 