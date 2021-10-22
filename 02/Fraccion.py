# -*- coding: utf-8 -*-
"""
Created on Tue Oct 19 19:45:23 2021

@author: IVAN
"""

class Fraccion:
    
    def __init__(self, num, den):
        if not isinstance(num,int) or not isinstance(den, int):
            raise TypeError("Numerador y denominador deben ser int")
        if den == 0:
            raise ValueError("Denominador no puede ser 0")
        self.__numerador = num
        self.__denominador = den
    
    def simplificar(self):
        num = self.__numerador
        den = self.__denominador
        mcd = self.__mcd(num, den)
        self.__numerador = int(num/mcd)
        self.__denominador = int(den/mcd)
    
    def __mcd(self, a, b):
        while a:
            a, b = b % a, a
        return b
        
    def set_num(self, num):
        self.__numerador = num
        
    def set_den(self, den):
        self.__numerador = den
        
    def get_num(self):
        return self.__numerador
    
    def get_den(self):
        return self.__denominador
        
        