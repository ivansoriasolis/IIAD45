# -*- coding: utf-8 -*-
"""
Ejemplo 3-3. 
@author: IVAN
"""


def promedio_prefijo3(S):
    """Devuelve una lista tal que para todos los elementos 
    A[j] son iguales al promedio de los anteriores S[0]..S[j]"""
    n = len(S)
    A = [0]*n
    total = 0
    for j in range(n):
        total += S[j]
        A[j] = total / (j+1)
    return A
