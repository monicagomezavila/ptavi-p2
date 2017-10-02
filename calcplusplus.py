#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
import calcoo
import calcoohija
import csv


class CalculadoraPlus(calcoohija.CalculadoraHija):
    def __init__(self, num1,num2):
        self.valor1=num1
        self.valor2=num2


if __name__ == "__main__":

    try:
        fichero = str(sys.argv[1])
    except IndexError:
        sys.exit("Escribe el nombre del fichero, ejemplo: fichero.txt")

    with open(fichero, "r") as fich:
        for linea csv.reader(fich):

        elementos = len(linea)
        numeros_sobran = linea[3:elementos]
        
        try:
            operando1 = int(operaciones[1])
            operando2 = int(operaciones[2])
        except ValueError:
            print("Introduce valores enteros en tu fichero")
        
        numeros = CalculadoraPlus(operando1,operando2)
  
        if operaciones[0] == "suma":
            result = numeros.suma()
            for numero in numeros_sobran:
                result = result + int(numero)
        
            print(result)

        elif operaciones[0] == "resta":
            result = numeros.resta()
            for numero in numeros_sobran:
                result = result - int(numero)
        
            print(result)

        elif operaciones[0] == "multiplica":
            result = numeros.mult()
            for numero in numeros_sobran:
                result = result * int(numero)
        
            print(result)

        elif operaciones[0] == "divide":
            try:
                result = numeros.div()
            except ZeroDivisionError:
                print("No se puede dividir entre 0") 
                break        
            for numero in numeros_sobran:
                try:
                    result = result / int(numero)
                except ZeroDivisionError:
                     print("No se puede divir entre 0")
                     print("Tu resultado antes de encontar un 0 es:")
                     break 
        
            print(result)
    
        else:
            print('Operación sólo puede ser suma, resta, divide, multiplica.')

fich.close()
