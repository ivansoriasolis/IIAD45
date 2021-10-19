# -*- coding: utf-8 -*-
"""
Ejemplo 1-2 Funcion que cuenta la cantida de ocurrencias 
"""
def contar(data, target):
    if not isinstance(data, (list, tuple, set)):
        raise TypeError("No es iterable")
    n = 0
    for item in data:
        if item == target:
            n += 1
    return n

lista = "[1, 3, 4, 5]"
buscado = 3

try:
    print(contar(lista, buscado))
except:
    print("Necesita un iterable")