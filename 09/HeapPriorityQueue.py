from Empty import Empty

from PriorityQueueBase import PriorityQueueBase
from PriorityQueue import PriorityQueue

class HeapPriorityQueue(PriorityQueue): # la clase base define _Item
  """Una cola de prioridad min-oriented implementada con un heap bianrio."""
  #------------------------ comportamientos privados ------------------------------
  def _parent(self, j):
    return (j-1) // 2

  def _left(self, j):
    return 2*j + 1
  
  def _right(self, j):
    return 2*j + 2

  def _has_left(self, j):
    return self._left(j) < len(self._data)     # indice mas alla de la lista?
  
  def _has_right(self, j):
    return self._right(j) < len(self._data)    # indice mas alla de la lista?
  
  def _swap(self, i, j):
    """Swap the elements at indices i and j of array."""
    self._data[i], self._data[j] = self._data[j], self._data[i]

  def _upheap(self, j):
    parent = self._parent(j)
    if j > 0 and self._data[j] < self._data[parent]:
      self._swap(j, parent)
      self._upheap(parent)             # recur a la posicion del padre
  
  def _downheap(self, j):
    if self._has_left(j):
      left = self._left(j)
      small_child = left               # aunque la derecha sea menor
      if self._has_right(j):
        right = self._right(j)
        if self._data[right] < self._data[left]:
          small_child = right
      if self._data[small_child] < self._data[j]:
        self._swap(j, small_child)
        self._downheap(small_child)    # recur a la posicion del hijo menor

  #--------------------------- comportamientos publicos  ------------------------------
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

if __name__ == '__main__':
    #Insertamos los pares (k, v) en cualquier orden
    hpq = HeapPriorityQueue()
    hpq.add(4, 'C')
    hpq.add(5, 'A')
    hpq.add(6, 'Z')
    hpq.add(15, 'K')
    hpq.add(9, 'F')
    hpq.add(7, 'Q')
    hpq.add(20, 'B')
    hpq.add(16, 'X')
    hpq.add(25, 'J')
    hpq.add(14, 'E')
    hpq.add(12, 'H')
    hpq.add(11, 'S')
    hpq.add(8, 'W')
    #atendemos por prioridad
    while not hpq.is_empty():
        print(hpq.remove_min())

    