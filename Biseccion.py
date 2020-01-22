'''
Author: Miguel Angel Navarro Rodríguez
IG: @mikenavarror
TW: @MikeNavarroR
e-mail: mike.navarroro@gmail.com

'''
import sympy as sp
import tkinter as tk
from numpy import *

x = sp.symbols('x')
funcion = input("Escribe la función en términos de x: ")
a = float(input("Valor de a: "))
b = float(input("Valor de b: "))
erroru = float(input("Error: "))
error = 1
lista = []
i = 0
print("{:>11} {:>11} {:>11} {:>11} {:>11} {:>11} {:>11}".format('a', 'b', 'f(a)', 'f(b)', 'Xn', 'f(Xn)', 'Error'))

while error > erroru:
    fa = sp.sympify(funcion).subs(x, a)
    fb = sp.sympify(funcion).subs(x, b)
    c = (a+b)/2
    lista.append(c)
    fc = sp.sympify(funcion).subs(x, c)
    if i != 0:
        error = abs((lista[i]-lista[i-1])/lista[i])
    print("{:<2}| {:^10.10s}| {:^10.10s}| {:^10.10s}| {:^10.10s}| {:^10.10s}| {:^11.10s}| {:^10.10s}|".format(str(i+1),str(a),str(b),str(fa),str(fb),str(c),str(fc),str(error)))
    print("-----------------------------------------------------------------------------------------")
    if fa * fc < 0:
        b = c
    elif fa * fc > 0:
        a = c
    i += 1
