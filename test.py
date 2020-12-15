from utils import subrayar, clrscr

def test():
    clrscr()
    
    # Subrayar.
    # subrayar(texto, caracter='=', porPalabra=True, auto_print=True)
    # Texto impreso en pantalla.
    subrayar('Título a subrayar')
    subrayar('Título a subrayar', '-')
    subrayar('Título a subrayar', '-', 0)
    print(subrayar('Título a subrayar', '-', 0, 0))

    # Texto retornado por la función.
    assert(subrayar('Título a subrayar', auto_print=0) == 'Título a subrayar\n====== = ======== ')
    assert(subrayar('Título a subrayar', auto_print=0) == 'Título a subrayar\n====== = ======== ')
    assert(subrayar('Título a subrayar', '-', auto_print=False) == 'Título a subrayar\n------ - -------- ')
    assert(subrayar('Título a subrayar', '-', False, False) == 'Título a subrayar\n-----------------')
    
    print('\n¡Todas las pruebas fueron exitosas!\n')

if __name__ == "__main__":    
    test()