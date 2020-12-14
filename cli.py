#!/usr/bin/python

from sys import argv

from utils import clrscr

# Constantes
T_ARGS= len(argv) # Total de argumentos.
ARGS = argv # Argumentos ingresados.
DEFAULT_SECTION = 'TODO' # Sección por defecto.

v_args = ['', 'add']


debug = False
libreta = {
            DEFAULT_SECTION : 
            {
                1 : 
                {
                    'text' : 'Hello world!'
                }
            },
            'Pruebas de la semana' :
            {
                1 : 
                {
                    'text' : 'lenguaje'
                }
            },
            'Salidas de hoy' :
            {
                1 : {
                    'text' : 'Ir al Kayak'
                },
                2 : {
                    'text' : 'Ir a la playa'
                }
            },
        }

def betainfo(msg):
    if debug:
        print(msg)

def test():
    clrscr()
    argumentos = argv
    print('Cantidad de argumentos:', len(argumentos))
    for i, argumento in enumerate(argumentos):
        print(f'4rgum3nt0 {i}:', argumento)

def show(seccionEspecifica=''):
    clrscr()
    indent = 3
    espacios = ' ' * (indent-1)
    sub1 = espacios
    sub2 = espacios * 2
    if seccionEspecifica:
        print(sub1, seccionEspecifica)
        for nota in libreta[seccionEspecifica]:
            print(sub2, nota, libreta[seccionEspecifica][nota]['text'])
    else:
        print("Todas las notas de todas las secciones:")
        for seccion in libreta:
            betainfo(seccion)
            print(sub1, seccion)
            for nota in libreta[seccion]:
                print(sub2, nota, libreta[seccion][nota]['text'])
            print()


def add(msj='', seccion=DEFAULT_SECTION):
    if seccion not in libreta:
        print(f'¡Nueva sección creada! \"{seccion}\"')
        libreta[seccion] = dict()

    T_NOTAS = len(libreta[seccion])
    ID_NOTA_NUEVA = T_NOTAS + 1

    libreta[seccion][ID_NOTA_NUEVA] = dict()
    libreta[seccion][ID_NOTA_NUEVA]['text'] = msj

    print('Nota agregada.')
    show()

def menu():
    print(
    "Willkommen мой друг",
    "Opciones disponibles:",
    "1) MostraR LiBreTa",
    "2) Añadir NoTa.",
    "0) Salir",
    sep='\n')

    opc = input("Opcion: ")
    if opc == '0':
        exit()
    elif opc == '1':
        show()
    elif opc == '2':
        add(input('Texto de la nota: '))
    menu()

def main():
    '''
    Recibe argumento(s) y dependiendo de la cantidad, 
    se decide la operación que se efectuará.
    '''
    betainfo('main')
    if T_ARGS == 1:
        betainfo('one argument')
        print("Libreta")
        show()
    elif len(argv) > 1:
        betainfo('more than one argument')
        if argv[1] == 'menu':
            betainfo('recognized argument')
            menu()
        elif argv[1] == 'add':
            if T_ARGS == 2: 
                # Si hay un segundo argumento, 
                # se añade como texto a una nota nueva
                # en la sección por defecto.
                 add(argv[2])
            elif T_ARGS == 5 and argv[3] in ['-s', '--seccion']:
                #print(argv[3], argv[4])
                add(argv[2], argv[4])
            else:
                argv.pop(0)
                argv.pop(0)
                sentence = ''
                for argus in argv:
                    sentence += ' ' + argus
                add(sentence.strip())
        else:
            if argv[1] in libreta:
                show(argv[1])
            else:
                print("Unrecognized yet:", argv[1])
    

if __name__ == "__main__":    
    if '-v' in argv: debug=True
    main()
    #test()
