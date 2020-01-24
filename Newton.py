'''
Author: Miguel Angel Navarro Rodríguez
IG: @mikenavarror
TW: @MikeNavarroR
e-mail: mike.navarroro@gmail.com

'''

import sympy as sp
import tkinter as tk
from numpy import *
from matplotlib import pyplot as plt

ven = tk.Tk()
ven.geometry('600x500')
ven.title("Newton")
ven.resizable(False, False)

funcion = tk.StringVar()
a_var = tk.StringVar()
err_u = tk.StringVar()

x = sp.symbols('x')

lblfun = tk.Label(ven, text="Función:").grid(row = 0, column = 1)
lblfunc = tk.Label(ven, text="f(x)").grid(row = 1, column = 5)
entfunc = tk.Entry(ven, textvariable=funcion).grid(row = 2, column = 5)
lbla = tk.Label(ven, text="Valor inicial").grid(row = 4, column = 5)
enta = tk.Entry(ven, textvariable=a_var).grid(row = 5, column = 5)
lblerr = tk.Label(ven, text="Error:").grid(row = 8, column = 1)
lblerroru = tk.Label(ven, text="error").grid(row = 9, column = 5)
enterroru = tk.Entry(ven, textvariable=err_u).grid(row = 10, column = 5)

def iniciar():
    vent = tk.Toplevel(ven)

    funci = funcion.get()
    erroru = float(err_u.get())
    ini = float(a_var.get())

    func = sp.sympify(funci)
    derivada = func.diff(x)
    error = 1
    lista = []
    i = 0

    vent.title(funci)

    m = tk.Label(vent, text="n", bg = "black", fg = "white", width=20, height=1).grid(row = 0, column = 0)
    m = tk.Label(vent, text="Xn", bg = "black", fg = "white", width=20, height=1).grid(row = 0, column = 1)
    m = tk.Label(vent, text="f(Xn)", bg = "black", fg = "white", width=30, height=1).grid(row = 0, column = 2)
    m = tk.Label(vent, text="f'(Xn)", bg = "black", fg = "white", width=30, height=1).grid(row = 0, column = 3)
    m = tk.Label(vent, text="error", bg = "black", fg = "white", width=20, height=1).grid(row = 0, column = 4)

    while error > erroru:
        fini = sp.sympify(funci).subs(x, ini)
        fder = sp.sympify(derivada).subs(x, ini)
        x1 = ini - (fini/fder)
        if i == 0:
            lista.append(ini)
        lista.append(x1)
        if i != 0:
            error = abs((lista[i]-lista[i-1])/lista[i])
        m = tk.Label(vent, text=i+1, width=10, height=1).grid(row = i+1, column = 0)
        m = tk.Label(vent, text=ini).grid(row = i+1, column = 1)
        m = tk.Label(vent, text=fini, width=20, height=1).grid(row = i+1, column = 2)
        m = tk.Label(vent, text=fder, width=20, height=1).grid(row = i+1, column = 3)
        m = tk.Label(vent, text=error).grid(row = i+1, column = 4)
        ini = x1
        i += 1


def graficar():
    funci = funcion.get()
    func = sp.sympify(funci)
    derivada = func.diff(x)
    lista = [func, derivada]

    a, b, z, y = [], [], [], []
    
    for i in range(-50, 51):
        z.append(i)
        a.append(i)
        y.append(sp.sympify(func).subs(x, i))
        b.append(sp.sympify(derivada).subs(x, i))


    plt.plot(z, y)
    plt.plot(a, b)
    plt.legend(labels= lista)

    plt.axhline(0, color="black")
    plt.axvline(0, color="black")

    plt.show()


tabular = tk.Button(ven, text="Tabular", command=iniciar).grid(row = 11, column = 3)
graficar = tk.Button(ven, text="Graficar", command=graficar).grid(row = 11, column = 5)

ven.mainloop()
