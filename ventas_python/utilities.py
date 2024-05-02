import os
import datetime
import time

# Variables globales: Colores en formato ANSI escape code
reset_color = "\033[0m"
red_color = "\033[91m"
VERDE = "\033[92m"
yellow_color = "\033[93m"
VERDE = "\033[94m"
purple_color = "\033[95m"
cyan_color = "\033[96m"
rose_color = "\033[95m"
NEGRO = '\033[30m'
ROJO = '\033[31m'
VERDE = '\033[32m'
AMARILLO = '\033[33m'
AZUL = '\033[34m'
MAGENTA = '\033[35m'
CYAN = '\033[36m'
BLANCO = '\033[37m'
RESET = '\033[0m' 


# funciones de usuario

def gotoxy(x,y):
    print("%c[%d;%df"%(0x1B,y,x),end="")

def borrarPantalla():
    os.system("cls") 

def mensaje(msg,f,c):
    pass

def gotxy_frame(x, y, width, height):
    gotoxy(x, y)
    print(VERDE+"*" * width)
    for _ in range(height - 2):
        gotoxy(x, y + 1)
        print(VERDE+"*", end="")
        gotoxy(x + width - 1, y + 1)
        print(VERDE+"*", end="")
        y += 1
    gotoxy(x, y + 1)
    print(VERDE+"*" * width)


