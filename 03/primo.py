# -*- coding: utf-8 -*-
"""
Created on Tue Nov  2 18:07:06 2021

@author: IVAN
"""

from time import time

def esPrimo(n):
    for divisor in range(2, n):
        #print(divisor)
        if n % divisor == 0:
            return False
    return True

tiempo_inicial = time()

esPrimo(12721)

tiempo_final = time()

print(tiempo_final - tiempo_inicial)