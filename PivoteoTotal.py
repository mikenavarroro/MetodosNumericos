'''
Author: Miguel Angel Navarro Rodríguez
IG: @mikenavarror
TW: @MikeNavarroR
e-mail: mike.navarroro@gmail.com

'''
from math import *
from numpy import *
import numpy as np
import tkinter as tk

ven = tk.Tk()
ven.geometry('600x500')
dim_var = tk.IntVar()
mat = tk.StringVar()

lblA = tk.Label(ven, text="Matriz A").grid(row = 0, column = 0)
lbldim = tk.Label(ven, text="Dimensión de la matriz de nxn").grid(row = 1, column = 0)
entdim = tk.Entry(ven, textvariable=dim_var).grid(row = 1, column = 1)
def aceptar():
    dim = dim_var.get()
    A = np.empty((dim, dim))
    for i in range(dim):
        for j in range(dim):
            m = tk.Entry(ven, width= 10, textvariable=mat).place(x = i*70+100, y = j*50+70)
            lista[j] = mat.get()
    for i in range(dim):
        for j in range(dim):
            A[i, j] = lista[i, j]
    print(A)

btnaceptar = tk.Button(ven, text="Aceptar", command=aceptar).grid(row = 0, column = 1)
'''
for i in range(dim):
    for j in range(dim):
        A[i, j] = float(input("Dame el número en la posición {}, {}: ".format(i+1, j+1)))
print("Matriz B: ")
B = np.empty((dim, 1))
for i in range(dim):
    B[i, 0] = float(input("Dame el número en la posición {}, 1: ".format(i+1)))
solucion = np.linalg.solve(A, B)
print("="*dim)
print(A)
print("="*dim)
print(B)
print("="*dim)
print(solucion)
'''
ven.mainloop()
