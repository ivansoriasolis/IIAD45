# Ejemplo 9-1. Una clase PriorityQueueBase con una clase anidada _Item

class PriorityQueueBase:
  """Clase base abstracta para una cola de prioridad"""

  #--------------------------- clase anidada _Item ------------------------------
  class _Item:
    __slots__ = '_key', '_value'

    def __init__(self, k, v):
      self._key = k
      self._value = v

    def __lt__(self, other):
      return self._key < other._key

    def __repr__(self):
      return '({0},{1})'.format(self._key, self._value)

  #-------------------------- funcionalidad publica------------------------------
  def is_empty(self):                 
    """devuelve True si la cola de prioridad está vacía."""
    return len(self) == 0

  def __len__(self):
    """devuelve el número de elementos en la cola de prioridad."""
    raise NotImplementedError('debe ser implementada por la subclase')

  def add(self, key, value):
    """Agregar un par (clave, valor) a la cola de prioridad."""
    raise NotImplementedError('debe ser implementada por la subclase')

  def min(self):
    """devuelve (k,v) tupla con clave mínima sin eliminarlo.
    si está vacía, lanza la excepción Empty."""
    raise NotImplementedError('debe ser implementada por la subclase')

  def remove_min(self):
    """Devuelve (k,v) tupla con clave mínima y la elimina.
    si está vacía, lanza la excepción Empty."""
    raise NotImplementedError('debe ser implementada por la subclase')
