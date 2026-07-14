# lib/dungeon/mapa.py
dungeon_mapa = {
    1: {  # ID 1 como chave principal
        'id': 1,
        'nome': 'Corredor escuro', 
        'descricao': 'Um corredor úmido e escuro, com teias de aranha balançando no teto.',
        'conexoes': {
            'norte': 2,
            'sul': None,
            'leste': 3,
            'oeste': None
        },
        'itens': ['moedas', 'arma', 'armadura', 'nada'],
        'monstros': ['Rato atroz', 'Aranha', 'nada'],
        'visitada': False,
        'bonus': -10 
    },
    2: {  # ID 2 como chave principal
        'id': 2,
        'nome': 'Deposito Velho',
        'descricao': 'Um deposito velho escuro e abandonado, com entulhos empoeirados e sujos.',
        'conexoes': {
            'norte': None,
            'sul': 1,
            'leste': None,
            'oeste': None
        },
        'itens': ['moedas', 'objetos valiosos', 'cura', 'nada'],
        'monstros': ['Rato atroz', 'Aranha', 'nada'],
        'visitada': False,
        'bonus': 0
    },
    3: {  # ID 3 como chave principal
        'id': 3,
        'nome': 'Cela',
        'descricao': 'Uma cela vazia e úmida, com esqueleto, sujeira e um fedor insuportável.',
        'conexoes': {
            'norte': None,
            'sul': None,
            'leste': None,
            'oeste': 1
        },
        'itens': ['moedas', 'arma', 'nada'],
        'monstros': ['Rato atroz', 'Aranha', 'nada'],
        'visitada': False,
        'bonus': -20
    }
}