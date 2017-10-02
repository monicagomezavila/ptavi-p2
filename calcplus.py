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


for linea in fich:
    linea = linea.replace("\n","")
    operaciones = linea.split(",")
    elementos = len(operaciones)
    numeros_sobran = operaciones[3:elementos]
    
    operando1 = int(operaciones[1])
    operando2 = int(operaciones[2])
  
    if operaciones[0] == "suma":
        result = operando1+operando2
        for numero in numeros_sobran:
            result = result + int(numero)
        
        print(result)

    elif operaciones[0] == "resta":
        result = operando1-operando2
        for numero in numeros_sobran:
            result = result - int(numero)
        
        print(result)

    elif operaciones[0] == "multiplica":
        result = operando1*operando2
        for numero in numeros_sobran:
            result = result * int(numero)
        
        print(result)

    elif operaciones[0] == "divide":
        try:
           result = operando1/operando2
        except ZeroDivisionError:
           print("Division by zero is not allowed")         
        for numero in numeros_sobran:
            result = result / int(numero)
        
        print(result)
    
    else:
        print('Operación sólo puede ser suma, resta, divide, multiplica.')

fich.close()
