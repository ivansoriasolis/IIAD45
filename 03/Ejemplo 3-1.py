# Ejemplo 3-1.  Funcion que devuelve el mayor valor de una lista

def encontrar_max(data):
    """Devuelve el elemento maximo de una lista"""
    masgrade = data[0]
    for val in data:
        if val > masgrande:
            masgrade = val
    return masgrande
