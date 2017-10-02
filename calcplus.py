#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys

try:
    fichero = str(sys.argv[1])
except IndexError:
    sys.exit("Escribe el nombre del fichero, ejemplo: fichero.txt")

fich = open(fichero, "r") 

operaciones = []

for linea in fich:
    operaciones = linea.split(",")
    print(operaciones)
    
#for operacion in operaciones:
#    if operacion[1] == "suma":
#        print("h")
#    elif operacion[1] == "resta":
#        print("d")
#    else:
#        print('Operación sólo puede ser suma, resta, divide, multiplica.')

fich.close()
