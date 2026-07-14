from os import system
from time import sleep
from msvcrt import getch
from lib.evento import *
from lib.interface import *
from .mapa import dungeon_mapa

'''
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

def explorar_dungeon(ficha):
    current_room_id = 1 # Começamos na sala com ID 1
    while True:
        system('cls')
        # Obter a sala atual do mapa
        sala_atual = dungeon_mapa[current_room_id]
        
        if not sala_atual['visitada']: # Se a sala ainda não foi visitada
            pergaminho(f"Ao adentrar o {sala_atual['nome']}, você observa o ambiente...") 
            sleep(0.5)

            evento_sorteado = gerar_evento() # Gera um evento aleatório
            sleep(0.8)

            if evento_sorteado == 'Tesouro':
                # Chama a função de evento de tesouro, passando a ficha e a sala atual
                # evento_tesouro internamente usará sala_atual['itens'] como 'loot_pool' e sala_atual['bonus']
                loot = evento_tesouro(ficha, sala_atual) 
                if loot is not None:
                    guardar_item(ficha, loot) # Guarda o item/tesouro na ficha do jogador

                    print('\nPressione qualquer tecla para ver seu inventário...')
                    getch()
                    mostra_inventario(ficha) # Exibe o inventário atualizado
                    print('\nPressione qualquer tecla para continuar...')
                    getch() # Pausa após mostrar inventário
                else:
                    print('Você procurou, mas não encontrou nada de valor.')
                    tecla_seguir() # Aguarda input para continuar

            elif evento_sorteado == "Armadilha":
                resultado = evento_armadilha(ficha) # Ativa o evento de armadilha
                if not resultado: # Se o jogador morrer na armadilha
                    print('\n==>O Herói MORREU!\n') 
                    tecla_seguir()
                    return False # Retorna False para indicar derrota e encerrar o jogo
                else:
                    print('\nVocê conseguiu escapar da armadilha, mas não ileso!')
                    tecla_seguir() # Aguarda input para continuar

            elif evento_sorteado == "Monstro":
                # Verificamos se há monstros potenciais listados para esta sala
                if sala_atual['monstros'] and sala_atual['monstros'] != ['nada']: # Evita tentar lutar contra 'nada'
                    # Apenas para exibição, escolhe um nome de monstro da lista da sala
                    nome_monstro_display = choice([m for m in sala_atual['monstros'] if m != 'nada']) 
                    print(f"\nVocê encontra um {nome_monstro_display} no caminho!") 
                    resultado = evento_monstro(ficha) # Inicia o combate (evento_monstro usa monstro genérico por enquanto)
                    if not resultado: # Se o jogador morrer no combate
                        print('\n==>O Herói MORREU!\n') 
                        tecla_seguir()
                        return False # Retorna False para indicar derrota e encerrar o jogo
                    else:
                        print(f'\nVocê derrotou o {nome_monstro_display}!')
                        if nome_monstro_display in sala_atual['monstros']:
                            sala_atual['mosntros'].remove(nome_monstro_display)
                            if sala_atual['mosntros'] is None:
                                sala_atual['mosntros'] = 'Nada'
                        tecla_seguir()
                        # Futuramente: Adicionar lógica aqui para remover o monstro derrotado
                        # de `sala_atual['monstros']` para que ele não reapareça.
                else:
                    print('A sala está estranhamente calma... nenhum monstro apareceu.')
                    tecla_seguir()
            else: # Caso o evento sorteado seja 'nada' ou algo inesperado
                print('A sala parece vazia e silenciosa.')
                tecla_seguir()

            # Após o processamento dos eventos da primeira visita, marque a sala como visitada
            sala_atual['visitada'] = True # Marca como visitada para que os eventos não se repitam
        else:
            # Mensagem para salas já visitadas
            print(f"Você retorna ao {sala_atual['nome']}. Parece familiar, você já explorou aqui antes.")
            tecla_seguir()

        # Limpa a tela novamente para o menu de navegação, após os eventos
        system('cls') 
        cabeçalho(f'{sala_atual['nome']}')
        pergaminho(sala_atual['descricao'])
        print("\nPara onde você deseja ir?")
        opcoes_movimento = []
        for direcao, proxima_sala_id in sala_atual['conexoes'].items():
            if proxima_sala_id is not None:
                # Se a sala conectada existir no mapa, mostre o nome dela
                nome_proxima_sala = dungeon_mapa[proxima_sala_id]['nome']
                opcoes_movimento.append(f"{direcao.capitalize()} ({nome_proxima_sala})")
        
        opcoes_movimento.append("Sair da Dungeon")
        escolha_movimento = menu("Escolha seu caminho", opcoes_movimento)

        direcoes_validas = []
        for direcao, proxima_sala_id in sala_atual['conexoes'].items():
            if proxima_sala_id is not None:
                direcoes_validas.append(direcao.capitalize())

        direcao_escolhida = None
        if 1 <= escolha_movimento <= len(direcoes_validas):
            direcao_escolhida = direcoes_validas[escolha_movimento - 1].lower()
            
            proximo_id = sala_atual['conexoes'][direcao_escolhida]
            if proximo_id is not None and proximo_id in dungeon_mapa:
                current_room_id = proximo_id
                print(f"Você se moveu para o {direcao_escolhida}. Entrando em {dungeon_mapa[current_room_id]['nome']}...")
                sleep(1) # Pequena pausa para a transição
            else:
                print("Não há caminho nesta direção. Tente novamente.")
                tecla_seguir()
        elif escolha_movimento == len(opcoes_movimento): # "Sair da Dungeon" é a última opção
            cabeçalho('Saindo da Dungeon...')
            return True # Assume que sair da dungeon é uma "vitória" ou sucesso
        else:
            print("Opção inválida. Digite uma das opções listadas.")
            tecla_seguir()
            continue # Continua o loop para pedir nova entrada


    # Removendo a lógica antiga de geração de eventos por sala 
    #    evento = gerar_evento()
    #    sleep(0.8)
    #    if evento == 'Tesouro':
    #        loot = evento_tesouro(ficha, sala)
    #        if loot is not None:
    #            guardar_item(ficha, loot)
    #        mostra_inventario(ficha)
    #    elif evento == "Armadilha":
    #        resultado = evento_armadilha(ficha)
    #        if not resultado:
    #            print('\n==>O jogador MORREU!\n') 
    #            return False
    #    elif evento == "Monstro":
    #        resultado = evento_monstro(ficha)
    #        if not resultado:
    #            print('\n==>O jogador MORREU!\n') 
    #            return False
    #    print('\nPressione um tecla avançar para a proxima Sala!')
    #    getch()
    #return True

