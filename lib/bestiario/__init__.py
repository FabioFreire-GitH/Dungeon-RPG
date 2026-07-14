from copy import deepcopy

_modelos_monstros = {
    'Rato atroz': {
        'nome': 'Rato atroz',
        'vida_max': 30,      # Vida que ele começa no combate
        'vida_atual': 30,    # Vida que vai diminuindo durante o duelo
        'força': 12,         # Força usada na fórmula de ataque
        'defesa': 2,         # Defesa usada para mitigar o dano do herói
        'xp': 15             # Experiência que o herói ganha ao derrotá-lo
    },
    'Aranha gigante': {
        'nome': 'Aranha gigante',
        'vida_max': 40,      
        'vida_atual': 40,    
        'força': 15,         
        'defesa': 3,         
        'xp': 20             
    }
}

def obter_monstro(nome):
    """Retorna uma cópia limpa do monstro para o combate."""
    if nome in _modelos_monstros:
        return deepcopy(_modelos_monstros[nome])
    return None