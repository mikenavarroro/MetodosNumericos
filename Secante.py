'''
Author: Miguel Angel Navarro Rodríguez
IG: @mikenavarror
TW: @MikeNavarroR
e-mail: mike.navarroro@gmail.com

'''
from math import e, pi
from math import *
import sympy as sp
import msvcrt as mv

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
    c = b - ((b - a) / (fb - fa) * fb)
    lista.append(c)
    fc = sp.sympify(funcion).subs(x, c)
    if i != 0:
        error = abs((lista[i]-lista[i-1])/lista[i])
    print("{:<2}| {:^10.10s}| {:^10.10s}| {:^10.10s}| {:^10.10s}| {:^10.10s}| {:^11.10s}| {:^10.10s}|".format(str(i+1),str(a),str(b),str(fa),str(fb),str(c),str(fc),str(error)))
    print("-----------------------------------------------------------------------------------------")
    a, b = b, c
    i += 1
mv.getch()
print("Presiona cualquier tecla para salir")
mv.getch()