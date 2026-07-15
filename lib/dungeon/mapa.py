# lib/dungeon/mapa.py
def gerar_dungeon_mapa():
    dungeon_mapa = {
        1: {  # Corredor escuro - Ponto de partida / Hub
            'id': 1,
            'nome': 'Corredor Escuro', 
            'descricao': 'Um corredor úmido e escuro, com teias de aranha balançando no teto. Parece ser um ponto central de acesso a outras áreas.',
            'conexoes': {
                'norte': 2,        # Deposito Velho
                'sul': 4,          # Sala Comum
                'leste': 3,        # Cela
                'oeste': 5         # Alojamento
            },
            'itens': ['moedas', 'arma', 'armadura', 'cura', 'nada'],
            'monstros': ['Rato atroz', 'Morcego da Caverna', 'nada'],
            'intro_vista': False,
            'armadilha_ativa': True,
            'loots_restantes': 1, 
            'bonus': -10 
        },
        2: {  # Deposito Velho
            'id': 2,
            'nome': 'Depósito Velho',
            'descricao': 'Um depósito velho e empoeirado, com caixas e barris empilhados. Cheira a mofo e abandono.',
            'conexoes': {
                'norte': None,
                'sul': 1,          # Corredor Escuro
                'leste': 6,        # Refeitório
                'oeste': None
            },
            'itens': ['objetos valiosos', 'armadura', 'cura','buff_defesa', 'nada'],
            'monstros': ['Rato atroz', 'Aranha gigante', 'nada'],
            'intro_vista': False,
            'armadilha_ativa': True,
            'loots_restantes': 3, 
            'bonus': 0
        },
        3: {  # Cela
            'id': 3,
            'nome': 'Cela Úmida',
            'descricao': 'Uma cela pequena e úmida, com grades enferrujadas e um catre quebrado. Sinais de ocupação recente, mas vazia agora.',
            'conexoes': {
                'norte': 7,        # Sala de Guarda
                'sul': None,
                'leste': None,
                'oeste': 1          # Corredor Escuro
            },
            'itens': ['moedas', 'nada'],
            'monstros': ['Rato atroz', 'Goblin Ladrão', 'nada'],
            'intro_vista': False,
            'armadilha_ativa': True,
            'loots_restantes': 2, 
            'bonus': -20
        },
        4: {  # Sala Comum
            'id': 4,
            'nome': 'Sala Comum',
            'descricao': 'Uma sala simples e vazia, com alguns destroços de móveis antigos espalhados pelo chão. Pouco resta de valor aqui.',
            'conexoes': {
                'norte': 1,        # Corredor Escuro
                'sul': None,
                'leste': None,
                'oeste': None
            },
            'itens': ['moedas', 'objetos valiosos', 'arma', 'buff_forca', 'nada'],
            'monstros': ['Aranha gigante', 'Goblin Ladrão', 'nada'],
            'intro_vista': False,
            'armadilha_ativa': True,
            'loots_restantes': 2, 
            'bonus': -30
        },
        5: {  # Alojamento
            'id': 5,
            'nome': 'Alojamento dos Servos',
            'descricao': 'Quartos pequenos e empoeirados onde os antigos servos descansavam. Poucos pertences restaram após o saque.',
            'conexoes': {
                'norte': None,
                'sul': None,
                'leste': 1,        # Corredor Escuro
                'oeste': None
            },
            'itens': ['moedas', 'objetos valiosos', 'cura','nada'],
            'monstros': ['Rato atroz', 'Morcego da Caverna', 'nada'],
            'intro_vista': False,
            'armadilha_ativa': True,
            'loots_restantes': 2, 
            'bonus': -10
        },
        6: {  # Refeitório
            'id': 6,
            'nome': 'Refeitório Quebrado',
            'descricao': 'O que sobrou de um grande refeitório, agora cheio de mesas e bancos destruídos. O fedor de decomposição é forte.',
            'conexoes': {
                'norte': None,
                'sul': 8,          # Arsenal
                'leste': None,
                'oeste': 2          # Depósito Velho
            },
            'itens': ['moedas', 'objetos valiosos', 'cura', 'nada'],
            'monstros': ['Aranha gigante', 'Zumbi Decrépito', 'nada'],
            'intro_vista': False,
            'armadilha_ativa': True,
            'loots_restantes': 2, 
            'bonus': -10
        },
        7: {  # Sala de Guarda 
            'id': 7,
            'nome': 'Posto de Guarda Abandonado',
            'descricao': 'Um pequeno posto de guarda, com restos de armas quebradas e armaduras enferrujadas. Poucos vigias sobreviveriam aqui.',
            'conexoes': {
                'norte': None,
                'sul': 3,          # Cela Úmida
                'leste': None,
                'oeste': 8          # Arsenal
            },
            'itens': ['arma', 'armadura','buff_forca','buff_defesa', 'nada'],
            'monstros': ['Goblin Ladrão', 'Zumbi Decrépito', 'nada'],
            'intro_vista': False,
            'armadilha_ativa': True,
            'loots_restantes': 2, 
            'bonus': -20
        },
        8: {  # Arsenal - Ponto de Interconexão Central
            'id': 8,
            'nome': 'Arsenal Saqueado',
            'descricao': 'Um antigo arsenal, hoje em ruínas, com estantes vazias. Ainda há uma chance de encontrar algo útil no meio dos escombros.',
            'conexoes': {
                'norte': 6,        # Refeitório Quebrado
                'sul': 9,          # Câmara Selada
                'leste': 7,        # Posto de Guarda Abandonado
                'oeste': None
            },
            'itens': ['arma', 'armadura', 'moedas', 'objetos valiosos', 'nada'],
            'monstros': ['Zumbi Decrépito', 'Goblin Ladrão', 'Aranha gigante'],
            'intro_vista': False,
            'armadilha_ativa': True,
            'loots_restantes': 3, 
            'bonus': 0
        },
        9: {  # Câmara Selada 
            'id': 9,
            'nome': 'Câmara Selada',
            'descricao': 'Uma câmara que parece ter sido lacrada há muito tempo. O ar é pesado e um pressentimento de algo valioso flutua.',
            'conexoes': {
                'norte': 8,        # Arsenal Saqueado
                'sul': None,
                'leste': 10,       # Cofre Antigo
                'oeste': None
            },
            'itens': ['moedas', 'objetos valiosos', 'gemas', 'artefatos', 'nada'],
            'monstros': ['Zumbi Decrépito', 'Aranha gigante'],
            'intro_vista': False,
            'armadilha_ativa': True,
            'loots_restantes': 3, 
            'bonus': 10
        },
        10: { # Cofre Antigo - Recompensa Final
            'id': 10,
            'nome': 'Cofre Antigo',
            'descricao': 'O coração da dungeon. Esta câmara cintila com uma aura de tesouros perdidos. Pode conter os maiores despojos da masmorra.',
            'conexoes': {
                'norte': None,
                'sul': None,
                'leste': None,
                'oeste': 9          # Câmara Selada
            },
            'itens': ['moedas', 'objetos valiosos', 'arma', 'armadura', 'gemas', 'artefatos', 'buff_forca', 'buff_defesa'],
            'monstros': ['Goblin Ladrão', 'Zumbi Decrépito'], # Colocando monstros mais 'fortes'
            'intro_vista': False,
            'armadilha_ativa': True,
            'loots_restantes': 3, 
            'bonus': 20
        }
    }
    
    return dungeon_mapa
