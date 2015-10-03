#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
import calcoohija

if __name__ == '__main__':

    fich = sys.argv[1]
    fichero = open(fich, 'r')
    lineas = fichero.readlines()

    calc = calcoohija.CalculadoraHija()

    for linea in lineas:
        datos = linea.split(',')
        """Cogemos la operacion"""
        operacion = datos[0]
        """Cogemos los operandos"""
        operandos = datos[1:]
        """Quitamos el /n"""
        operandos[-1] = operandos[-1][:-1]
        result = int(operandos[0])
        if operacion == "suma":
            for operando in operandos[1:]:
                operando = int(operando)
                result = calc.suma(result, operando)
        elif operacion == "resta":
            for operando in operandos[1:]:
                operando = int(operando)
                result = calc.resta(result, operando)
        elif operacion == "multiplica":
            for operando in operandos[1:]:
                operando = int(operando)
                result = calc.multi(result, operando)
        elif operacion == "divide":
            for operando in operandos[1:]:
                operando = int(operando)
                result = calc.div(result, operando)
        else:
            sys.exit('Operacion only: sumar, restar, multip o dividir')

        print(operacion + ": ", result)
