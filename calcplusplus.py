#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
import csv
import calcoohija

if __name__ == '__main__':

    calc = calcoohija.CalculadoraHija()
    fich = sys.argv[1]
    with open(fich, newline='') as fichero:
        lineas = csv.reader(fichero)

        for linea in lineas:
            """Cogemos la operacion"""
            operacion = linea[0]
            """Cogemos los operandos"""
            operandos = linea[1:]
            result = int(operandos[0])
            if operacion == "suma":
                for operando in operandos[1:]:
                    operando = int(operando)
                    result = calc.suma(result, operando)
                print(operacion + ": ", result)
            elif operacion == "resta":
                for operando in operandos[1:]:
                    operando = int(operando)
                    result = calc.resta(result, operando)
                print(operacion + ": ", result)
            elif operacion == "multiplica":
                for operando in operandos[1:]:
                    operando = int(operando)
                    result = calc.multi(result, operando)
                print(operacion + ": ", result)
            elif operacion == "divide":
                for operando in operandos[1:]:
                    operando = int(operando)
                    result = calc.div(result, operando)
                print(operacion + ": ", result)
            else:
                sys.exit('Operacion only: sumar, restar, multip o dividir')

    # Cerramos el fichero
