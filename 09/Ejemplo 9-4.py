#Ejemplo 9-4. Implementacion de una cola de prioridad basada en arreglo

from PriorityQueueBase import PriorityQueueBase

class HeapPriorityQueue(PriorityQueueBase): # la clase base define _Item
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