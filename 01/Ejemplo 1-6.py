# Ejemplo 1-6: Generador de factores de un número

def factores(n):
    for k in range(1, n+1):
        if n % k == 0:
            yield k 

