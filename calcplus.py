#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
import calcoo
import calcoohija

try:
    fichero = str(sys.argv[1])
except IndexError:
    sys.exit("Escribe el nombre del fichero, ejemplo: fichero.txt")

fich = open(fichero, "r") 

operaciones = []

for linea in fich:
    linea = linea.replace("\n","")
    operaciones = linea.split(",")
    
    if operaciones[0] == "suma":
        print("h")
    elif operaciones[0] == "resta":
        print("d")
    elif operaciones[0] == "multiplica":
        print("ff")
    elif operaciones[0] == "divide":
        print("ee")
    
    else:
        print('Operación sólo puede ser suma, resta, divide, multiplica.')

fich.close()
