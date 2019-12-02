'''
Author: Miguel Angel Navarro Rodríguez
IG: @mikenavarror
TW: @MikeNavarroR
e-mail: mike.navarroro@gmail.com

'''
from math import *
import msvcrt as mv
from numpy import *
import numpy as np

print("Matriz A")
dim = int(input("Dimensión de la matriz de nxn: "))
A = np.empty((dim, dim))
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
mv.getch()
print("Presiona cualquier tecla para salir")
mv.getch()