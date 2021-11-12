# -*- coding: utf-8 -*-
"""
Created on Fri Nov 12 17:25:45 2021

@author: IVAN
"""
def ocupadoN(i, j, tablero):
    if i < 0:
        return False
    return tablero[i][j] or ocupadoN(i-1, j, tablero)

def ocupadoS(i, j, tablero):
    if i > len(tablero)-1:
        return False
    return tablero[i][j] or ocupadoS(i+1, j, tablero)

def ocupadoE(i, j, tablero):
    if j > len(tablero[0])-1:
        return False
    return tablero[i][j] or ocupadoE(i, j+1, tablero)

def ocupadoO(i, j, tablero):
    if j < 0:
        return False
    return tablero[i][j] or ocupadoO(i, j-1, tablero)

ancho = 8
alto = 8
tablero = [ [0 for n in range(ancho)] for m in range(alto)]