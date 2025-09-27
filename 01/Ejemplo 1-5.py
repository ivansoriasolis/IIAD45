# Ejemplo 1-5: Encontrar factores de un número

def factores(n):
    results = []
    for k in range(1, n+1):
        if n % k == 0:
            results.append(k)
    return results 

