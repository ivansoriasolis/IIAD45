# AdaptableHeapPriorityQueue

from HeapPriorityQueue import HeapPriorityQueue

class AdaptableHeapPriorityQueue(HeapPriorityQueue):
  """A locator-based priority queue implemented with a binary heap."""

  #------------------------------ clase Locator ------------------------------
  class Locator(HeapPriorityQueue._Item):
    """Token for locating an entry of the priority queue."""
    __slots__ = '_index'                 # agregar _index para rastrear la posición

    def __init__(self, k, v, j):
      super().__init__(k,v)
      self._index = j

  #------------------------------ comportamientos privados ------------------------------
  # redefinir swap para actualizar el índice del localizador
  def _swap(self, i, j):
    super()._swap(i,j)                   # realizar el intercambio en la lista
    self._data[i]._index = i             # resetear el índice del localizador (post-swap)
    self._data[j]._index = j             # resetear el índice del localizador (post-swap)

  def _bubble(self, j):
    if j > 0 and self._data[j] < self._data[self._parent(j)]:
      self._upheap(j)
    else:
      self._downheap(j)

  #------------------------------ comportamientos públicos ------------------------------
  def add(self, key, value):
    """Agregar un par key-value."""
    token = self.Locator(key, value, len(self._data)) # inicializar el localizador
    self._data.append(token)
    self._upheap(len(self._data) - 1)
    return token

  def update(self, loc, newkey, newval):
    """Actualizar la clave y valor para la entrada identificada por le localizador loc."""
    j = loc._index
    if not (0 <= j < len(self) and self._data[j] is loc):
      raise ValueError('Localizador inválido')
    loc._key = newkey
    loc._value = newval
    self._bubble(j)

  def remove(self, loc):
    """Remover y devolver el par (k,v) identificado por el localizador."""
    j = loc._index
    if not (0 <= j < len(self) and self._data[j] is loc):
      raise ValueError('Localizador inválido')
    if j == len(self) - 1:                # item a la última posición
      self._data.pop()                    # removerlo de la lista
    else:
      self._swap(j, len(self)-1)          # intercabiar con el último
      self._data.pop()                    # removerlo de la lista
      self._bubble(j)                     # reparar la propiedad del montículo
    return (loc._key, loc._value)             


if __name__ == '__main__':
    #Insertamos los pares (k, v) en cualquier orden
    ahpq = AdaptableHeapPriorityQueue()
    ahpq.add(4, 'C')
    ahpq.add(5, 'A')
    ahpq.add(6, 'Z')
    ahpq.add(15, 'K')
    l = ahpq.add(9, 'F')
    ahpq.add(7, 'Q')
    ahpq.add(20, 'B')
    ahpq.add(16, 'X')
    ahpq.add(25, 'J')
    m = ahpq.add(14, 'E')
    ahpq.add(12, 'H')
    ahpq.add(11, 'S')
    ahpq.add(8, 'W')
    
    #actualizamos la localizacion l    
    ahpq.update(l, 4, 'Z')
    
    #removemos la localizacion m
    ahpq.remove(m)
    
    #atendemos por prioridad
    while not ahpq.is_empty():
        print(ahpq.remove_min())