#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
import calcoohija

if __name__ == '__main__':

    fichero = open(sys.argv[1] , 'r')
    lineas = fichero.readlines()

    calc = calcoohija.CalculadoraHija()

    for linea in lineas:
	    datos = linea.split(',')
	    operacion = datos[0]
	    operandos = datos[1:]
	    operandos[-1] = operandos[-1][:-1]
	    print(operandos)
	    result = int(operandos[0])
        if operacion == "suma":
            for operando in operandos[1:]:
                operando = int(operando)
                result = calc.suma(result, operando)
        elif operacion == "resta":
            for operando in operandos[1:]:
                operando = int(operando)
                result = calc.resta(result, operando)
        elif operacion == "multi":
            for operando in operandos[1:]:
                operando = int(operando)
                result = calc.multi(result, operando)
        elif operacion == "div":
            for operando in operandos[1:]:
                operando = int(operando)
                result = calc.div(result, operando)
        else:
            sys.exit('Operación sólo puede ser sumar, restar, multip o dividir.')

    print(result)
