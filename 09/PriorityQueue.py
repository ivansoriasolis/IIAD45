# Ejemplo 9-5. Implementación de una cola de prioridad usando un montículo binario

from Empty import Empty
from PriorityQueueBase import PriorityQueueBase

class PriorityQueue(PriorityQueueBase):
    #--------------------------- comportamientos publicos  ------------------------------
    def __init__(self):
        """Crea una nueva cola de prioridad."""
        self._data = []

    def __len__(self):
        """Devolver el numero de items en la cola de prioridad."""
        return len(self._data)

    def add(self, key, value):
        """Agregar un par clave valor para la cola de prioridad."""
        self._data.append(self._Item(key, value))
        self._upheap(len(self._data) - 1)            # upheap la nueva posicion
    
    def min(self):
        """Devuelve pero no remueve (k,v)  con la minima clave."""
        if self.is_empty():
            raise Empty('Cola de prioridad vacia.')
        item = self._data[0]
        return (item._key, item._value)

    def remove_min(self):
        """Remueve y devuelve (k,v) con la clave minima."""
        if self.is_empty():
            raise Empty('Cola de prioridad vacia.')
        self._swap(0, len(self._data) - 1)           # poner item minimo al final
        item = self._data.pop()                      # y remover el item de la lista;
        self._downheap(0)                            # entonces fijar la nueva posicion
        return (item._key, item._value)