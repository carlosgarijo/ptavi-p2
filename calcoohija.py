#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
import calcoo


class CalculadoraHija(calcoo.Calculadora):

    def multi(self, x, y):
        return x * y

    def div(self, x, y):
        try:
            return x/y
        except ZeroDivisionError:
            sys.exit("Error: Division by zero is not allowed")


def operaciones(operacion, operando1, operando2, calc):

    if operacion == "suma":
        result = calc.suma(operando1, operando2)
    elif operacion == "resta":
        result = calc.resta(operando1, operando2)
    elif operacion == "multi":
        result = calc.multi(operando1, operando2)
    elif operacion == "div":
        result = calc.div(operando1, operando2)
    else:
        sys.exit('Operación sólo puede ser sumar, restar, multip o dividir.')

    return result

if __name__ == '__main__':
    try:
        operando1 = int(sys.argv[1])
        operando2 = int(sys.argv[3])
    except ValueError:
        sys.exit("Error: Non numerical parameters")

    calc = CalculadoraHija()

    result = operaciones(sys.argv[2], operando1, operando2, calc)

    print(result)
