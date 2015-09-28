#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys


class Calculadora():

    def suma(self, x, y):
        return x + y

    def resta(self, x, y):
        return x - y

if __name__ == '__main__':
    try:
        operando1 = int(sys.argv[1])
        operando2 = int(sys.argv[3])
    except ValueError:
        sys.exit("Error: Non numerical parameters")

    calc = Calculadora()

    if sys.argv[2] == "suma":
        result = calc.suma(operando1, operando2)
    elif sys.argv[2] == "resta":
        result = calc.resta(operando1, operando2)
    else:
        sys.exit('Operación sólo puede ser sumar o restar.')

    print(result)
