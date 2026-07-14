from time import sleep
from random import randint
from msvcrt import getch
from lib.interface import *
from lib.itens import *


def combate(ficha, vida_inimigo, nome_monstro):
    pergaminho(f"⚔️ O duelo começou! Você enfrenta o temível {nome_monstro}! ⚔️\n")
    while ficha['vida'] > 0 and vida_inimigo > 0:
        pergaminho('\n===>Seu Turno! Escolha uma Opção:')
        if ficha["equipamento"]["arma"] is None:
            print(f'1. Ataque (com os punhos)')
        else:
            print(f'1. Ataque ({ficha["equipamento"]["arma"]})')
        print(f'2. Curar ()')# verificar invenrario e suar item.
        op = input('Digite 1 ou 2: ')
        print(linha())
        #Turno Heroi
        if op == '1':
            ataq_heroi = ficha['força'] + randint(1,4)*10
            vida_inimigo -= ataq_heroi
            pergaminho(f'Você avança e golpeia! Causa {ataq_heroi} de dano no {nome_monstro}.')
        elif op == '2':
            item_usado = mostra_inventario(ficha)
            if not item_usado:
                continue # Volta para o início do turno do herói!
        else:
            pergaminho('Você hesitou e perdeu a chance de atacar!')

        if vida_inimigo<=0:
            break
    
        #Turno NPC
        pergaminho(f'\n==> Turno do {nome_monstro}...')
        ataq_inimigo = randint(0, 3)*10 - ficha['defesa']
        ficha['vida'] -= max(0, ataq_inimigo)
        pergaminho(f' O {nome_monstro} contra-ataca e te causa {max(0, ataq_inimigo)} de dano!')

        #status turno
        print(linha())
        pergaminho(f' STATUS ATUAL | Seu HP: {max(0, ficha["vida"])} | HP do {nome_monstro}: {max(0, vida_inimigo)}')
        print(linha())
    #resultado
    if ficha['vida'] > 0:
        resultado = f'VITÓRIA! Você derrotou o {nome_monstro} e sobreviveu ao duelo!'
        cabeçalho(resultado)
        return True
    else:
        resultado = f'DERROTA... O {nome_monstro} foi implacável. Você caiu em combate.'
        cabeçalho(pergaminho(resultado))
        return False
    


 