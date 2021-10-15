# -*- coding: utf-8 -*-
"""
Ejemplo 1-5. Función tradicional que computa factores
"""

def factores(n):
    results = []
    for k in range(1, n+1):
        if n % k == 0:
            results.append(k)
    return results 

