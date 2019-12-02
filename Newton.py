'''
Author: Miguel Angel Navarro Rodríguez
IG: @mikenavarror
TW: @MikeNavarroR
e-mail: mike.navarroro@gmail.com

'''
import msvcrt as mv
from math import e, pi
from math import *
from sympy import *
import sympy as sp

x = sp.symbols('x')
funcion = input("Escribe la función en términos de x: ")
ini = float(input("Valor inicial: "))
erroru = float(input("Error: "))
func=sp.sympify(funcion)
derivada= func.diff(x)
error = 1
lista = []
i = 0
print("{:>11} {:>11} {:>11} {:>11}".format('Xn', 'f(Xn)', "f'(Xn)", 'Error'))

while error > erroru:
    fini = sp.sympify(funcion).subs(x, ini)
    fder = sp.sympify(derivada).subs(x, ini)
    x1 = ini - (fini/fder)
    if i == 0:
        lista.append(ini)
    lista.append(x1)
    if i != 0:
        error = abs((lista[i]-lista[i-1])/lista[i])
    print("{:<2}| {:^10.10s}| {:^10.10s}| {:^10.10s}| {:^10.10s}|".format(str(i+1),str(ini),str(fini),str(fder),str(error)))
    print("-----------------------------------------------------")
    ini = x1
    i += 1
mv.getch()
print("Presiona cualquier tecla para salir")
mv.getch()