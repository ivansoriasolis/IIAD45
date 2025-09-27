# Ejemplo 9.6: Revision de la clas HeapPriorityQueue para incluir un constructor con monticulo  

  def __init__(self, contents = ()):
    """Crea una nueva cola de prioridad.
    
    Por defecto la cola puede estar vacía. Si se da un contenido,
    esta debe ser una secuencia iterable de tuplas (k, v)
    especificando el conenido incial"""
    self._data = [ self._Item(k, v) for k, v in contents ]
    if len(self._data) > 1:                   # construir el heap
      self._heapify()

  def _heapify(self):
    start = self._parent(len(self) - 1)     # empezar en el ultimo padre
    for j in range(start, -1, -1):          # ir hasta la raiz
      self._downheap(j)