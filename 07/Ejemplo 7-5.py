# Ejemplo 7-5. Una clase _Nodo para listas doblemente enlazadas

class _Node:
    """Clase no publica para almacenar un nodo de lista doblemente enlazada"""
    __slots__ = '_elemento', '_prev', '_next'
    
    def __init__(self, element, prev, next):
        self._element = elemento
        self._prev = prev
        self._next = next

