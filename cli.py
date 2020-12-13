#!/usr/bin/python

from sys import argv

from utils import clrscr

# Constantes
T_ARGS= len(argv) # Total de argumentos.
ARGS = argv # Argumentos ingresados.

debug = True

def betainfo(msg):
    if debug:
        print(msg)

def test():
    clrscr()
    argumentos = argv
    print('Cantidad de argumentos:', len(argumentos))
    for i, argumento in enumerate(argumentos):
        print(f'4rgum3nt0 {i}:', argumento)

def menu():
    print("Willkommen мой друг")
    input("Type something: ")


def main():
    # Comandos reconocidos / valid arguments.
    betainfo('main')
    if T_ARGS == 1:
        betainfo('one argument')
        print("Libreta")
    elif len(argv) > 1:
        betainfo('more than one argument')
        if argv[1] == 'menu':
            betainfo('recognized argument')
            if argv[1] in v_args:
                v_args[1]
        else:
            print("Unrecognized yet:", argv[1])
    

if __name__ == "__main__":    
    main()
    #test()