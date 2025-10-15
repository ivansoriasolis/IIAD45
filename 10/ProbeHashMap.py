# Ejemplo 10.6. ProbeHashMap

from HashMapBase import HashMapBase

class ProbeHashMap(HashMapBase):
  """Map hash implementado con sondeo lineal para resolucion de colisiones."""
  _AVAIL = object()       #sentinel para marcar celdas vaciadas

  def _is_available(self, j):
    """Retorna True si el indice j esta disponible en la tabla."""
    return self._table[j] is None or self._table[j] is ProbeHashMap._AVAIL

  def _find_slot(self, j, k):
    """Busca la clave k en el bucket en el indice j."""
    firstAvail = None
    while True:                               
      if self._is_available(j):
        if firstAvail is None:
          firstAvail = j                      # marca este como primar avail
        if self._table[j] is None:
          return (False, firstAvail)          # búsqueda ha fallado
      elif k == self._table[j]._key:
        return (True, j)                      # encuentra match
      j = (j + 1) % len(self._table)          # mantener el sondeo circular

  def _bucket_getitem(self, j, k):
    found, s = self._find_slot(j, k)
    if not found:
      raise KeyError('Key Error: ' + repr(k))        # no se encuentra match
    return self._table[s]._value

  def _bucket_setitem(self, j, k, v):
    found, s = self._find_slot(j, k)
    if not found:
      self._table[s] = self._Item(k,v)               # inserta nuevo item
      self._n += 1                                   # tamaño del map incrementa
    else:
      self._table[s]._value = v                      # sobreescribe valor

  def _bucket_delitem(self, j, k):
    found, s = self._find_slot(j, k)
    if not found:
      raise KeyError('Key Error: ' + repr(k))        # no se encuentra match
    self._table[s] = ProbeHashMap._AVAIL             # mark como vaciado

  def __iter__(self):
    for j in range(len(self._table)):                # escanea toda la tabla
      if not self._is_available(j):
        yield self._table[j]._key