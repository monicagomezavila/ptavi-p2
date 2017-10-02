#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys


class Calculadora():
    def __init__(self, num1, num2):
        self.valor1 = num1
        self.valor2 = num2

    def suma(self):
        return self.valor1 + self.valor2

    def resta(self):
        return self.valor1 - self.valor2

if __name__ == "__main__":
    try:
        operando1 = int(sys.argv[1])
        operando2 = int(sys.argv[3])
    except ValueError:
        sys.exit("Error: Non numerical parameters")

    numeros = Calculadora(operando1, operando2)

    if sys.argv[2] == "suma":
        result = numeros.suma()
    elif sys.argv[2] == "resta":
        result = numeros.resta()
    else:
        sys.exit('Operación sólo puede ser sumar o restar.')

    print(result)
