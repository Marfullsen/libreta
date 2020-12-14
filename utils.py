
import os

def clrscr():
   # for mac and linux(here, os.name is 'posix')
   if os.name == 'posix':
      _ = os.system('clear')
   else:
      # for windows platfrom
      _ = os.system('cls')

def help():
   msg =[
      'Ayuda con los comandos.',
      'libreta\t\t\t#Muestra las secciones con todas las notas.',
      'libreta add "Terminar documentación"\t\t#Añade una nota.'
   ]
   return '\n'.join(msg)