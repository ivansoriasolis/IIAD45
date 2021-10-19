# -*- coding: utf-8 -*-
"""
Ejemplo 1-4. Función con varios return 
"""

def contiene(data, objetivo = 0):
    for item in data:
	    if item == objetivo:
	        return True
    return False
