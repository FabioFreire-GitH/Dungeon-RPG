from msvcrt import getch
from lib.interface import *
from lib.itens import *
from lib.dungeon.mapa import *

def criar_personagem():
    ficha = dict()
    while True:
        nome = input('Nome do Heroí: ').strip()
        if nome.replace(' ', '').isalpha():  # verifica se cada string substituido os espaços são do tipo alfabeticos (aqui nao esta atribuindo o nome com o reclace a nenhuma variavel)   
            ficha['nome'] = nome
            ficha['força'] = 10
            ficha['defesa'] = 5
            ficha['vida'] = 100
            ficha['ouro'] = 0
            ficha['inventario'] = []
            ficha['equipamento'] = {'arma': None, 'armadura': None}
            ficha['mapa'] = gerar_dungeon_mapa()
            ficha['nivel_atual'] = 1
            ficha['xp_atual'] = 0
            ficha['xp_prox_nivel'] = 100
            ficha['nivel_max'] = 5
            ficha['buff_forca_temp'] = 0
            ficha['buff_defesa_temp'] = 0
            print(f'\nHeroi {ficha["nome"]} Criado!')
            print('\nPressione qualque tecla para continuar...')
            getch()
            return ficha
        else:
            print('Digite um nome valido!')


def mostra_status(ficha):
    print()
    cabeçalho('STATUS DO HERÓI')

    print(f'Nome   : {ficha["nome"]}')
    print(f'Vida   : {ficha["vida"]}')
    print(f'Ouro   : {ficha["ouro"]}')
    print(linha())

    print(f'Força  : {ficha["força"]}')
    print(f'Defesa : {ficha["defesa"]}')
    print(linha())

    print(f"Nivel  : {ficha['nivel_atual']} / {ficha['nivel_max']} máx.")
    print(f"XP     : {ficha['xp_atual']} / {ficha['xp_prox_nivel']} Up.")
    print(linha())
    
def subir_nivel(ficha):
    ficha['nivel_atual'] += 1
    ficha['xp_atual'] -= ficha['xp_prox_nivel']  # Sobra de XP acumula para o próximo nível
    ficha['xp_prox_nivel'] = int(ficha['xp_prox_nivel'] * 1.5)  # Aumenta a dificuldade do próximo nível
            
    # Bônus de Atributos por Level Up (Evolução)
    ficha['vida'] = 100  # Cura completamente
    ficha['força'] += 3
    ficha['defesa'] += 2




