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
	    lenght = len(datos)
	    for i in range(lenght):
	       if i == 0:
	           pass
	       elif i == 1:
	           operador1 = datos[i]
	           operador2 = datos[i+1]
	           result = calcoohija.operaciones(operacion, operador1, operador2, calc)
	       elif i != lenght:
	           if i == (lenght - 1):
	               operador1 = result
	               operador2 = datos[i+1][:-1]
	               result = calcoohija.operaciones(operacion, operador1, operador2, calc)
	           else:
	               operador1 = result
	               operador2 = datos[i+1]
	               result = calcoohija.operaciones(operacion, operador1, operador2, calc)

    print(result)
    """if operacion == "suma":
        result = calc.suma(operando1, operando2)
    elif operacion == "resta":
        result = calc.resta(operando1, operando2)
    elif operacion == "multiplica":
        result = calc.multi(operando1, operando2)
    elif operacion == "divide":
        result = calc.div(operando1, operando2)
    else:
        sys.exit('Operación sólo puede ser sumar, restar, multip o dividir.')

    print(result)"""
