# lib/dungeon/sala.py

# Exemplo de estrutura de dicionário para representar uma sala da dungeon
sala_exemplo = {
    'id': 1,  # Identificador único da sala
    'nome': 'nome da sala',
    'descricao': 'Um corredor úmido e escuro, com teias de aranha balançando no teto.',
    'conexoes': {
        'norte': 2,  # ID da sala conectada ao norte
        'sul': None, # Nenhuma conexão ao sul
        'leste': 3,  # ID da sala conectada ao leste
        'oeste': None # Nenhuma conexão ao oeste
    },
    'itens': [],     # Lista de itens encontrados na sala (inicialmente vazia ou com itens predefinidos)
    'monstros': [],  # Lista de monstros presentes na sala (inicialmente vazia ou com monstros predefinidos)
    'visitada': False, # Indica se a sala já foi visitada pelo jogador
    'bonus': -10 # raridade do item (modificador de raridade)
}
