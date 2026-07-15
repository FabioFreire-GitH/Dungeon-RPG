from random import randint, choice
from lib.combate import *
from lib.itens import *
from lib.bestiario import *

def gerar_evento(sala_atual):
    lista_eventos_disponiveis = []

    if sala_atual['monstros'] and sala_atual['monstros'] != ['nada']:
        lista_eventos_disponiveis.append('Monstro')
    
    if sala_atual['armadilha_ativa']: # Só adiciona armadilha se estiver ativa
        lista_eventos_disponiveis.append('Armadilha')
    
    if sala_atual['loots_restantes'] > 0: # Só adiciona tesouro se houver loot
        lista_eventos_disponiveis.append('Tesouro')
    
    # Se, por algum motivo, não houver nenhum evento, sempre oferecemos "Nada"
    if not lista_eventos_disponiveis:
        lista_eventos_disponiveis.append('Nada') # Garante que sempre haja uma opção

    evento_sorteado = choice(lista_eventos_disponiveis)
    return evento_sorteado


def evento_tesouro(ficha,sala):#evento_tesouro(ficha,sala) - upgrade
    print('Você se depara com objetos interessantes!')
    op = input('Deseja procurar algo? [s/n] ').strip().lower()
    if op == 's':
        busca = randint(1,100)
        if busca <= 60:
            loot = gerar_loot(sala)
            return loot
        else:
            bonus_pericia = 15
            loot = gerar_loot(sala, bonus_pericia)
            return loot
    else:
        return None     
    
    

def evento_armadilha(ficha):
    dano = randint(1,2)*10
    ficha['vida'] -= dano
    print(f'''
            => Uma ARMADILHA!!!
            => O Mecânismo Dispara:
        
            => Você sofreu {dano} de Dano.
          ''')
    if ficha['vida'] <= 0:
        return False
    else:
        return True


def evento_monstro(ficha, monstro):
    dados_monstro = obter_monstro(monstro)
    print('''
            => Um MONSTRO!!! 
            => A Criatura está Furiosa e pronta para Atacar.
          
            => PREPARE-SE!        
          ''')
    return combate(ficha, dados_monstro)