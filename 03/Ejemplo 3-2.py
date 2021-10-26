# -*- coding: utf-8 -*-
"""
Ejemplo 3-2. 
@author: IVAN
"""


def promedio_prefijo2(S):
    """Devuelve una lista tal que para todos los elementos 
    A[j] son iguales al promedio de los anteriores S[0]..S[j]"""
    n = len(S)
    A = [0]*n
    for j in range(n):
        A[j] = sum(S[0:j+1]) / (j+1)
    return A
