# Clase recorrido de Euler

class EulerTour:
  """Clase base abstracta para realizar el recorrido de Euler de un arbol.

  _hook_previsit y _hook_postvisit pueden ser sobreescritas por la subclase.
  """
  def __init__(self, tree):
    """Prepara un template de una recorrido de Euler para un árbol."""
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
    """Visita Position p, antes del recorrido de su hijo.

    p        Posicion de la posicion actual siendo visitada
    d        profundidad de p en el arbol
    path     lista de indices de los hijos en el camino de la raiz a p
    """
    pass

  def _hook_postvisit(self, p, d, path, results):
    """Visita Position p, despues del recorrido de su hijo.

    p        Posicion de la posicion actual siendo visitada
    d        profundidad de p en el arbol
    path     lista de indices de los hijos en el camino de la raiz a p
    results  una lista de los valores devueltos por _hook_postvisit(c)
            para cada hijo c of p.
    """
    pass

class PreorderPrintIndentedTour(EulerTour):
  def _hook_previsit(self, p, d, path):
   print(2*d*' ' + str(p.element()))

class PreorderPrintIndentedLabeledTour(EulerTour):
  def _hook_previsit(self, p, d, path):
    label = '.'.join(str(j+1) for j in path)    # etiquetas son one-indexed
    print(2*d*' ' + label, p.element())

class ParenthesizeTour(EulerTour):
  def _hook_previsit(self, p, d, path):
    if path and path[-1] > 0:                  # p sigue un sibling
      print(', ', end='')                      # de forma que lo precede con coma
    print(p.element(), end='')                 # entonces imprime el elemento
    if not self.tree().is_leaf(p):             # si p tiene hijos
      print(' (', end='')                      # imprime parentesis de apertura

  def _hook_postvisit(self, p, d, path, results):
    if not self.tree().is_leaf(p):             # si p tiene hijos
      print(')', end='')                       # imprime parentesis cerrados


class DiskSpaceTour(EulerTour):
  def _hook_postvisit(self, p, d, path, results):
    # simplemente agrega el espacio asociado con p al de sus subarboles
    return p.element().space() + sum(results)   

class BinaryEulerTour(EulerTour):
  """Clase base abstracta para realizar un recorrido de Euler en un árbol binario.

  Esta versión incluye un _hook_invisit adicional que se llama después del recorrido
  del subárbol izquierdo (si existe), pero antes del recorrido del subárbol derecho (si existe).

  Nota: El hijo derecho siempre se asigna con el índice 1 en el camino, incluso si no hay hermano izquierdo.
  """
  def _tour(self, p, d, path):
    results = [None, None]          # se actualizará con los resultados de las llamadas recursivas
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
    """Visita la posición p, entre el recorrido de sus subárboles izquierdo y derecho."""
    pass

class BinaryLayout(BinaryEulerTour):
  """Clase para calcular las coordenadas (x, y) de cada nodo de un arbol binario."""
  def __init__(self, tree):
    super().__init__(tree)           # se debe llamar al constructor de la clase padre
    self._count = 0                  # inicializa el contador de nodos procesados

  def _hook_invisit(self, p, d, path):
    p.element().setX(self._count)    # la coordenada x se asigna en serie usando el contador
    p.element().setY(d)              # la coordenada y es la profundidad
    self._count += 1                 # avanza el contador de nodos procesados
