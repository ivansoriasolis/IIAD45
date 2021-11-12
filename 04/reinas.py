# -*- coding: utf-8 -*-
"""
Created on Fri Nov 12 17:25:45 2021

@author: IVAN
"""
def ocupadoN(i, j, tablero):
    if i < 0:
        return False
    return tablero[i][j] or ocupadoN(i-1, j, tablero)

ancho = 8
alto = 8
tablero = [ [0 for n in range(alto)] for m in range(ancho)]