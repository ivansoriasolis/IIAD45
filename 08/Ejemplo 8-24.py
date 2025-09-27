# Ejemplo 8-24.py

from BinaryEulerTour import BinaryEulerTour

class BinaryLayout(BinaryEulerTour):
  """Clase para calcular las coordenadas (x, y) de cada nodo de un arbol binario."""
  def __init__(self, tree):
    super().__init__(tree)           # se debe llamar al constructor de la clase padre
    self._count = 0                  # inicializa el contador de nodos procesados

  def _hook_invisit(self, p, d, path):
    p.element().setX(self._count)    # la coordenada x se asigna en serie usando el contador
    p.element().setY(d)              # la coordenada y es la profundidad
    self._count += 1                 # avanza el contador de nodos procesados