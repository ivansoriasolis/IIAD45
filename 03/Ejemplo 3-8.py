# Ejemplo 3-8. Algoritmo unico2

def unico2(S):
    """Devuelve True si no hay elementos duplicados en la secuencia S"""
    temp = sorted(S)
    for j in range(len(temp)-1):
        if temp[j+1] == temp[j]:
            return False
    return True

unico2([1,2,3,2])