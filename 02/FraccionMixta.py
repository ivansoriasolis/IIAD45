# -*- coding: utf-8 -*-
"""
Created on Mon Oct 25 15:51:27 2021

@author: IVAN
"""

from Fraccion import Fraccion

class FraccionMixta (Fraccion):
    def __init__(self, numerador, denominador, entero):
        super().__init__(numerador, denominador)
        self.__entero = entero
        
    def __str__(self):
        return str(self.__entero) + super().__str__()