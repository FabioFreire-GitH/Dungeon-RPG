from time import sleep
from random import randint
from msvcrt import getch
from lib.interface import *
from lib.itens import *
from lib.personagem import *


def combate(ficha, monstro):
    pergaminho(f"⚔️ O duelo começou! Você enfrenta o temível {monstro['nome']}! ⚔️\n")
    while ficha['vida'] > 0 and monstro['vida_atual'] > 0:
        # Calcular atributos efetivos no início de CADA TURNO do herói
        forca_efetiva = ficha['força'] + ficha['buff_forca_temp']
        defesa_efetiva = ficha['defesa'] + ficha['buff_defesa_temp'] 
        
        pergaminho('\n===>Seu Turno! Escolha uma Opção:')
        if ficha["equipamento"]["arma"] is None:
            print(f'1. Ataque (com os punhos)')
        else:
            print(f'1. Ataque ({ficha["equipamento"]["arma"]})')
        print(f'2. Abrir Iventário')# verificar invenrario e usar item.
        op = input('Digite 1 ou 2: ')
        print(linha())
        #Turno Heroi
        if op == '1':
            dano = max(1, (forca_efetiva + randint(1, 6)) - monstro['defesa'])
            monstro['vida_atual'] -= dano
            pergaminho(f"Você avança e golpeia! Causa {dano} de dano no {monstro['nome']}.")
        elif op == '2':
            item_usado = mostra_inventario(ficha)
            if not item_usado:
                continue # Volta para o início do turno do herói!
        else:
            pergaminho('Você hesitou e perdeu a chance de atacar!')

        if monstro['vida_atual']<=0:
            break
    
        #Turno NPC
        pergaminho(f"\n==> Turno do {monstro['nome']}...")
        dano_monstro = max(1, (monstro['força'] + randint(1, 6)) - defesa_efetiva)
        ficha['vida'] -= max(0, dano_monstro)
        pergaminho(f" O {monstro['nome']} contra-ataca e te causa {max(0, dano_monstro)} de dano!")

        #status turno
        print(linha())
        pergaminho(f" STATUS ATUAL | Seu HP: {max(0, ficha['vida'])} | HP do {monstro['nome']}: {max(0, monstro['vida_atual'])}")
        print(linha())
        #resultado
    if ficha['vida'] > 0:
        resultado = f"VITÓRIA! Você derrotou o {monstro['nome']} e sobreviveu ao duelo!\n"
        resultado += f"Você ganhou {monstro['xp']} de XP!\n"
        ficha['xp_atual'] += monstro['xp']  # Adiciona o XP em vez de substituir
        
        # Verificar Level Up
        if ficha['xp_atual'] >= ficha['xp_prox_nivel'] and ficha['nivel_atual'] < ficha['nivel_max']:
            subir_nivel(ficha)
            resultado += f"\n🎉 PARABÉNS! Você subiu para o Nível {ficha['nivel_atual']}!\n"
            resultado += f"Sua força e defesa aumentaram, e sua vida foi totalmente restaurada!"
            
        elif ficha['nivel_atual'] == ficha['nivel_max']:
            resultado += f"Você já está no nível máximo ({ficha['nivel_atual']})!"
            
        pergaminho(resultado)
        cabeçalho("FIM DE COMBATE")
        ficha['buff_forca_temp'] = 0
        ficha['buff_defesa_temp'] = 0
        return True
    else:
        resultado = f"DERROTA... O {monstro['nome']} foi implacável. Você caiu em combate."
        pergaminho(resultado)
        cabeçalho("FIM DE COMBATE")
        ficha['buff_forca_temp'] = 0
        ficha['buff_defesa_temp'] = 0
        return False
    


 