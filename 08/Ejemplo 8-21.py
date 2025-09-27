#Ejemplo 8-21. Una subclase que devuelve una representacion identada y etiquetada4

class PreorderPrintIndentedLabeledTour(EulerTour):
  def _hook_previsit(self, p, d, path):
    label = '.'.join(str(j+1) for j in path)    # etiquetas son one-indexed
    print(2*d*' ' + label, p.element())