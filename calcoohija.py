#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys


class Calculadora():

    def suma(self, x, y):
        return x + y

    def resta(self, x, y):
        return x - y


class CalculadoraHija(Calculadora):

    def multi(self, x, y):
        return x * y

    def div(self, x, y):
        try:
            return x/y
        except ZeroDivisionError:
            sys.exit("Error: Division by zero is not allowed")


if __name__ == '__main__':
    try:
        operando1 = int(sys.argv[1])
        operando2 = int(sys.argv[3])
    except ValueError:
        sys.exit("Error: Non numerical parameters")

    calc = CalculadoraHija()

    if sys.argv[2] == "suma":
        result = calc.suma(operando1, operando2)
    elif sys.argv[2] == "resta":
        result = calc.resta(operando1, operando2)
    elif sys.argv[2] == "multi":
        result = calc.multi(operando1, operando2)
    elif sys.argv[2] == "div":
        result = calc.div(operando1, operando2)
    else:
        sys.exit('Operación sólo puede ser sumar, restar, multip o dividir.')

    print(result)
