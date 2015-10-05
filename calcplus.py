#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
import calcoohija

def operaciones(dicc, operacion, operando, operandos, result):
    try:
        funcion = dicc[operacion]
        for operando in operandos[1:]:
            operando = int(operando)
            result = funcion(result, operando)
    except:
        sys.exit('Operacion only: suma, resta , multiplica o divide')

    return result

if __name__ == '__main__':

    fich = sys.argv[1]
    fichero = open(fich, 'r')
    lineas = fichero.readlines()

    calc = calcoohija.CalculadoraHija()

    dicc = {"suma": calc.suma, "resta": calc.resta, "multiplica": calc.multi, "divide": calc.div}

    for linea in lineas:
        datos = linea.split(',')
        """Cogemos la operacion"""
        operacion = datos[0]
        """Cogemos los operandos"""
        operandos = datos[1:]
        """Quitamos el /n"""
        operandos[-1] = operandos[-1][:-1]
        result = int(operandos[0])

        result = operaciones(dicc, operacion, operando, operando, result)

        print(operacion + ": ", result)
