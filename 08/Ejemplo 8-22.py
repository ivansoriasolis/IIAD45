#Ejemplo 8-22. Una subclase de EulerTour que imprime una representacion parentetica

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