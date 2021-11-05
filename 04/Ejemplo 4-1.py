# Ejemplo 4-1. Implementación recursiva del factorial

def factorial(n):
    if n == 1:
        return 1
    else:
        return n*factorial(n-1)


