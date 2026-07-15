from copy import deepcopy

_modelos_monstros = {
    'Rato atroz': {
        'nome': 'Rato atroz',
        'vida_max': 20,      # Vida que ele começa no combate
        'vida_atual': 20,    # Vida que vai diminuindo durante o duelo
        'força': 8,          # Força usada na fórmula de ataque
        'defesa': 1,         # Defesa usada para mitigar o dano do herói
        'xp': 15,             # Experiência que o herói ganha ao derrotá-lo
        'respawnable': True
    },
    'Aranha gigante': {
        'nome': 'Aranha gigante',
        'vida_max': 40,      
        'vida_atual': 40,    
        'força': 15,         
        'defesa': 3,         
        'xp': 20,
        'respawnable': False             
    },
    'Goblin Ladrão': {
        'nome': 'Goblin Ladrão',
        'vida_max': 35,      
        'vida_atual': 35,    
        'força': 14,         
        'defesa': 3,         
        'xp': 18,
        'respawnable': False             
    },
    'Zumbi Decrépito': {
        'nome': 'Zumbi Decrépito',
        'vida_max': 50,      
        'vida_atual': 50,    
        'força': 10,         
        'defesa': 5,         
        'xp': 25,
        'respawnable': False             
    },
    'Morcego da Caverna': {
        'nome': 'Morcego da Caverna',
        'vida_max': 25,      
        'vida_atual': 25, 
        'força': 10,         
        'defesa': 1,         
        'xp': 12,
        'respawnable': True             
    }
}

def obter_monstro(nome):
    """Retorna uma cópia limpa do monstro para o combate."""
    if nome in _modelos_monstros:
        return deepcopy(_modelos_monstros[nome])
    return None