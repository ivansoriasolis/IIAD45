# Se asume que SortedTableMap está disponible

from SortedTableMap import SortedTableMap

class CostPerformanceDatabase:
  """Mantiene una base de datos de pares (costo, rendimiento) máximos."""

  def __init__(self):
    """Crea una base de datos vacía."""
    self._M = SortedTableMap()             # o un mapa ordenado más eficiente

  def best(self, c):
    """Devuelve el par (costo, rendimiento) con el mayor costo que no excede c.

    Devuelve None si no existe tal par.
    """
    return self._M.find_le(c)

  def add(self, c, p):
    """Agrega una nueva entrada con costo c y rendimiento p."""
    # determinar si (c,p) está dominado por un par existente
    other = self._M.find_le(c)              # other es al menos tan barato como c
    if other is not None and other[1] >= p: # si su rendimiento es igual o mejor,
        return                              # (c,p) está dominado, así que se ignora
    self._M[c] = p                          # de lo contrario, agregar (c,p) a la base de datos
    # y ahora eliminar cualquier par que esté dominado por (c,p)
    other = self._M.find_gt(c)              # other más caro que c
    while other is not None and other[1] <= p:
      del self._M[other[0]]
      other = self._M.find_gt(c)

