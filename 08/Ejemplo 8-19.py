# Ejemplo 8-19. Clase recorrido de Euler

class EulerTour:
  """Clase base abstracta para realizar el recorrido de Euler de un arbol.

  _hook_previsit y _hook_postvisit pueden ser sobreescritas por la subclase.
  """
  def __init__(self, tree):
    """Prepara un template de una recorrido de Euler para un arbol."""
    self._tree = tree

  def tree(self):
    """Devuelve la referencia al arbol que esta siendo recorrido."""
    return self._tree

  def execute(self):
    """Realiza el recorrido y devuelve cualquier resultado de la postvisita"""
    if len(self._tree) > 0:
      return self._tour(self._tree.root(), 0, [])    # inicia la recursividad

  def _tour(self, p, d, path):
    """Realiza el recorrido del subarbol con raiz en la posicion p

    p        Posicion del nodo actual siendo visitado
    d        Profundidad de p en el arbol
    path     lista de indices de los hijos en el camino de la raiz a p
    """
    self._hook_previsit(p, d, path)                       # "pre visita" p
    results = []
    path.append(0)          # agrega nuevo indice al final del camino anterior a la recursion
    for c in self._tree.children(p):
      results.append(self._tour(c, d+1, path))  # recursion en el subarbol hijo
      path[-1] += 1         # incrementa el indice
    path.pop()              # remueve indices extranos al final del camino
    answer = self._hook_postvisit(p, d, path, results)    # "post visita" p
    return answer

  def _hook_previsit(self, p, d, path):
    pass

  def _hook_postvisit(self, p, d, path, results):
    pass