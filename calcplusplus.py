#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
import csv
import calcoohija
import calcplus

if __name__ == '__main__':

    calc = calcoohija.CalculadoraHija()

    dicc = {"suma": calc.suma,
            "resta": calc.resta,
            "multiplica": calc.multi,
            "divide": calc.div}

    fich = sys.argv[1]
    with open(fich, newline='') as fichero:
        lineas = csv.reader(fichero)

        for linea in lineas:
            """Cogemos la operacion"""
            operacion = linea[0]
            """Cogemos los operandos"""
            operandos = linea[1:]
            result = int(operandos[0])

            result = calcplus.operaciones(dicc, operacion, operandos, result)

            print(operacion + ": ", result)
    # Cerramos el fichero
