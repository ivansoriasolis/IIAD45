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
    if j == len(self) - 1:                # item at last position
      self._data.pop()                    # just remove it
    else:
      self._swap(j, len(self)-1)          # swap item to the last position
      self._data.pop()                    # remove it from the list
      self._bubble(j)                     # fix item displaced by the swap
    return (loc._key, loc._value)             
