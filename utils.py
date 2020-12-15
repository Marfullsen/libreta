
import os

def clrscr():
   # for mac and linux(here, os.name is 'posix')
   if os.name == 'posix':
      _ = os.system('clear')
   else:
      # for windows platfrom
      _ = os.system('cls')

def help(auto_print=False):
   """
   La ayuda es una lista que
   retorna cada elemento con
   un salto de línea al final.
   """
   msg =[
      'Ayuda con los comandos.',
      'libreta                                 #Muestra las secciones con todas las notas.',
      'libreta add "Terminar documentación"    #Añade una nota.'
   ]
   if auto_print:
      print('\n'.join(msg))
   else: 
      return '\n'.join(msg)

def subrayar(texto, caracter='=', porPalabra=True, auto_print=True):
   """
   Subraya un texto con un caracter especial
   
   Parametros y su descripción:
   texto: string del contenido que será subrayado.
   caracter: string del símbolo que se usará para subrayar.
   porPalabra: Booleano que indica si los espacios no serán subrayados, por defecto True.
   auto_print: Booleano que indica si se imprime directamente en pantalla sin retorno, por defecto True.
   """
   palabras = texto.split(' ')
   largoConEspacios = len(texto)
   subrayado = ''
   retorno = ''
   if porPalabra:
      retorno += texto + '\n'

      for palabra in palabras:
         subrayado += (caracter * len(palabra)) + ' '
      retorno += subrayado
      
   else:
      subrayado = caracter * largoConEspacios
      retorno += texto + '\n' + subrayado

   if auto_print: 
      retorno += '\n'
      print(retorno, end='')
   else:
      return retorno
      