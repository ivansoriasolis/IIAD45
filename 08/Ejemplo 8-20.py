#Ejemplo 8-20. Identado preorden

class PreorderPrintIndentedTour(EulerTour):
  def _hook_previsit(self, p, d, path):
   print(2*d*' ' + str(p.element()))