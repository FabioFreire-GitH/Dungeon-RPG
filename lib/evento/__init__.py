from random import randint, choice
from lib.combate import *
from lib.itens import *

def gerar_evento():
    lista_evento = ['Tesouro', 'Armadilha', 'Monstro']
    #lista_evento = ['Tesouro']
    evento_sorteado = choice(lista_evento) #sorteio com a mesma probabilidade(refletir para as proximas fases)
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
    vida_inimigo = randint(3,5)*10
    nome_monstro = monstro
    print('''
            => Um MONSTRO!!! 
            => A Criatura está Furiosa e pronta para Atacar.
          
            => PREPARE-SE!        
          ''')
    return combate(ficha, vida_inimigo, nome_monstro)