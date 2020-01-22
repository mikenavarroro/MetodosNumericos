'''
Author: Miguel Angel Navarro Rodríguez
IG: @mikenavarror
TW: @MikeNavarroR
e-mail: mike.navarroro@gmail.com

'''
from numpy import *
import sympy as sp
import tkinter as tk
from matplotlib import pyplot as plt

ven = tk.Tk()
ven.geometry('600x500')
ven.title("Falsa Posición")
ven.resizable(False, False)

func = tk.StringVar()
a_var = tk.StringVar()
b_var = tk.StringVar()
err_u = tk.StringVar()


x = sp.symbols('x')

lblfun = tk.Label(ven, text="Función:").grid(row = 0, column = 1)
lblfunc = tk.Label(ven, text="f(x)").grid(row = 1, column = 5)
entfunc = tk.Entry(ven, textvariable=func).grid(row = 2, column = 5)
lblinter = tk.Label(ven, text="Intervalo:").grid(row = 3, column = 1)
lbla = tk.Label(ven, text="a").grid(row = 4, column = 5)
enta = tk.Entry(ven, textvariable=a_var).grid(row = 5, column = 5)
lblb = tk.Label(ven, text="b").grid(row = 6, column = 5)
entb = tk.Entry(ven, textvariable=b_var).grid(row = 7, column = 5)
lblerr = tk.Label(ven, text="Error:").grid(row = 8, column = 1)
lblerroru = tk.Label(ven, text="error").grid(row = 9, column = 5)
enterroru = tk.Entry(ven, textvariable=err_u).grid(row = 10, column = 5)

def graficar():
    funcion = func.get()

    z = np.arange(-10, 10, 1000)
    y = sp.sympify(funcion).subs(x, z)

    plt.plot(z, y)
    plt.title(funcion)
    plt.xlim(-10, 10)
    plt.ylim(-10, 10)
    plt.axhline(0, color="black")
    plt.axvline(0, color="black")
    plt.show()


def iniciar():
    vent = tk.Toplevel(ven)
    funcion = func.get()
    a = float(a_var.get())
    b = float(b_var.get())
    erroru = float(err_u.get())
    error = 1
    lista = []
    i = 0

    vent.title(funcion)

    m = tk.Label(vent, text="n", bg = "black", fg = "white", width=10, height=1).grid(row = 0, column = 0)
    m = tk.Label(vent, text="a", bg = "black", fg = "white", width=10, height=1).grid(row = 0, column = 1)
    m = tk.Label(vent, text="b", bg = "black", fg = "white", width=10, height=1).grid(row = 0, column = 2)
    m = tk.Label(vent, text="f(a)", bg = "black", fg = "white", width=10, height=1).grid(row = 0, column = 3)
    m = tk.Label(vent, text="f(b)", bg = "black", fg = "white", width=10, height=1).grid(row = 0, column = 4)
    m = tk.Label(vent, text="Xn", bg = "black", fg = "white", width=10, height=1).grid(row = 0, column = 5)
    m = tk.Label(vent, text="f(Xn)", bg = "black", fg = "white", width=10, height=1).grid(row = 0, column = 6)
    m = tk.Label(vent, text="error", bg = "black", fg = "white", width=10, height=1).grid(row = 0, column = 7)

    while error > erroru:
        fa = sp.sympify(funcion).subs(x, a)
        fb = sp.sympify(funcion).subs(x, b)
        c = ((a * fb) - (b * fa))/(fb - fa)
        lista.append(c)
        fc = sp.sympify(funcion).subs(x, c)
        if i != 0:
            error = abs((lista[i]-lista[i-1])/lista[i])
        m = tk.Label(vent, text=i+1, width=10, height=1).grid(row = i+1, column = 0)
        m = tk.Label(vent, text=a).grid(row = i+1, column = 1)
        m = tk.Label(vent, text=b, width=10, height=1).grid(row = i+1, column = 2)
        m = tk.Label(vent, text=fa).grid(row = i+1, column = 3)
        m = tk.Label(vent, text=fb, width=10, height=1).grid(row = i+1, column = 4)
        m = tk.Label(vent, text=c).grid(row = i+1, column = 5)
        m = tk.Label(vent, text=fc, width=10, height=1).grid(row = i+1, column = 6)
        m = tk.Label(vent, text=error).grid(row = i+1, column = 7)

        if fa * fc < 0:
            b = c
        elif fa * fc > 0:
            a = c
        i += 1

tabular = tk.Button(ven, text="Tabular", command=iniciar).grid(row = 11, column = 3)
graficar = tk.Button(ven, text="Graficar", command=graficar).grid(row = 11, column = 5)

ven.mainloop()
