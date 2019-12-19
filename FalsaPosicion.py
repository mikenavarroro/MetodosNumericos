'''
Author: Miguel Angel Navarro Rodríguez
IG: @mikenavarror
TW: @MikeNavarroR
e-mail: mike.navarroro@gmail.com

'''
import numpy as np
import sympy as sp
import tkinter as tk
from matplotlib import pyplot as plt

ven = tk.Tk()
ven.geometry('600x500')

func = tk.StringVar()
a_var = tk.IntVar()
b_var = tk.IntVar()
err_u = tk.StringVar()


x = sp.symbols('x')

lblfunc = tk.Label(ven, text="f(x)").place(x = 10, y = 10)
entfunc = tk.Entry(ven, textvariable=func).place(x = 30, y = 10)
lbla = tk.Label(ven, text="a").place(x = 10, y = 30)
enta = tk.Entry(ven, textvariable=a_var).place(x = 30, y = 30)
lblb = tk.Label(ven, text="b").place(x = 10, y = 50)
entb = tk.Entry(ven, textvariable=b_var).place(x = 30, y = 50)
lblerroru = tk.Label(ven, text="error").place(x = 10, y = 70)
enterroru = tk.Entry(ven, textvariable=err_u).place(x = 30, y = 70)

def graficar():
    funcion = func.get()
    a = a_var.get()
    b = b_var.get()
    if a > b:
        a, b = b, a

    plt.plot(x, [sp.sympify(funcion).subs(x, i) for i in range(1, 19)])


    plt.show()
def iniciar():
    vent = tk.Toplevel(ven)
    funcion = func.get()
    a = a_var.get()
    b = b_var.get()
    erroru = float(err_u.get())
    error = 1
    lista = []
    i = 0
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

tabular = tk.Button(ven, text="Tabular", command=iniciar).place(x = 200, y = 300)
graficar = tk.Button(ven, text="Graficar", command=graficar). place(x = 400, y = 300)

ven.mainloop()
