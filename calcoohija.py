#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
import calcoo


class CalculadoraHija(calcoo.Calculadora):
    def __init__(self, num1, num2):
        self.valor1 = num1
        self.valor2 = num2

    def mult(self):
        return self.valor1 * self.valor2

    def div(self):
        return self.valor1 / self.valor2

if __name__ == "__main__":
    try:
        operando1 = int(sys.argv[1])
        operando2 = int(sys.argv[3])
    except ValueError:
        sys.exit("Error: Non numerical parameters")

    numeros = CalculadoraHija(operando1, operando2)

    if sys.argv[2] == "suma":
        result = numeros.suma()
    elif sys.argv[2] == "resta":
        result = numeros.resta()
    elif sys.argv[2] == "multiplica":
        result = numeros.mult()
    elif sys.argv[2] == "divide":
        try:
            result = numeros.div()
        except ZeroDivisionError:
            print("Division by zero is not allowed")
    else:
        sys.exit('Operación sólo puede ser suma, resta, divide, multiplica.')

    try:
        print(result)
    except NameError:
        print("No se puede mostrar el resultado")
