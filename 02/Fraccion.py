# -*- coding: utf-8 -*-
"""
Created on Tue Oct 19 19:45:23 2021

@author: IVAN
"""

class Fraccion:
    
    def __init__(self, num, den):
        self.__numerador = num
        self.__denominador = den
        
    def set_num(self, num):
        self.__numerador = num
        
    def set_den(self, den):
        self.__numerador = den
        
    def get_num(self):
        return self.__numerador
    
    def get_den(self):
        return self.__denominador
        
        