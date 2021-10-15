# -*- coding: utf-8 -*-
"""
Ejemplo 1-2 Funcion que cuenta la cantida de ocurrencias 
"""

def count(data, target):
    n = 0
    for item in data:
        if item == target:
            n += 1
    return n
