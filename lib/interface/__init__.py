from os import system
from msvcrt import getch
from sys import stdout
from time import sleep


def leiaInt(msg):
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            print('Digite uma opção valida!')
            continue
        else:
            return n

def linha(tam=40):
    return '='*tam


def cabeçalho(txt):
    print(linha())
    print(txt.center(40))
    print(linha())


def menu(titulo, lista):
    cabeçalho(titulo)
    c = 1
    for item in lista:
        print(f'{c} - {item}')
        c += 1
    print(linha())
    opc = leiaInt('Sua opção: ')
    return opc


def limpa_tela():
    system('cls')#melhorar para verificar qual sistema operacional


def tecla_seguir():
    print('Pressione qualquer tecla...')
    getch()

# Função do efeito de pergaminho
def pergaminho(texto, atraso=0.03):
    for letra in texto:
        stdout.write(letra)
        stdout.flush()
        sleep(atraso)
    print()
    sleep(0.5) # Pequena pausa dramática após a frase

        
       
