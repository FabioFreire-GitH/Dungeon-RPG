from random import choice, randint

ref_tesouros = ['moedas','joias','artefatos', 'gemas', 'objetos valiosos']
ref_itens = ['cura','arma','armadura']


def gerar_item(tipo_item, bonus_sala=0):
    if tipo_item == 'cura':
        tipo_cura = ['Poção pequena','Poção média']
        nome_item = choice(tipo_cura)
    elif tipo_item == 'arma':
        tipo_arma = ['Adaga','Espada','Machado']
        nome_item = choice(tipo_arma)
    elif tipo_item == 'armadura':
        tipo_armadura = ['Couro leve','Cota de Malha']
        nome_item = choice(tipo_armadura)
    else:
        return None
    raridade = gerar_raridade(bonus_sala)
    efeito = gerar_bonus_item(nome_item, tipo_item, raridade)
    item = {'nome': nome_item,'tipo': tipo_item, 'efeito': efeito, 'raridade': raridade}
    return item


def gerar_bonus_item(nome_item, tipo_item, raridade):
    multiplicador = {'Baixa':0.7, 'Comum': 1.0, 'Raro': 1.3, 'Épico': 1.7, 'Lendário': 2.2 }
    if tipo_item == 'cura':
        if nome_item == 'Poção pequena':
            bonus = 20
        elif nome_item == 'Poção média':
            bonus = 40
    elif tipo_item == 'arma':
        if nome_item == 'Adaga':
            bonus = 5
        elif nome_item == 'Espada':
            bonus = 10
        elif nome_item == 'Machado':
            bonus = 15
    elif tipo_item == 'armadura':
        if nome_item == 'Couro leve':
            bonus = 3
        elif nome_item == 'Cota de Malha':
            bonus = 7
    bonus_final = int(bonus * multiplicador[raridade])
    return bonus_final


def gerar_raridade(bonus=0):
    pesos = {
        'Baixa': 40,
        'Comum': 30,
        'Raro': 20,
        'Épico': 8,
        'Lendário': 2
    }
    # reduz pesos ruins
    perda_baixa = int(pesos['Baixa'] * bonus / 100)
    perda_comum = int(pesos['Comum'] * bonus / 100)

    pesos['Baixa'] -= perda_baixa
    pesos['Comum'] -= perda_comum

    bonus_total = perda_baixa + perda_comum

    # redistribui nos bons
    pesos['Raro'] += int(bonus_total * 0.5)
    pesos['Épico'] += int(bonus_total * 0.3)
    pesos['Lendário'] += int(bonus_total * 0.2)

    raridade = randint(1, 100)
    
    limite1 = pesos['Baixa']
    limite2 = limite1 + pesos['Comum']
    limite3 = limite2 + pesos['Raro']
    limite4 = limite3 + pesos['Épico']

    if raridade <= limite1:
        return 'Baixa'
    elif raridade <= limite2:
        return 'Comum'
    elif raridade <= limite3:
        return 'Raro'
    elif raridade <= limite4:
        return 'Épico'
    else:
        return 'Lendário'


def gerar_tesouro(tipo_tesouro, bonus_sala=0):
    multiplicador = {'Baixa':0.7, 'Comum': 1.0, 'Raro': 1.8, 'Épico': 2.6, 'Lendário': 4.0 }
    familia = tipo_tesouro
    qtd = 1 # caso nao seja moedas - este é a quantidade padrão para os demais objetos
    if familia == 'moedas':
        moeda = ['Punhado','Bolsa', 'Sacola']
        nome_tesouro = choice(moeda)
        valor_base = 5
        if nome_tesouro == 'Punhado':
            qtd = randint(2,7)
        elif nome_tesouro == 'Bolsa':
            qtd = randint(5,20)
        elif nome_tesouro == 'Sacola':
            qtd = randint(15,30)
    elif familia == 'joias':
        joia = {'Anel':30, 'Colar':60,'Bracelete':50, 'Broche':40, 'Tiara':80}
        nome_tesouro = choice(list(joia.keys()))
        valor_base = joia[nome_tesouro]
    elif familia == 'artefatos':
        artefato = {'Estatueta':100, 'Ídolo':180, 'Cálice':220, 'Cetro':300, 'Orbe':450}
        nome_tesouro = choice(list(artefato.keys()))
        valor_base = artefato[nome_tesouro]
    elif familia == 'gemas':
        gema = {'Quartzo':25,'Ametista':60,'Safira':120,'Rubi':180,'Esmeralda':250}
        nome_tesouro = choice(list(gema.keys()))
        valor_base = gema[nome_tesouro]
    elif familia == 'objetos valiosos':
        objeto = {'Tapeçaria':80, 'Pintura':110, 'Livro Antigo': 140, 'Castiçal de Prata': 90, 'Porcelana Rara': 130}
        nome_tesouro = choice(list(objeto.keys()))
        valor_base = objeto[nome_tesouro]
    else: 
        return None
    raridade = gerar_raridade(bonus_sala)
    valor_final = qtd * int(valor_base*multiplicador[raridade])
    tesouro = {'nome': nome_tesouro,'tipo': familia, 'valor_base': valor_base, 'quantidade': qtd,'raridade': raridade, 'valor_final': valor_final}
    return tesouro


def gerar_loot(sala, bonus_pericia=0):# controla o loot por sala
    sorteio_loot = choice(sala['itens'])
    if sorteio_loot == 'nada':
        print('Nada encontrado nesta sala.')
        return None
    elif sorteio_loot in ref_tesouros:
        tesouro = gerar_tesouro(sorteio_loot, sala['bonus']+bonus_pericia)
        print(f'Você encontrou um(a) {tesouro["nome"]} de {tesouro["tipo"]} com raridade {tesouro["raridade"]} e valor final de {tesouro["valor_final"]}!')
        return tesouro
    elif sorteio_loot in ref_itens:
        item = gerar_item(sorteio_loot, sala['bonus']+bonus_pericia)
        print(f'Você encontrou um(a) {item["nome"]} de {item["tipo"]} com raridade {item["raridade"]} e com bônus de efeito {item["efeito"]}!')
        return item

