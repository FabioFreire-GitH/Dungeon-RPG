from os import system
from time import sleep
from msvcrt import getch
from lib.evento import *


def gerar_cenario():
    # 1. Dungeon Abandonada - Tema: ruínas, decadência, saque. // 2. Catacumbas - Tema: mortos, ossos, relicários. // 3. Fortaleza Inimiga - Tema: militar. // 
    # 4. Templo Antigo - Tema: sagrado/místico. // 5. Mina Profunda - Tema: exploração e minerais.
    cenarios = {
            'Dungeon Abandonada': { 
            'salas': {
            'Corredor Escuro': {
                'loot': ['arma','armadura','nada'] , 'bonus': -90},
            'Sala Comum': {
                'loot': ['moedas','objetos valiosos','arma', 'cura', 'nada'], 'bonus': -30},
            'Deposito Velho': {
                'loot': ['objetos valiosos','armadura','nada'], 'bonus': -10},
            'Cela': {
                'loot': ['moedas','nada'], 'bonus': -20},
            'Alojamento': {
                'loot': ['moedas','objetos valiosos', 'cura', 'nada'], 'bonus': -10},
            'Refeitório': {
                'loot': ['moedas','objetos valiosos','cura' ,'nada'], 'bonus': -10},
            'Sala de Guarda': {
                'loot': ['arma','armadura','nada'], 'bonus': -20},
            'Arsenal': {
                'loot': ['arma','armadura','nada'], 'bonus': 0},
            'Câmara Selada': {
                'loot': ['moedas','objetos valiosos','nada'], 'bonus': 10},
            'Cofre Antigo': {
                'loot': ['moedas','objetos valiosos','arma','armadura','nada'], 'bonus': 20}}
            },
            'Catacumbas': {
            'salas': {
                'Cripta': {
                    'loot': ['moedas','joias', 'gemas', 'armadura', 'nada'], 'bonus': -30},
                'Capela': {
                    'loot': ['moedas', 'joias','cura' ,'nada'], 'bonus': 0},
                'Altar': {
                    'loot': ['moedas','joias','cura' ,'nada'], 'bonus': 20},
                'Galeria de Ossos': {
                    'loot': ['moedas','joias', 'nada', 'armadura'], 'bonus': -10},
                'Sala dos Relicários': {
                    'loot': ['joias','artefatos', 'nada','arma'], 'bonus': 10},
                'Câmara dos Sacrifícios': {
                    'loot': ['joias', 'gemas', 'nada','arma'], 'bonus': -30},
                'Túmulo Esquecido': {
                    'loot': ['moedas','joias', 'gemas', 'nada', 'armadura'], 'bonus': 0},
                'Câmara dos Segredos': {
                    'loot': ['joias','artefatos', 'arma', 'cura','nada'], 'bonus' : 20},
                'Câmara do Lich': {
                    'loot': ['moedas','joias','artefatos', 'arma',  'nada'], 'bonus': 15},
                'Mausoléu': {
                    'loot': ['moedas','joias', 'gemas',  'nada'], 'bonus': 10}}
                }
    }
    nome_cenario = choice(list(cenarios.keys()))
    cenario = cenarios[nome_cenario]
    return nome_cenario, cenario # retorna um tupla com o nome do cenario e o dicionario do cenario


def gerar_sala(cenario):
    nome_sala = choice(list(cenario['salas'].keys())) 
    sala = cenario['salas'][nome_sala]
    return nome_sala, sala
'''
testei no main
cen = gerar_cenario()
print (cen[1])
sala = gerar_sala(cen[1])
print()
print(sala)
'''

def explorar_dungeon(ficha):
    nome_cenario, cenario = gerar_cenario() # gera o cenario e retorna o nome e o dicionario do cenario - desempacotando a tupla
    for c in range(10):
        system('cls')
        nome_sala, sala = gerar_sala(cenario) # gera a sala e retorna o nome e o dicionario da sala - desempacotando a tupla
        cabeçalho(f'{nome_cenario} sala {c+1}: {nome_sala}')
        print('\nPressione um tecla para entrar!')
        getch()
        evento = gerar_evento()
        sleep(0.8)
        if evento == 'Tesouro':
            loot = evento_tesouro(ficha, sala)
            if loot is not None:
                guardar_item(ficha, loot)
            mostra_inventario(ficha)
        elif evento == "Armadilha":
            resultado = evento_armadilha(ficha)
            if not resultado:
                print('\n==>O jogador MORREU!\n') 
                return False
        elif evento == "Monstro":
            resultado = evento_monstro(ficha)
            if not resultado:
                print('\n==>O jogador MORREU!\n') 
                return False
        print('\nPressione um tecla avançar para a proxima Sala!')
        getch()
    return True


# ============================================
# FASE 2.2 — CONTEXTO DE SALAS
#
# OBJETIVO:
# Criar um sistema de ambientes para influenciar
# loot, raridade e eventos da dungeon.
#
# PLANO:
#
# [ ] Criar gerar_sala()
#     -> sorteia tipo de ambiente
#
# [ ] Cada sala deve definir:
#     - nome
#     - categorias de tesouro
#     - bonus de raridade
#     - eventos possíveis
#
# Estrutura sugerida:
#
# sala = {
#     'nome': 'Aposento',
#     'categorias': ['Joias', 'Objetos Valiosos'],
#     'bonus_raridade': 10
# }
#
# Fluxo futuro:
#
# explorar_dungeon()
#     -> gerar_sala()
#     -> gerar_evento()
#     -> gerar_tesouro(sala['categorias'], sala['bonus_raridade'])
#
# Expansões futuras:
#
# [ ] Salas secretas
# [ ] Salas de boss
# [ ] Armadilhas especiais
# [ ] NPCs
# [ ] Lojas
# [ ] Altares
# [ ] Eventos únicos
# ============================================
'''
Pequena melhoria de responsabilidade

Hoje:

system('cls')
print(...)
getch()

estão dentro da dungeon.

Funciona.

Mas pense:

isso é lógica de interface.

Não de dungeon.

Dungeon deveria pensar:

sala atual
evento
resultado

Não em:

limpar tela
esperar tecla

Mas isso é aceitável no seu estágio.

Não moveria agora.

Só marca
'''

