# Ejemplo 10-7. SortedTableMap

from .map_base import MapBase

class SortedTableMap(MapBase):
  """Implementación de mapa usando una tabla ordenada."""

  #----------------------------- comportamientos no públicos -----------------------------
  def _find_index(self, k, low, high):
    """Devuelve el índice del primer elemento con clave mayor o igual que k.

    Devuelve high + 1 si ningún elemento cumple la condición.

    Es decir, se devolverá j tal que:
       todos los elementos del segmento table[low:j] tienen clave < k
       todos los elementos del segmento table[j:high+1] tienen clave >= k
    """
    if high < low:
      return high + 1                               # ningún elemento cumple la condición
    else:
      mid = (low + high) // 2 
      if k == self._table[mid]._key:
        return mid                                  # coincidencia exacta encontrada
      elif k < self._table[mid]._key:
        return self._find_index(k, low, mid - 1)    # Nota: puede devolver mid
      else:
        return self._find_index(k, mid + 1, high)   # la respuesta está a la derecha de mid

  #----------------------------- comportamientos públicos -----------------------------
  def __init__(self):
    """Crea un mapa vacío."""
    self._table = []

  def __len__(self):
    """Devuelve el número de elementos en el mapa."""
    return len(self._table)

  def __getitem__(self, k):
    """Devuelve el valor asociado con la clave k (lanza KeyError si no se encuentra)."""
    j = self._find_index(k, 0, len(self._table) - 1)
    if j == len(self._table) or self._table[j]._key != k:
      raise KeyError('Key Error: ' + repr(k))
    return self._table[j]._value
  
  def __setitem__(self, k, v):
    """Asigna el valor v a la clave k, sobrescribiendo el valor existente si está presente."""
    j = self._find_index(k, 0, len(self._table) - 1)
    if j < len(self._table) and self._table[j]._key == k:
      self._table[j]._value = v                         # reasigna el valor
    else:
      self._table.insert(j, self._Item(k,v))            # agrega un nuevo elemento
  
  def __delitem__(self, k):
    """Elimina el elemento asociado con la clave k (lanza KeyError si no se encuentra)."""
    j = self._find_index(k, 0, len(self._table) - 1)
    if j == len(self._table) or self._table[j]._key != k:
      raise KeyError('Key Error: ' + repr(k))
    self._table.pop(j)                                  # elimina el elemento
  
  def __iter__(self):
    """Genera las claves del mapa ordenadas de mínimo a máximo."""
    for item in self._table:
      yield item._key

  def __reversed__(self):
    """Genera las claves del mapa ordenadas de máximo a mínimo."""
    for item in reversed(self._table):
      yield item._key

  def find_min(self):
    """Devuelve el par (clave, valor) con la clave mínima (o None si está vacío)."""
    if len(self._table) > 0:
      return (self._table[0]._key, self._table[0]._value)
    else:
      return None

  def find_max(self):
    """Devuelve el par (clave, valor) con la clave máxima (o None si está vacío)."""
    if len(self._table) > 0:
      return (self._table[-1]._key, self._table[-1]._value)
    else:
      return None

  def find_le(self, k):
    """Devuelve el par (clave, valor) con la mayor clave menor o igual que k.

    Devuelve None si no existe tal clave.
    """
    j = self._find_index(k, 0, len(self._table) - 1)      # la clave de j >= k
    if j < len(self._table) and self._table[j]._key == k:
      return (self._table[j]._key, self._table[j]._value)      # coincidencia exacta
    elif j > 0:
      return (self._table[j-1]._key, self._table[j-1]._value)  # Nota: uso de j-1
    else:
      return None

  def find_ge(self, k):
    """Devuelve el par (clave, valor) con la menor clave mayor o igual que k.

    Devuelve None si no existe tal clave.
    """
    j = self._find_index(k, 0, len(self._table) - 1)      # la clave de j >= k
    if j < len(self._table):
      return (self._table[j]._key, self._table[j]._value)
    else:
      return None

  def find_lt(self, k):
    """Devuelve el par (clave, valor) con la mayor clave estrictamente menor que k.

    Devuelve None si no existe tal clave.
    """
    j = self._find_index(k, 0, len(self._table) - 1)      # la clave de j >= k
    if j > 0:
      return (self._table[j-1]._key, self._table[j-1]._value)  # Nota: uso de j-1
    else:
      return None

  def find_gt(self, k):
    """Devuelve el par (clave, valor) con la menor clave estrictamente mayor que k.

    Devuelve None si no existe tal clave.
    """
    j = self._find_index(k, 0, len(self._table) - 1)      # la clave de j >= k
    if j < len(self._table) and self._table[j]._key == k:
      j += 1                                       # avanzar más allá de la coincidencia
    if j < len(self._table):
      return (self._table[j]._key, self._table[j]._value)
    else:
      return None

  def find_range(self, start, stop):
    """Itera sobre todos los pares (clave, valor) tales que start <= clave < stop.

    Si start es None, la iteración comienza con la clave mínima del mapa.
    Si stop es None, la iteración continúa hasta la clave máxima del mapa.
    """
    if start is None:
      j = 0
    else:
      j = self._find_index(start, 0, len(self._table)-1)   # encuentra el primer resultado
    while j < len(self._table) and (stop is None or self._table[j]._key < stop):
      yield (self._table[j]._key, self._table[j]._value)
      j += 1
