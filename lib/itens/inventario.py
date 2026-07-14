from lib.interface import *


def mostra_inventario(ficha):
    print()
    cabeçalho('INVENTÁRIO')
    if len(ficha['inventario']) == 0:
        print('Mocilha Vazia!')
        return False
    else:
        c = 1
        for item in ficha['inventario']:
            print(f'{c} - {item["nome"]}', end=' ')
            if item['tipo'] in ('cura','armadura','arma'):
                print(f'(+{item["efeito"]:>20})')
            elif item['tipo'] in ('joias','gemas','objetos valiosos','artefatos'):
                print(f' - Valor: ({item["valor_final"]:>20})')
            c += 1
        print(linha())
        opc = leiaInt('Escolha um item para Usar (0 para voltar): ')
        if opc == 0:
            return False
        elif 1 <= opc <= len(ficha['inventario']):
            item = ficha['inventario'][opc - 1]
            if item['tipo'] in ('arma','armadura'):
                return equipar_item(ficha, item)
            elif item['tipo'] == 'cura':
                return usar_item_cura(ficha, item)
            else:
                print('Este item não pode ser usado.')
                return False
        else:
            print('Opção inválida!')
            return False
    print(linha())


def guardar_item(ficha, loot):
    if loot is None:
        return
    if loot['tipo'] == 'moedas':
        ficha['ouro'] += loot['valor_final']
        print(f'Um(a) {loot["nome"]} com {loot["quantidade"]} de {loot["tipo"]} foi adicionado ao Valor do seu Ouro!')
    else:
        ficha['inventario'].append(loot)
        print(f'{loot["tipo"]}: {loot["nome"]} foi adicionado ao seu Inventário!')


def remover_item(ficha, item):
    ficha['inventario'].remove(item)


def usar_item_cura(ficha, item):
    if item['tipo'] == 'cura':
        op = input(f'Deseja usar o Item ({item["nome"]})? [s/n]')
        
        if op == 's':
            ficha['vida'] += item['efeito']
            remover_item(ficha,item)
            print(f'Você usou {item["nome"]} e recuperou {item["efeito"]} de Vida!')
            return True
        else:
            print('Item não usado!')
            return False
    else:
        print('Não é possivel usar este item!')
        return False


def mostra_equipamentos(ficha):
    cabeçalho('EQUIPAMENTOS')
    arma = ficha['equipamento']['arma']
    armadura = ficha['equipamento']['armadura']
    if arma is not None:
        print(f'Arma     : {arma["nome"]}', end=' ')
        print(f'(+{arma["efeito"]} Força)')
    else:
        print('(Arma     : Nenhuma arma equipada)')
    if armadura is not None:
        print(f'Armadura : {armadura["nome"]}', end=' ')
        print(f'(+{armadura["efeito"]} Defesa)')
    else:
        print('(Armadura : Nenhuma armadura equipada)')
    print(linha())


def equipar_item(ficha, item):
    if ficha['equipamento']['arma'] is not None and item['tipo'] == 'arma':
        print(f'Você já tem uma arma equipada: {ficha["equipamento"]["arma"]}. Deseja substituir? (s/n)')
        resposta = input().lower()
        
        if resposta == 's':
            arma_antiga = ficha['equipamento']['arma']
            ficha['força'] -= arma_antiga['efeito']  # Remove o bônus da arma equipada
            guardar_item(ficha, arma_antiga)  # Guarda a arma antiga no inventário
            remover_item(ficha, item)  # Remove a nova arma do inventário
            
            ficha['equipamento']['arma'] = item
            ficha['força'] += item['efeito']  # Adiciona o bônus da nova arma
            print(f'Você equipou a {item["nome"]} e ganhou {item["efeito"]} de Força!')
            return True
        else:
            print('Equipamento não alterado.')
            return False
    elif ficha['equipamento']['armadura'] is not None and item['tipo'] == 'armadura':
        print(f'Você já tem uma armadura equipada: {ficha["equipamento"]["armadura"]}. Deseja substituir? (s/n)')
        resposta = input().lower()
        
        if resposta == 's':
            armadura_antiga = ficha['equipamento']['armadura']
            ficha['defesa'] -= armadura_antiga['efeito']  # Remove o bônus da armadura equipada
            guardar_item(ficha, armadura_antiga) #Guarda a armadura antiga
            remover_item(ficha, item) #remove o item novo do inventario
            
            ficha['equipamento']['armadura'] = item
            ficha['defesa'] += item['efeito']  # Adiciona o bônus da nova armadura
            print(f'Você equipou a {item["nome"]} e ganhou {item["efeito"]} de Defesa!')
            return True

        else:
            print('Equipamento não alterado.')
            return False
    else:
        if item['tipo'] == 'arma':
            remover_item(ficha, item)
            ficha['equipamento']['arma'] = item
            ficha['força'] += item['efeito']
            print(f'Você equipou a {item["nome"]} e ganhou {item["efeito"]} de Força!')
            return True
        
        elif item['tipo'] == 'armadura':
            remover_item(ficha, item)
            ficha['equipamento']['armadura'] = item
            ficha['defesa'] += item['efeito']
            print(f'Você equipou a {item["nome"]} e ganhou {item["efeito"]} de Defesa!')
            return True
