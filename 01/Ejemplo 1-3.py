# -*- coding: utf-8 -*-
"""
Ejemplo 1-3 Funcion que cuenta la cantida de ocurrencias 
"""
def contar(data, target):
    n = 0
    for item in data:
        if item == target:
            n += 1
    return n

lista = [1, 3, 4, 5]
buscado = 3

print(contar(lista, buscado))
