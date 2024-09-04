#criar aqui um centerprint, um print centralizado automático
#Também criar aqui outras ferramentas de terminal 
from os import get_terminal_size
from os import system
__size = get_terminal_size()[0]
def centerprint(message):
    half = int((len(message))/2)
    print(' '*(int((__size/2))-half), f"{message}")
def filler(char):
    print(char*__size)

def tabber(msg):
    print(' '*4, f"{msg}")
def cls():
    system("CLS")
def pause():
    system("pause")

if __name__ == "__main__":
    filler('*')
    centerprint("Roma")
    filler('*')