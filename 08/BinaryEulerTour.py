## -*- coding: utf-8 -*-

class BinaryEulerTour(EulerTour):
  """Clase base abstracta para realizar un recorrido de Euler en un arbol binario.

  Esta version incluye un _hook_invisit adicional que se llama despues del recorrido
  del subarbol izquierdo (si existe), pero antes del recorrido del subarbol derecho 
  (si existe).

  Nota: El hijo derecho siempre se asigna con el indice 1 en el camino, 
  incluso si no hay hermano izquierdo.
  """
  def _tour(self, p, d, path):
    results = [None, None] # se actualizara con los resultados de las llamadas recursivas
    self._hook_previsit(p, d, path)                  # "pre visita" para p
    if self._tree.left(p) is not None:               # considerar el hijo izquierdo
      path.append(0)
      results[0] = self._tour(self._tree.left(p), d+1, path)
      path.pop()
    self._hook_invisit(p, d, path)                   # "in visita" para p
    if self._tree.right(p) is not None:              # considerar el hijo derecho
      path.append(1)
      results[1] = self._tour(self._tree.right(p), d+1, path)
      path.pop()
    answer = self._hook_postvisit(p, d, path, results)    # "post visita" para p
    return answer

  def _hook_invisit(self, p, d, path):
    """Visita la posicion p, entre el recorrido de sus subarboles izquierdo y derecho."""
    pass